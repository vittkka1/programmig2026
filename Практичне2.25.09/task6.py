password=input("Введіть пароль")
lower=False
upper=False
number=False
for char in password:
    if char.islower():
        lower=True
    elif char.isupper():
        upper=True
    elif char.isnumber():
        number=True
if lower and upper and number:
    print("Password is secure")
else:
    print("Password is insecure")