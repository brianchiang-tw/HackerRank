def swap_case(s):

    swap_str = str()
    for i in range( len(s) ):

        char = s[i]

        if char.islower():
            swap_str += char.upper()

        elif char.isupper():
            swap_str += char.lower()
        
        else:
            swap_str += char
            continue


    return swap_str

if __name__ == '__main__':