largest = None
smallest = None
while True :
    num = input('Enter a number: ')
    if num == 'done' :
        break
    print(num)
    try:
        notnum = float(num)
    except:
        print('Invalid Input')
        continue
    if smallest is None:
        smallest = notnum
    if notnum > largest :
        largest = notnum
    elif notnum < smallest :
        smallest = notnum

def done(largest, smallest) :
    print('Maximum is: ', largest)
    print('Minimum is: ', smallest)

done(largest, smallest)