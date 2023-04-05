def fibonacci(n):
    """Return the nth value in the fibonacci series.
    Note:
        the Fibonacci sequence is a sequence in which each number is the sum of the two preceding ones
    
        Return the nth value in the fibonacci series.
    
    Args:
        n (int): The position of the desired number in the fibonacci series.
        
    Returns:
        int: The nth value in the fibonacci series.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
    
a=fibonacci(7)
print(a)



def lucas(n):
    """Return the nth value in the lucas numbers.
    
    Args:
        n (int): The position of the desired number in the lucas numbers.
        
    Returns:
        int: The nth value in the lucas numbers.
    """
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)




def sum_series(n, first=0, second=1):
   
    """
    Prints the nth element in a series.

    Parameters:
    n (int): The index of the element to be printed.
    first (int): The first element in the series. Default value is 0.
    second (int): The second element in the series. Default value is 1.

    Returns:
    int: The nth element in the series.
    """
    if first == 0 and second == 1:
        return fibonacci(n)

    elif first == 2 and second == 1:
        return lucas(n)

    else:
        if n == 0:
            return first
        elif n == 1:
            return second
        else:
            return sum_series(n-1, first, second) + sum_series(n-2, first, second)