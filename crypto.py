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
