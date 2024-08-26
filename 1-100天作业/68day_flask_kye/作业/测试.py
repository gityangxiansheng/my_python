from werkzeug.security import generate_password_hash,check_password_hash


password = '454565ddsadsaZZ'  
#密码转换为哈希值
password_hash = generate_password_hash(password)  

#检查密码是否正确
is_correct = check_password_hash(password_hash, password)  

print(is_correct)

print(password_hash)