
if __name__ == '__main__':

    return_d, return_m, return_y = map( int, input().split() )
    expect_d, expect_m, expect_y = map( int, input().split() )

    fine = 0;

    if  expect_y > return_y \
        or ( expect_y == return_y and expect_m > return_m ) \
        or ( expect_y == return_y and expect_m == return_m and expect_d > return_d ):
        
        pass

    elif return_d > expect_d and expect_m == return_m and expect_y == return_y :
        fine = 15 * ( return_d - expect_d )

    elif return_m > expect_m and expect_y == return_y :
        fine = 500 * ( return_m - expect_m )
    
    else:
        fine = 10000

    print( fine )

        