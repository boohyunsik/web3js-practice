import hashlib

from ecdsa import SigningKey, SECP256k1
sk = SigningKey.generate(curve=SECP256k1)
print(sk.to_string().hex())

vk = sk.verifying_key
print(vk)

signature = sk.sign(b"message")
print(signature)

result = vk.verify(signature, b"message")
print(result)


///////////

from Crypto.PublicKey import RSA
from hashlib import sha512

keyPair = RSA.generate(bits=1024)

msg = b'Test'
hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
print("hash", hash)
signature = pow(hash, keyPair.d, keyPair.n)

print("signature : ", hex(signature))

hashFromSignature = pow(signature, keyPair.e, keyPair.n)
print("hashFromSignature", hashFromSignature)


/////////////

from ecies.utils import generate_key
from ecies import encrypt, decrypt

secret_key = generate_key()
sk_bytes = secret_key.secret
pk_bytes = secret_key.public_key.format(True)

message = b"test"

encrypted_message = encrypt(pk_bytes, message)
print(encrypted_message)

decrypted_message = decrypt(sk_bytes, encrypted_message)
print(decrypted_message)
