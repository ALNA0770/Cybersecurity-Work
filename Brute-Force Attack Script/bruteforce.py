'''
Forage AIG Cybersecurity Program
Bruteforce starter template
'''
from zipfile import ZipFile, BadZipFile

def attempt_extract(zf_handle, password):
    try:
        zf_handle.extractall(pwd=password.encode('utf-8'))
        return True
    except (RuntimeError, BadZipFile):
        return False

def main():
    print("[+] Beginning brute-force attack")
    # Use the absolute path to your ZIP file
    with ZipFile(r"your0file0path") as zf:
        with open(r"your0file0path", 'r', encoding='latin1') as f:
            for line in f:
                password = line.strip()
                if attempt_extract(zf, password):
                    print(f"[+] Password found: {password}")
                    return
                else:
                    print(f"[-] Attempted password: {password}")

    print("[+] Password not found in list")

if __name__ == "__main__":
    main()
