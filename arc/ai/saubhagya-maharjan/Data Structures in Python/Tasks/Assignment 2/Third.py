def palindrome_checker(x):
    if x < 0:
        return False
    
    org_num = x
    rev_num = 0

    while x>0:
        digit = x % 10
        rev_num = rev_num * 10 + digit
        x //= 10

    return org_num == rev_num

num = int(input("Enter the number:"))

if palindrome_checker(num):
    print("True - It's a palindrome.")
else:
    print("False - Not a palindrome.")

    