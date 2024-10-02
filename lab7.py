import hashlib
import bcrypt

# sring to hash
password = "my_secure_password"

#MD5
md5_hash=hashlib.md5(password.encode()).hexdigest()
print("MD5:",md5_hash)

#SHA-1
sha1_hash=hashlib.sha1(password.encode()).hexdigest()
print("sha1:",sha1_hash)
 #bcrypt
bcrypt_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
print("bcrypt:", bcrypt_hash.decode())
#SHA-256
sha256_hash=hashlib.sha256(password.encode()).hexdigest()
print("sha256:",sha256_hash)
#SHA512
sha512_hash=hashlib.sha512(password.encode()).hexdigest()
print("sha512:",sha512_hash)

    #BLAKE2
blake2_hash=hashlib.blake2b(password.encode()).hexdigest()
print("blake2:",blake2_hash)

    #SHA-3
sha3_256_hash=hashlib.sha3_256(password.encode()).hexdigest()
print("sha3:", sha3_256_hash)