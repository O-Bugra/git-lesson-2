number = input("Write the number :")

if number.isdigit() and int(number)>0 :
    sum = sum([int(i)**len(number) for i in number])
    
    if int(number) == sum:
        print(" {} is an armstrong number".format(number))
    else :
        print(" {} is not an armstrong number".format(number))
  
else :
   print("It is an invalid entry. Don't use non-numeric, float or negatice values!")







#number = int(input("Write the number :"))
#print(number)
#if type(number) != int or number < 0 :
#    print("It is an invalid entry. Don't use non-numeric, float or negatice values!")
#
#elif sum([int(i) ** len(number) for i in number]) == number :
#    C
#    
#else :
#    print(" {} is not a armstrong number".format(number))
