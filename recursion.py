def factoria(a):
    if a == 0:
        return 1
    else:
        return(a*factoria(a-1))

print(factoria(5))

#exponent recursion
def expo(num, exp):
    if exp == 0:
        return 1
    else:
        return num * expo(num,exp-1)
    
print(expo(3,5))

#add each digit of number

def adddigits(num):
    if num == 0:
        return 0
    else:
        return num%10 +adddigits(num//10)

print(adddigits(1234))