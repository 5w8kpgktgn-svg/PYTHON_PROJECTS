import secrets
import string
def generator_password(
        length=7,
        upper=True,
        lower=True,
        digits=True,
        symbol=True
):
    upper_letters=string.ascii_uppercase
    lower_letters=string.ascii_lowercase
    digits=string.digits
    symbol="!@#$%^&*()-_=+[]{};:,.<>?/"

    caracter=""
    password=[]

    if upper:
        caracter+=upper_letters
        password.append(secrets.choice(upper_letters))
    if lower:
        caracter+=lower_letters
        password.append(secrets.choice(lower_letters))
    if digits:
        caracter+=digits
        password.append(secrets.choice(digits))
    if symbol:
        caracter+=symbol
        password.append(secrets.choice(symbol))
    if not caracter:
        raise ValueError("at least one character type must be selected!")
    if length<len(password):
        raise ValueError("The password length cannot be less than the selected character type!")
    
    remaining_length=length-len(password)
    for _ in range(remaining_length):
        password.append(secrets.choice(caracter))
    
    secrets.SystemRandom().shuffle(password)
    return "".join(password)
password=generator_password(length=8)
print("generated password",password)
