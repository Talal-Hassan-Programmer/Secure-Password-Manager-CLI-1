# imports
from cryptography.fernet import Fernet


def gen_key(): # Func for genrating Key
    key = Fernet.generate_key()
    with open("key.key","wb") as f:
        f.write(key)

try: # genrating a key 9in starting if there is no key.
    with open("key.key", "r") as p:
        pass
except:
    gen_key()


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
    try:

        with open("password.txt", "r") as f:
            for i in f:
                name , encrypted = i.strip().split(' : ', 1)
                decrypted = fernet.decrypt(encrypted.encode())
                print(f"{name} : {decrypted.decode()}")
    except FileNotFoundError:
        print("No passwords yet.")
        



def del_pass(): # password deleting func
    try:
        k = load_key()
        fernet = Fernet(k)
        ll = []
        with open("password.txt", "r") as f:
            for i in f:
                name , encrypted = i.strip().split(' : ', 1)
                decrypted = fernet.decrypt(encrypted.encode())
                ll.append(f"{name} : {decrypted.decode()}")
        for i in range(len(ll)):
            print(i+1,ll[i])
        pp = int(input("enter the number: "))
        
        while True:
            if pp > 0 and pp <= len(ll):
                ll.pop(pp-1)
                break
            else:
                pp = int(input("please enter a valid number: "))
        
        with open("password.txt", "w") as p:
            for i in ll:
                name, password = i.strip().split(' : ', 1)

                k = load_key()

                fernet = Fernet(k)

                encrypted = fernet.encrypt(password.encode())

                p.write(f"{name} : {encrypted.decode()} \n")
    
    except FileNotFoundError:
        print("No passwords yet.")




def search_pass():
    k = load_key()
    fernet = Fernet(k)
    search_name = input("pls enter the username:  ").lower()
    try:

        with open("password.txt", "r") as f:
            for i in f:
                name , encrypted = i.strip().split(' : ', 1)
                decrypted = fernet.decrypt(encrypted.encode())
                if (search_name) == (name.lower()) :
                    print(f"{name} : {decrypted.decode()}")
                
    except FileNotFoundError:
        print("No passwords yet.")




def main():
    while True:
        ch = ["add","delete","view","search","generate a new key","exit"]

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
        elif user == "search":
            search_pass()
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
