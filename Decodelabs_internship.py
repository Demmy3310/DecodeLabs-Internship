print("PASSWORD STRENGTH CHECKER")
password= input("TYPE IN PASSWORD")
has_uppercase= False
for character in password:
    if character.isupper():
        has_uppercase= True
has_lowercase= False
for character in password:
    if character.islower():
        has_lowercase= True
has_digit=False
for character in password:
    if character.isdigit():
        has_digit= True
has_symbol= False
for character in password:
    if not character.isalnum():
        has_symbol= True
if len(password)>=10 and has_lowercase and has_uppercase and has_digit and has_symbol:
    print("Strong")
elif len(password)>=8 and has_uppercase and has_lowercase and has_digit and has_symbol:
    print("medium")
else: 
    print("Weak")