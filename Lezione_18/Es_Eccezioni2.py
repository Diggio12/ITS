def validate_password(password:str):
    x:int = 0
    y:int = 0
    if len(password) >= 20:
        for i in password:
            if i.isupper() == True:
                x += 1
            elif i.isalnum() == True:
                y += 1
                if y >= 4 and x >= 3:
                    print('Password checks criteria')

    else:
        raise SyntaxError(f'The password does not meet the criteria')
    
validate_password('Aksalore')
