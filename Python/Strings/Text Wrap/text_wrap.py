import textwrap

def wrap(string, max_width):

    text_wrapped = str()

    for i in range(len(string)):
        # print( string[i], end='')
        text_wrapped += string[i]

        if (i+1)%max_width == 0:
            # print()
            text_wrapped += '\n'

    return text_wrapped

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)