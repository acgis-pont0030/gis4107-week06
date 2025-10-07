def is_valid_phone_number(phone_number):
    if len(phone_number) == 12 and ''.join(phone_number[i] for i in [3, 7]) == '--':
        if ''.join((phone_number[i] for i in range(0,2))).isdigit() and ''.join((phone_number[i] for i in range(4,6))).isdigit() and ''.join((phone_number[i] for i in range(8,11))).isdigit():
            return True
        else:
            return False
    else:
        return False