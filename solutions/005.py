
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to
10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the 
numbers from 1 to 20?
"""

from util.functions import getfactors

def run() -> int:

    res = 1
    for i in range( 1, 21 ):
        
        a = getfactors( i )
        
        if a == []:
            res *= i
        
        else:
            for x in a:
                
                if res % i != 0:
                    res*= x

                else:
                    break
                    
    return res

if __name__ == '__main__':
    print( run())
