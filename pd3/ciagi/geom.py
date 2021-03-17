def n_ty(a1, n, q):
    return a1 * q**(n-1)

def suma_n(a1, n, q):
    if q != 1:
        return a1 * ((q - q**n) / (1 - q))
    else:
        return a1 * n