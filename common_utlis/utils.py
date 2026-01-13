import bcrypt

def generate_hash_pwd(password):
    
    hash_pwd = bcrypt.hashpw(password.encode('utf-8'),salt=bcrypt.gensalt())
    
    return hash_pwd.decode('utf-8')

def verify_pwd(hash_pwd,raw_pwd):
    # raw_pwd = raw_pwd.encode('utf-8')
    
    return bcrypt.checkpw(raw_pwd.encode('utf-8'),hash_pwd.encode('utf-8'))