# imports
from cryptography.fernet import Fernet


def gen_key(): # Func for genrating Key
    key = Fernet.generate_key()
    with open("key.key","wb") as f:
        f.write(key)


def load_key(): #loading Key from key.key
    with open("key.key", "rb") as f:
        return f.read()
    


def add_pass(): # adding new passwords
    name = input("enter account name:")
    password = input("enter you password:")

    k = load_key()

    fernet = Fernet(k)

    encrypted = fernet.encrypt(password.encode())

    with open("password.txt", "a") as p:
        p.write(f"{name} : {encrypted.decode()} \n")


def get_pass(): # getting all passwords
    k = load_key()
    fernet = Fernet(k)

    with open("password.txt", "r") as f:
        for i in f:
            name , encrypted = i.strip().split(" : ")
            decrypted = fernet.decrypt(encrypted.encode())
            print(f"{name} : {decrypted.decode()}")
def del_pass():
    k = load_key()
    fernet = Fernet(k)
    ll = []
    with open("password.txt", "r") as f:
        for i in f:
            name , encrypted = i.strip().split(" : ")
            decrypted = fernet.decrypt(encrypted.encode())
            ll.append(f"{name} : {decrypted.decode()}")
    for i in range(len(ll)):
        print(i+1,ll[i])
    pp = int(input("enter the number: "))
    with open("password.txt", "a") as p:
    
        p.write("")
    if pp <=0:
        pp = int(input("Please enter the a valid number: "))
    else:
        ll.pop(pp-1)
    
    with open("password.txt", "w") as p:
        for i in ll:
            name, password = i.strip().split(" : ")

            k = load_key()

            fernet = Fernet(k)

            encrypted = fernet.encrypt(password.encode())

            p.write(f"{name} : {encrypted.decode()} \n")
    
    
    pass
def main():
    while True:
        ch = ["add","delete","view","generate a new key (for first time do it)","exit"]

        print("what whould you like to do")
        for i in ch:
            print(i)

        user = input().lower()
        if user == "add":
            add_pass()
        elif user == "delete":
            del_pass()
        elif user == "view":
            get_pass()
        elif user == "generate a new key":
            confirm = input("⚠️ This will delete the old key and make all stored passwords unreadable. Are you sure? (yes/no): ").strip().lower()
            if confirm == "yes":
                gen_key()
                print("✅ New key generated.")
            
        elif user == "exit":
            break
        else:
            print("Enter a valid choice.")


main()
