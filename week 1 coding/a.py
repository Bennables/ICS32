#a
a = 10
some_string = " 10"
some_other_string = "20"
hello_world = some_string + " " + some_other_string + " "
print(hello_world+str(a))

#Demo of repeating strings
niners_string = "49ers " * 10
print(niners_string)

#Replaces only the first 5 instances of 49 with Nin
new_niner_string = niners_string.replace("49", "Nin", 5)
print(new_niner_string)

#Replaces only the first 5 instances of 49 with Nin
new_niner_string2 = new_niner_string.replace("Nin", "49", 5)
print(new_niner_string)

some_temp_string = int(some_string) - int(some_other_string)
print(some_temp_string)

def combining_strings():
    a = "Hello"
    #single_space = " "
    b = "World!"
    final_string = a + " " + b
    print(final_string)
    #return final_string

combining_strings()
print(some_string)