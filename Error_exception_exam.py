#Program try, except and finally
try:
    for i in ['a','b','c']:
        print(i**2)
except:
    print("Can't do it")

#Second case
x=5
y=0
try:
    z = x/y
except ZeroDivisionError:
    print("Can't divid by zero!")
finally:
    print('All done!')

#Third case
def Ask_nm():
    while True:
        try:
            n = int(input('Input an integer: '))
            print('Thank you, your number squared is: ', n**2)
            break
        except:
            print('An error occured! Please try again')
            continue

Ask_nm()