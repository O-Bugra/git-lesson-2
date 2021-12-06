number = int(input("Enter a number :"))

if number <= 0 :
    print("Please enter a positive integer.")

elif number == 2 :
    print("2 is a prime number.")

else :
    for i in range(2,number):
        if number % i == 0:
            print("{} is not a prime number".format(number))
            break
    else :
       print("{} is a prime number".format(number))