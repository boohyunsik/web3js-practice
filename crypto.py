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
