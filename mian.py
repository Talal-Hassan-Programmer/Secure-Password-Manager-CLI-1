# imports
from cryptography.fernet import Fernet


def gen_key(): # Func for genrating Key
    key = Fernet.generate_key()
    with open("key.key","wb") as f:
        f.write(key)

x = input("what to genrate a new key (yes/no) : ").lower()
if x == "yes": # asking for key generation
    gen_key() 


def load_key(): #loading Key from key.key
    with open("key.key", "rb") as f:
        return f.read()
    


def add_pass():
    name = input("enter account name:")
    password = input("enter you password:")

    k = load_key()

    fernet = Fernet(k)

    encrypted = fernet.encrypt(password.encode())

    with open("password.txt", "a") as p:
        p.write(f"{name} : {encrypted.decode()} \n")


add_pass()