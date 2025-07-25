# 🔐 Password Cracking & Hashing – Cybersecurity Project

This project demonstrates how passwords are stored securely using cryptographic hash functions and explores techniques used to crack weak passwords using brute-force and dictionary attacks.

> ⚠️ **Note:** This project is intended strictly for **educational purposes** and to raise awareness about password vulnerabilities. Do not use this knowledge for unethical purposes.

---

## 📁 Project Structure


---

## 🧩 Project Description

This project includes **two core modules**:

### 1️⃣ Password Cracking

- **Brute-force attack**:
  - Tries every possible combination of characters
  - Works on small and simple passwords
- **Dictionary attack**:
  - Uses a file of common passwords to guess user passwords
  - Fast but only as good as the dictionary used

### 2️⃣ Hashing Algorithms

- Demonstrates how to securely hash and verify passwords using:
  - `MD5`, `SHA1`, `SHA256` (for demonstration)
  - `bcrypt` (industry-recommended with salt)

---

## 🚀 How to Run the Code

> ✅ Prerequisite: Install Python and `bcrypt`

Install dependencies:
```bash
pip install bcrypt

python advanced_hash_demo.py
python advanced_brute_force_demo.py
python advanced_dictionary_attack.py


Hashing
yaml
Copy
Edit
MD5 Hash:       03ff9bba2d24446a8c90e967de66eaa5
SHA1 Hash:      c3ce83e4b2b934c84e11c042160f67122e449508
SHA256 Hash:    3975db6c57f8f94dc86138b6bca418f9982db81ac9f5821598fd73e31f7bba41
bcrypt Hash:    $2b$12$V86Xrs1yo4...
Password Verified using bcrypt: ✅ Success




Brute-force Attack
yaml
Copy
Edit
Trying: a
Trying: b
...
Password found: 12a
Time taken: 3.21 seconds

Dictionary Attack
yaml
Copy
Edit
Trying password: password123
Trying password: welcome
Password matched: letmein
Time taken: 0.01 seconds
