def factoria(a):
    if a == 0:
        return 1
    else:
        return(a*factoria(a-1))

print(factoria(5))