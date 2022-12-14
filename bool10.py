from math import sqrt
def main(a):
    """
    Check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    if sqrt(a)==a*a:
        result=True
    else:
        result=False
    return result