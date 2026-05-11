def encrypt(m: str, k: int) -> str:
    encryptm = ""
    for a in m:
        encryptm += chr(ord(a)^k)
    return encryptm
