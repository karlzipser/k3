from k3 import *

"""
def sigma(m):
    P = Percent('calling sigma( '+str(m)+' )')
    timer = Timer(1)
    q = 0
    for n in range(1,m+1):
        if n % 500 == 0:
            P.show(n,m+1)
        q += 1/n
    return q
"""

def sigma_(m,f):
    P = Percent('calling sigma( '+str(m)+' )')
    timer = Timer(1)
    q = 0
    for n in range(1,m+1):
        if n % 500 == 0:
            P.show(n,m+1)
        q += f(n)
    return q

def f(n):
    return 1/n

if __name__ == '__main__':
    A = get_Arguments({'k':10})
    k = A['k']
    print('k =',k)
    a = sigma_(3**k,f)
    b = sigma_(3**(k-1),f)
    print('output =',a-b)