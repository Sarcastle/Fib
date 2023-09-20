response = input('Input number for FIB sequence\n')

if not response.isnumeric():
    print('Please enter a valid number.')
else:
    y = int(response)

    myoutput = ''
    if y > 0:
        myoutput += '0\t'
    if y > 1:
        myoutput += '1\t'
    if y > 2:
        previousNumber1 = 0
        previousNumber2 = 1
        for x in range(2, y):
            currentNumber = previousNumber1 + previousNumber2
            myoutput += f'{currentNumber}\t'
            previousNumber1 = previousNumber2
            previousNumber2 = currentNumber
    print(myoutput)