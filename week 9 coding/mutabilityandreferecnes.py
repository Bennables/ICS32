print('--- playing with integers---')
someInt = 1000
print("original someintvalue = " + str(someInt))
print('original reference of someint value: ' + str(id(someInt)))

someInt += 1
print('update someint value: ' + str(someInt))
print('updated referece of someint value: ', str(id(someInt)))

print('--- playing with integers---')
somestr = '1354'
print("original somestr value = " + str(somestr))
print('original reference of somestr value: ' + str(id(somestr)))

somestr ='3125'
print('update somstrt value: ' + str(somestr))
print('updated referece of somestr value: ', str(id(somestr)))

somelist = [100,101,102]
print('original somelis tvalue ,', somelist)
print('orignal referecne of somelist', str(id(somelist)))
print('original referecnhe fo somelies[0]' , str(id(somelist[0])))

somelist.append(4234)

print('appended somelis tvalue ,', somelist)
print('appended referecne of somelist', str(id(somelist)))
print('appended referecnhe fo somelies[0]' , str(id(somelist[0])))


somelist[0]=4334

print('changed somelis tvalue ,', somelist)
print('changed referecne of somelist', str(id(somelist)))
print('changed referecnhe fo somelies[0]' , str(id(somelist[0])))

somelist[0] = 100
print('changed back somelis tvalue ,', somelist)
print('changed back referecne of somelist', str(id(somelist)))
print('changed back referecnhe fo somelies[0]' , str(id(somelist[0])))

anotehrlist = [somelist, somelist]
print('original anotherlist:' , anotehrlist)
print('original anotherLIst:', str(id(anotehrlist)))
print('original anotherLIst[0]:', str(id(anotehrlist[0])))
print('original anotherLIst[1]:', str(id(anotehrlist[1])))

anotehrlist[0] = [1003,524,522]
print('original anotherlist:' , anotehrlist)
print('original anotherLIst:', str(id(anotehrlist)))
print('original anotherLIst[0]:', str(id(anotehrlist[0])))
print('original anotherLIst[1]:', str(id(anotehrlist[1])))


#program will be diff bc changing antoehr arr changes address

