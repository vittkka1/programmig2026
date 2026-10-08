def create_user(username,role='user',status="active"):
    return f"Користувач: {username}, Роль: {role}, Статус: {status}"
user_name=create_user(" ")
print(user_name)
admin=create_user (" ",role="admin")
print(admin)