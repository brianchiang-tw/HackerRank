def split_and_join(line):
    # write your code here

    pure_token = list( line.split() )

    gen_str = "-".join( pure_token )

    return gen_str


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)