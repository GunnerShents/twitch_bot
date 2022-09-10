def find_num(word):
    number = []
    words = word.split()
    for i in words:
        if i.isdecimal():
            number.append(int(i))
    if len(number) == 0:
            number = [6]
            
    return number[0]
            

test = find_num("!dice 20")
print (test)







# def find_nums(word):
#     number = []
#     print (word)
#     if [number.append(int(i)) for i in word.split() if i.isdecimal()]:

#     else:
#         number = [6] 
#     return number[0]




def fizz_buzz(num_one, num_two):
    # find lower number and assign to appropriate variables

    if num_one < num_two:
        start = num_one
        end = num_two
    else:
        start = num_two
        end = num_one

    counter = start # Use to track position starting at the lower number

    # This loop checks if the remainder of counter / 3 or 5 is 0 and prints the
    # appropriate response. It then increments counter by 1 until it reaches the
    # higher number.

    while counter < end + 1:
        if counter % 3 == 0 and counter % 5 != 0:
            print('Fizz')
            counter = counter + 1
        elif counter % 5 == 0 and counter % 3 != 0:
            print('Buzz')
            counter = counter + 1
        elif counter % 3 == 0 and counter % 5 == 0:
            print('FizzBuzz')
            counter = counter + 1
        else:
            print(counter)
            counter = counter + 1



