
def fibonacci(n):
    """Returns nth term of from the fibonacci sequence"""
    prev, next=(1,1)

    for i in range(0, n-2):
            prev, next= next, prev+next

    return(next)

def lucas(n):
    """Returns nth term of from the lucas sequence"""
    prev, next=(2,1)

    for i in range(0, n-2):
            prev, next= next, prev+next

    return(next)


def sum_series(n, term1=0, term2=1):
"""Determins if there is or is not an input, will run either the fibonacci function or the lucas function"""

    if term1 == 0 and term2 ==1:
        return fibonacci(n)
    if term1 == 2 and term2 ==1:
        return lucas(n)
        
        
        
        
    #     # return(n, args1)
    # if n==1 and args1 == (2, 1):
    #     # return("Im happy")
      
    # if args1 == '':

# Original Code        
# def sum_series(n, *args1):
#         # return(n, args1)
#     if n==1 and args1 == (2, 1):
#         # return("Im happy")
#         return lucas(n)
      
#     if args1 == '':
#         return fibonacci(n)




if __name__ == "__main__":
    n = int(input())