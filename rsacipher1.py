import rsa

(pubkey, privkey)= rsa.newkeys(1024)
print(pubkey)
print(privkey)

message = b'criptografia'
crypto=rsa.encrypt(message, pubkey)
print(crypto)

decrypt= rsa.decrypt(crypto,privkey)
print(decrypt.decode())