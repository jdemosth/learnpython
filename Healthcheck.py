print("Hello! this is a health check app to see if you are healthy or not.")
# 22print("please enter your age ")
while True:
    age = input("please enter your age ")
    if age.isdigit():
        break
    else:
        print("Sorry, age must be a number")

def is_float(text):
    try:
        float(text)
        return True
    except ValueError:
        return False




while True:
    sleep_hours = input("please enter the amount of hours you slept last night ")
    if (is_float(sleep_hours)):
        break
    else:
        print(" Enter valid sleep hours ")




# num_glasses_water = input(
#     "please enter the number of glasses of water you have drank today ")

if float(sleep_hours) >= 8:
     print("Great sleep!")
else:
    print("Try to sleep a bit more ")

# if int(num_glasses_water) >=6:
#     print("Hydration is good!")
# else:
#     print("Drink more water")



