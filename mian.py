# imports
from cryptography.fernet import Fernet


def gen_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as f:
        f.write(key)

x = input("what to genrate a new key (yes/no) : ").lower()
if x == "yes":
    gen_key()

