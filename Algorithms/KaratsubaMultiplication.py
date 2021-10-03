
#Reduces the multiplication of two n-digit numbers to at most  n^{\log_23}\approx n^{1.585} single-digit multiplications in general

def KaratsubaMultiplication(x, y):
    if x < 10 and y < 10:
        return x * y

    num1_len = len(str(x))
    num2_len = len(str(y))

    n = max(num1_len,num2_len)
    
    nby2 = round(n/2)
    # round decides to be floor or ceil value
    num1 = x // (10 ** nby2)
    rem1 = x % (10 ** nby2)

    # of ceil or floor recursively
    num2 = y // (10 ** nby2)
    rem2 = y % (10 ** nby2)

    ac = KaratsubaMultiplication(num1, num2)
    bd = KaratsubaMultiplication(rem1, rem2)
    ad_plus_bc = KaratsubaMultiplication(num1 + rem1, num2 + rem2) - ac - bd

    return (10 ** (2*nby2))*ac + (10 ** nby2)*ad_plus_bc + bd

print(KaratsubaMultiplication(1234343,5672438))
