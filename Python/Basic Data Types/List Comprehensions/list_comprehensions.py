def grid_of_requirement( x, y, z, n ):

    X, Y, Z = list( range(0, x+1) ), list( range(0, y+1) ), list( range(0, z+1) )

    solution = [ [i,j,k] for i in X for j in Y for k in Z if i+j+k != n]

    return solution


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    coordinate = grid_of_requirement(x, y, z, n)
    print( coordinate )
