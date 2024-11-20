#To check weather the given number is palindrome or not

#case I:

n = int(input("Enter the number: ")) #input = 494, 49, 4, 0

rev = 0 # 4, 49, 494

x = n

while n > 0: #494 > 0, 49 > 0, 4 > 0, 0 !> 0
    rev = (rev*10) + n % 10 # 0 + 4 = 4, 40 + 9 = 49, 490 + 4 = 494
    n //= 10 #n = n // 10, 494 // 10 = 49, 49 // 10 = 4, 4 // 10 = 0

if x == rev:
    print("Therefore", x ,"is a palindrome number.")

else:
    print("Therefore", x ,"is not a palindrome number.")

#case II:

num = input("Write a number: ")

if num == num[::-1]:
    print(num, "is a palindrome number")
else:
    print(num, "is not a palindrome number")
