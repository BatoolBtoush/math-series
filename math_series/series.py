
def fibonacci(n):
    """
    This function takes n as an argument and returns the fibonacci value for it
    based on what the fibonacci series is:
    which is a series that starts with the numbers 0 and 1 consecutively 
    followed by integers determined by the sum of the two previous integers.

    As demonstrated here: [0, 1, 1, 2, 3, 5, 8, 13, ...]
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)




def lucas(n):
    """
    This function takes n as an argument and returns the lucas value for it
    based on what the lucas series is:
    Which is a series that starts with the numbers 2 and 1 consecutively 
    followed by integers determined by the sum of the two previous integers.

    As demonstrated here: [2, 1, 3, 4, 7, 11, 18, 29, ...]
    """
    if n == 0:
      return 2
    elif n == 1:
      return 1
    else:
      return lucas(n-1)+lucas(n-2)



def sum_series(n,x=0,y=1):
    """
    This function takes 3 arguments:
    the first is a requied argument, which must be passed when the function is called ---> n (number)
    the second and third are optional arguments..
    if I choose to keep them as is  ---> the function will return a number from the fibonacci series
    but if I choose to change them into 2 and 1 consecutively --->  the function will return a number from the lucas series
    same goes if I choose to change them to any other number ---> the function will return a number from a different series
    """
    if n==0:
      return x
    elif n==1:
      return y
    else:
      return sum_series(n-1, x=x, y=y) + sum_series(n-2, x=x, y=y)