
def linearRegration(xi, yi, fx):
    X = Y = 0
    N = len(xi)

    for i in range(0, N):
        X = X + xi[i]
        Y = Y + yi[i]
    
    X = X/N
    Y = Y/N

    xx = xxyy = 0
    for i in range(0, N):
        x_x = xi[i] - X
        y_y = yi[i] - Y

        xx   = xx + (x_x * x_x)
        xxyy = xxyy + (x_x * y_y)
    
    m = xxyy / xx
    b = Y - (m * X)

    return (b+ (m*fx))


def main():

    # pizza size (inch)
    xi = [6, 8, 12, 14, 18]

    # pizza price (tk)
    yi = [350, 775, 1150, 1395, 1675]

    # if pizza size is 17, find prize?
    x = 17

    y = linearRegration(xi, yi, x)

    print(y)

main()
