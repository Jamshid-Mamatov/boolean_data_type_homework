from math import trunc
def main(a):
    """
    Check the natural number. Natural numbers are numbers used in counting.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    if trunc(a)==a and a>0:
        result=True
    else:
        result=False
    return result