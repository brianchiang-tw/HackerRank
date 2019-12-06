def mutate_string(string, position, character):

    # method_#1
    #str_list = list( string )
    #str_list[position] = character
    #str_modified = ''.join(str_list)
    
    str_modified = mutate_string_method2( string, position, character)

    return str_modified


# method_#2
def mutate_string_method2(string, position, character):

    str_modified = string[:position] + character + string[position+1:]

    return str_modified

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)