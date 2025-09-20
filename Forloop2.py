#for loop 

summation = 0
for i in range(1, 10):
    summation = summation + i  # summation += i
print("Sum is:", summation) # 1+0 = 1, 1+2=3, 3+3=6, 6+4=10, 10+5=15, 15+6=21, 21+7=28, 28+8=36, 36+9=45


print("*********************************")
for k in range( 1, 10, 2):
    print("Number:", k)          # print number 1 to 9 next line  i.e 1,3,5,7,9 -> 1+2=3, 3+2=5, 5+2=7, 7+2=9