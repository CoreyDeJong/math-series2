
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


def sum_series(n, *args):
    if args == '':
        fibonacci(n)
    if args == '2,1':
        lucas(n)





if __name__ == "__main__":
    n = int(input())