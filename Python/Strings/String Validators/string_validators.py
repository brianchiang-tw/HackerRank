def string_check_with_func(s, opcode):

        
    for char in s:

        chk_flag = None

        if opcode == "isalnum":
            chk_flag = char.isalnum()

        elif opcode == "isalpha":
            chk_flag = char.isalpha()

        elif opcode == "isdigit":
            chk_flag = char.isdigit()

        elif opcode == "islower":
            chk_flag = char.islower()

        elif opcode == "isupper":
            chk_flag = char.isupper()



        if chk_flag is True:
            print("True")
            break    
    else:
        print("False")


def string_checker( s ):

    # alphabet or numeric
    string_check_with_func(s, "isalnum" ) 

    # alphabet
    string_check_with_func(s, "isalpha" )     

    # digit 0 ~ 9
    string_check_with_func(s, "isdigit" ) 

    # lowercase letter
    string_check_with_func(s, "islower" ) 

    # uppercase letter
    string_check_with_func(s, "isupper" ) 

    return


if __name__ == '__main__':
    s = input()

    string_checker( s )
