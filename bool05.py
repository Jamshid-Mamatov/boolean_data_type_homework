def main(a):
    """
    check the following statement "The variable "a" is an odd number"
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    x=a%2
    return x==1
print(main(2),main(1))