def is_valid_phone_number(phone_number):
    if ''.join(phone_number[i] for i in [0:2, 4:6, 8:11]).isdigit() and ''.join(phone_number[i] for i in [3, 7]) == '--':
        return True
    else:
        return False