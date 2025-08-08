# 🔐 Secure Password Manager CLI

A simple, beginner-friendly command-line password manager built with Python and the `cryptography` library. It allows you to securely store and retrieve encrypted passwords for different accounts using symmetric encryption (Fernet).

---

## 🚀 Features

- ✅ Secure password encryption using `cryptography.fernet`
- ✅ Add and store account-password pairs safely
- ✅ View and decrypt saved passwords
- ✅ Generate a new encryption key when needed (⚠️ resets all stored data)
- ✅ Simple CLI-based menu system

---

## 📁 Project Structure
Secure-Password-Manager-CLI-1/
│
├── main.py # Main program logic
├── key.key # Generated encryption key (ignored by Git) --Auto genrate via Func 
├── password.txt # Encrypted password storage -- Auto genrate 
├── .gitignore # Prevents sensitive files from being committed
└── README.md # This file


---

## ⚙️ How to Use

### 🔧 Requirements:
- Python 3.7+
- `cryptography` module

Install it with:
```bash
pip install cryptography

python main.py
You'll see a menu like this:

What would you like to do?
add
view
generate a new key
exit


Choose an option to add/view passwords, or generate a new encryption key.

⚠️ WARNING
If you generate a new key, all previously stored passwords become unreadable.
Only do this when starting fresh.

🧠 How It Works
Passwords are encrypted with a key stored in key.key.

Encrypted passwords are saved in password.txt with the format:
    account_name : encrypted_password
When viewing, the encrypted password is decrypted back to plaintext using the same key.

🛡️ Security Notes
Keep key.key private — anyone with it can decrypt your passwords.

.gitignore is set to exclude key.key from being uploaded to GitHub. *- key.key is genrated in the folder not in .gitignore

✍️ Author
Talal Hassan
Student & Aspiring Cybersecurity Engineer 🇶🇦
🔗 [GitHub Profile](https://github.com/Talal-Hassan-Programmer)

📌 License
This project is licensed under the MIT License — feel free to modify and use it for personal learning.

