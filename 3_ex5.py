sum=0
try:
    while True:
        for i in map(int, input('Please enter a number plus space and number for receiving the sum or enter any other symbol to quit:').split()):
            sum = sum + i
        print(sum)
        #sum = 0
except ValueError:
    print('Not a number entered!')
