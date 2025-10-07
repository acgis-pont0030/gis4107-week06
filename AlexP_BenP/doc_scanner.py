def has_x_code(in_text):
    encode = 'Tx6op3'
    if encode in in_text:
        return True
    else:
        return False

def get_x_code_position(in_text):
    encode = 'Tx6op3'
    if encode in in_text:
        return in_text.find(encode)+1
    else:
        return -1

    
   