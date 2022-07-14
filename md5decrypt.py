import hashlib

hashed_password = input("type MD5 hash : ")

wordlist = input("wordlist : ")

for password in open(wordlist, 'r').readlines():
    hashed = hashlib.md5(password.strip().encode()).hexdigest()
    if hashed == hashed_password:
        print(f' password is {password}')