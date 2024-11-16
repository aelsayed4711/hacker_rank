#------------------------------------------------------------------------------------------------
# URL........: https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true
#
# Description:
#
#-------------------------------------------------------------------------------------------------
def is_leap(year:int) -> bool:
    """
     The year can be evenly divided by 4, is a leap year, unless
     The year can be evenly divided by 100, it is NOT a leap year, unless
     The year is also evenly divisible by 400. Then it is a leap year
    Args:
        year (int): year 
    Returns:
        bool: True when leap year otherwise False
    """
    leap = False
    if (year % 4 == 0):
        if (year % 100 == 0) :
            if (year % 400 == 0):
                leap = True
            else:
                leap = False
        elif (year % 4 == 0):     
            leap = True
    return leap
