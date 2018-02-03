#find all numbers in between 2000 and 3200 that are
#divisible by 7 but are not multiples of 5
#print numbers on single line separated by comma

empty_list = []

for i in range(2000, 3201):
    if (i%7 == 0) and (i%5 != 0):
        empty_list.append(str(i))

print(','.join(empty_list))
