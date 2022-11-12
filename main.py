print("Jenine Paula")
print("o----")
print(" ||||")
print("jenny"*10)
price = 10
price = 20

rating = 4.5
is_boolean = True
print(price)
#exercise
patient_name = "John Smith"
patient_age = 20
is_new = True

#input("What is your name? ")
#print("Hi " + name)
name = input("What is your name? ")
color = input("what is your favorite color? ")
print(name + " likes " + color)
#exercise

weight = input("how many kgs are you?")
weight_lbs = int(weight)*0.45
print(weight_lbs)
course = '''' 
hi am jennny
i wrote you an email
please reach back
thank you
'''
print(course)
peak = "jeniffer"
print(peak[1:-2])
first = "Joe"
last = "Doe"
message = first  + ' [' + last + '] is a coder'
msg = f"{first} [{last}] is a coder "
print(msg)

tutorial = "Python for beginners"
print(len(tutorial))
print(tutorial.upper())
print(tutorial.replace("Python", "java"))
print("java" in tutorial)
x = 10
x += 3
x -= 2
print(x)
#if statements
is_hot = True
is_cold = False
if is_hot:
          print("its a hot day")
          print("enjoy your day")
elif is_cold:
    print("its a cold day")
    print("wear warm clothes")

else:
    print("its a lovely day")
    #exercise
price = 10000000
good_credit = True
if good_credit:
    down_payment = 0.1*price
else:
    down_payment = 0.2*price
print(f"down payment: ${down_payment}")

#while loop
i = 0
while i < 5:
    print(i)
    i += 1
print("done")

secret_number = 8
guess_count = 0
guess_limit =3
while guess_count < guess_limit:
   guess = int(input("Guess: "))
   guess_count += 1
   if guess == secret_number:
       print("You won")
       break
else:
    print("You failed")
prices = [10, 20, 30]
total = 0
for item in prices:
    total += item
    print(f"Total: {total}")

numbers = [5, 8, 15, 2, 12]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
        print(max)

num = [3, 3, 34, 5,5,7]
num.insert(0, 4)
num.pop()#removes last number in a list
num.sort()# arranges numbers in the list
num.reverse() #reverse the numbers
nums = num.copy()
num.append(6)
print(20 in num)#find a number in a list








