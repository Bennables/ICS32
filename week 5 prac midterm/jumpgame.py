'''*****************************************************************************
Problem 1 Requirements:
Create a function called jump_game that takes a list of positive whole numbers.
Starting at the first index in the array, the integer value at any given index
is the maximum number of spots that you can jump forward within the array.
Return true if you can get to the last index position in the array and false if
you can never reach the final index position in the array.
*****************************************************************************'''
#***************Write Your Solution to Problem 1 below this line****************

# max num spots
def jump_game(list_ints):

    count = list_ints[0]
    cur_max = 0
    max_ind = 0
    i = 0
    while i < len(list_ints)-1:
        cur_max = 0
        ind = 0
        j = list_ints[i+1:i+count+1]
        for b in range(0,len(j)):
            if i + b + j[b] >= i + j[ind]+ind:
                ind = b
                cur_max = i +b+j[b]
        if cur_max == 0:
            return False
        else:
            i = ind + i+1
            count = list_ints[i]
        

    return True


'''
loop thru it

'''

print(jump_game([3,0,0,1,1,2,3]))
print(jump_game([1,1,1,0,1,2,3]))
print(jump_game([3,2,0,1,1,2,3]))
print(jump_game([3,0,0,0,1,2,3]))
print(jump_game([3,0,0,0,1,2,3]))











