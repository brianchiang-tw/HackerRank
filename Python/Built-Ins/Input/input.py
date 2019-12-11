# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':

    x, target = map(int, input().split() )

    polynomail = input()

    if eval(polynomail) == target:
        print("True")

    else:
        print("False")
