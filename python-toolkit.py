import socket
import re
import hashlib
from concurrent.futures import ThreadPoolExecutor

while True:
    print("""Mini Cyber Security Toolkit (Python CLI Project)\n
       1. URL Checker Enter(1) \n
       2. Password Checker Enter(2) \n
       3. Port Scanner Enter(3) \n
       4. File Hasher Enter(4) \n
       5. Login System Enter(5) \n
       6. Exit Enter(6) \n """)
    menu = int(int(input("ENTER: ")))

    def url_checker():
        score = 0
        reason = []
        url = input("Enter url: ").strip().lower() #strip string k start or end sy space remove kerta hei
        if not url.startswith("https://"):
             score += 1
             reason.append("No Https (Not Safe)")
        print("Score:", score)
        print("Reason:", reason)

        keywords=["login","verify","update","bank","free","secure","account"]
        for word in keywords:
            if word in url:
                score += 1
                reason.append(f"Contains suspicious keyword: {word}")

        if len(url) > 100:
            score += 1
            reason.append("Url is too long")

        if url.count('.') > 4:
            score += 1
            reason.append("Too many dots in Url")

        ip_pattern = r"\d{1,3}(\.\d{1,3}){3}"
        if re.search(ip_pattern, url):
            score += 2
            reason.append("URL contains IP address")

        print("\n=== Result ===")
        if score == 0:
            print("SAFE URL")
        elif score <= 2:
            print("SUSPICIOUS URL")
        else:
            print("DANGEROUS (PHISHING) URL")

        print("\nReasons:")
        for r in reason:
            print("-", r)


    def password_checker():
        while True:
            print("Enter your Password to check weak or strong: ")
            passkey = str(input())

            if len(passkey) < 5:
                print("lenght is too short(weak password)")
            elif not any(c.isupper() for c in passkey) and any(c.islower() for c in passkey):
                print("Uppercase and lowercase is importand for strong passkeys(weak password)")
            elif not any(char.isdigit() for char in passkey):
                print("There is no number in passkey It importand(Weak Password)")
            elif not any(not char.isalnum() for char in passkey):
                print("Ther is no symbols(weak password")
            else:
                print("Strong password")
                break


    def scan_port():
        print("Enter your IP Address: ")
        ip = input()

        def port_scanner(port):
            s = socket.socket()
            s.settimeout(0.5)

            result = s.connect_ex((ip, port))

            if result == 0:
                print(f"[OPEN] Port {port}")
            s.close()

        with ThreadPoolExecutor(max_workers=100) as executor:
            executor.map(port_scanner, range(1, 1025))

    def file_hasher():
        print("Type any confidential message for convert to hash: ")
        msg = str(input())

        hash_object = hashlib.sha256(msg.encode())
        hash_result = hash_object.hexdigest()

        print("YOur message successfully convert into sha256: ", hash_result)

    def long_system():
        print("LOGIN SYSTEM: 3 attempts allowed")

        username = "admin"
        password = "admin"
        attempts = 0

        while attempts < 3:
            idname = input("Enter username: ")
            user_password = input("Enter password: ")

            if idname == username and user_password == password:
                print("LOGIN SUCCESSFULLY")
                break
            else:
                attempts += 1
                print("Wrong Credential Try Again")

        if attempts == 3:
            print("User blocked")

    match menu:
        case 1:
            menu == 1
            url_checker()
        case 2:
            menu == 2
            password_checker()
        case 3:
            menu == 3
            scan_port()
        case 4:
            menu == 4
            file_hasher()
        case 5:
            menu == 5
            long_system()
        case 6:
            menu == 6
            exit
