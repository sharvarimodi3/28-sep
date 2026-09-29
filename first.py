num = int(input("INPUT NO. : "))
sum = 0
n = num
while (num>0) :
    sum = sum*10+(num%10)
    num//=10
    if (n==sum) :
        print ("NUMBER IS PALINDROME")
