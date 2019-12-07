# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    x, y = int( input() ), int( input() )

    qr_tuple = divmod(x, y)
    print( f'{qr_tuple[0]}\n{qr_tuple[1]}\n{qr_tuple}')
