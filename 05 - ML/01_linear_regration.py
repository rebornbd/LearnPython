
def linearRegration(xi, yi, fx):
    '''
    y = b + mx

    m = Σ[(x – x̄)(y -  ȳ)] / Σ[(x – x̄)2]
    b =  ȳ - mx̄
    '''

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


def rsquared(xi, yi):
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

    '''
    r^2 = 1 - (ssr / sst)

    ssr(sum squared regression) = Σ[(yi - ŷ)^2]     | ŷ = y estimate
    sst(total sum of squares)   = Σ[(yi - ȳ)^2]     | ȳ = mean
    
    if  r^2 == 1: perfect fit
        r^2 == 0: can't fit
    '''
    ssr = sst = 0
    for i in range(0, N):
        _yi = b + (m * xi[i])

        ssr = ssr + ((yi[i] - _yi) * (yi[i] - _yi))
        sst = sst + ((yi[i] - Y) * (yi[i] - Y))
    
    rsqure = 1 - (ssr / sst)

    return rsqure


def main():

    # pizza size (inch)
    # xi = [6, 8, 12, 14, 18]
    xi = [1, 2, 3, 4, 5]

    # pizza price (tk)
    # yi = [350, 775, 1150, 1395, 1675]
    yi = [1, 20, -30, 40, -5]

    # if pizza size is 17, find prize?
    x = 17

    y = linearRegration(xi, yi, x)
    rsqure = rsquared(xi, yi)

    print("  y:", y)
    print("r^2:", rsqure)

main()
