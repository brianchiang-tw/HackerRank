cube = lambda x: x**3# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    
    fib_list = [0] * n
    
    # Initialization for first two terms
    if n >= 1:
        fib_list[0] = 0

    if n >= 2:
        fib_list[1] = 1

    for i in range(2, n):
        fib_list[i] = fib_list[i-1] + fib_list[i-2]

    
    return fib_list


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))