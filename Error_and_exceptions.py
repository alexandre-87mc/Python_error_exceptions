#Errors and exceptions

#Try, except and finally
try:
    file1 = open('testFile', 'r')
    file1.write('Testing')
except:
    print('Error with file')
else:
    print("There's no error")

try:
    f = open('testFile2', 'r')
    f.write('Test again')
#finally is executed no mather if there is a error
finally:
    print('Always execute')