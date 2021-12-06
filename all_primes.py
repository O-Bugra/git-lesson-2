def isprime(num):
    if num==0 or num==1 :
        return False
    for n in range(2,int(num**1/2)+1):
        if num%n==0:
            return False
    return True

list = [ ]
limit = int(input("Enter number :"))
for i in range(limit):
    if isprime(i):
        list.append(i)
print(list)
