import bcrypt

def generate_hash_pwd(password):
    
    hash_pwd = bcrypt.hashpw(password.encode('utf-8'),salt=bcrypt.gensalt())
    
    return hash_pwd.decode('utf-8')
    