def wrapper(f):
    def fun(l):
        # complete the function

        for i, phone_number in enumerate(l):

            if len(phone_number) == 10:
                l[i] = "+91" + " " + phone_number[0:5] + " " + phone_number[5:]

            elif phone_number[0] == '0':

                l[i] = "+91" + " " + phone_number[1:6] + " " + phone_number[6:]
            
            elif phone_number[0:2] == '91':

                l[i] = "+91" + " " + phone_number[2:7] + " " + phone_number[7:]
            
            elif phone_number[0:3] == '+91':

                l[i] = "+91" + " " + phone_number[3:8] + " " + phone_number[8:]

        # run run core function with formatted list l
        return f(l)

    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


