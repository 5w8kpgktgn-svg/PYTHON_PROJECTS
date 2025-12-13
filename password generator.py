import secrets
import string
def generator_password(
        length=7,
        upper=True,
        lower=True,
        digits=True,
        symbol=True
):
    upper_list=string.ascii_uppercase
    lower_list=string.ascii_lowercase
    digits_list=string.digits
    symbol_list="!@#$%^&*()-_=+[]{};:,.<>?/"

    caracter=""
    password=[]

    if upper:
        caracter+=upper_list
        password.append(secrets.choice(upper_list))
    if lower:
        caracter+=lower_list
        password.append(secrets.choice(lower_list))
    if digits:
        caracter+=digits_list
        password.append(secrets.choice(digits_list))
    if symbol:
        caracter+=symbol_list
        password.append(secrets.choice(symbol_list))
    if not caracter:
        raise ValueError("at least one character type must be selected!")
    if length<len(password):
        raise ValueError("The password length cannot be less than the selected character type!")
    
    minus=length-len(password)
    for _ in range(minus):
        password.append(secrets.choice(caracter))
    
    secrets.SystemRandom().shuffle(password)
    return "".join(password)
password=generator_password(length=8)
print("generated password:",password)

