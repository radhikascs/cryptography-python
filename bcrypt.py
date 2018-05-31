import bcrypt
password = bytes('password', 'utf-8')
hashed_pw = bcrypt.hashpw(password, bcrypt.gensalt(14))
print(hashed_pw)