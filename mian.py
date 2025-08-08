# imports
from cryptography.fernet import Fernet


def gen_key(): # Func for genrating Key
    key = Fernet.generate_key()
    with open("key.key","wb") as f:
        f.write(key)

x = input("what to genrate a new key (yes/no) : ").lower()
if x == "yes": # asking for key generation
    gen_key() 


def load_key():
    with open("key.key", "rb") as f:
        return f.read()
    
print(load_key()) #Checking if the key is loaded
