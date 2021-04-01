# 2 Vars
# A: print all digits between the vars BUT 5 (anything w/5 in it like 15 55 45...)

# Ask for vars
num_one, num_two = input("Enter 2 numbers:").split()
num_one = int(num_one)
num_two = int(num_two)
# #pint test
# print(num_one, num_two)

#loop through allll the between numbers
for i in range(num_one, num_two+1):
    if not "5" in str(i):
        #if n the str is not 5 then print it :)
        print(i)







