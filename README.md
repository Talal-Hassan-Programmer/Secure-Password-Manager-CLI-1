# 🔐 Secure Password Manager CLI

A beginner-friendly command-line password manager built with Python. Stores and retrieves passwords using symmetric encryption via the `cryptography` library (Fernet).

> Built as part of a personal Python + cybersecurity learning roadmap.

---

## ✨ Features

| Feature | Status |
|---|---|
| AES-based encryption via Fernet | ✅ |
| Add account/password pairs | ✅ |
| View & decrypt saved passwords | ✅ |
| Delete a specific password entry | ✅ |
| Auto-generate key on first run | ✅ |
| Re-generate encryption key (with confirmation) | ✅ |
| Input validation & error handling | ✅ |

---

## 📁 Project Structure

```
Secure-Password-Manager-CLI-1/
│
├── main.py          # All program logic
├── key.key          # Auto-generated encryption key (git-ignored)
├── password.txt     # Encrypted password storage (auto-created)
├── .gitignore       # Excludes key.key and password.txt
└── README.md        # This file
```

---

## ⚙️ Setup & Usage

### Requirements
- Python 3.7+
- `cryptography` library

```bash
pip install cryptography
```

### Run

```bash
python main.py
```

### Menu

```
what would you like to do
add
delete
view
generate a new key
exit
```

- **add** — enter an account name and password to encrypt and store it
- **delete** — lists all entries by number; enter the number to remove
- **view** — decrypts and displays all stored passwords
- **generate a new key** — creates a new key (requires confirmation; see warning below)
- **exit** — close the program

---

## 🧠 How It Works

1. On first run, a Fernet encryption key is auto-generated and saved to `key.key`
2. When you add a password, it is encrypted and written to `password.txt` in the format:
   ```
   account_name : <encrypted_token>
   ```
3. When you view passwords, each token is decrypted using the same key
4. Delete re-encrypts the remaining entries and rewrites the file

---

## ⚠️ Warning

Generating a new key will make **all existing stored passwords permanently unreadable**. Only do this when starting fresh. A confirmation prompt is required before the key is replaced.

---

## 🛡️ Security Notes

- `key.key` is excluded from Git via `.gitignore` — never commit it
- Anyone with access to `key.key` can decrypt your passwords
- This project is intended for **learning purposes** — not production use

---

## ✍️ Author

**Talal Hassan** — Competitive Programmer · IOI Qatar 2026 National Champion · Cybersecurity Enthusiast 🇶🇦

[GitHub — Talal-Hassan-Programmer](https://github.com/Talal-Hassan-Programmer)

---

## 📌 License

Licensed under the [MIT License](https://opensource.org/licenses/MIT) — free to use and modify for personal learning.
