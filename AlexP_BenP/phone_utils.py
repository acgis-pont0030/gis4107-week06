def is_valid_phone_number(phone_number):
    if phone_number[0:2,4:6,11].isdigit() and phone_number[3,7] == '-':
        return True
    else:
        return False
    