import calendar
print()

def addtwo(a, b):
    added = a + b
    return a


x = addtwo(2, 7)
print(x)
print()


def stuff():
    print('Hello')
    return
    print('World')


stuff()
print()


def func(x):
    print(x)


func(10)
func(20)
print()

x = 'banana'
y = max(x)
z = y * 2
print(x)
print()


def thing():
    print('Hello')


print('There')
print()


def computepay(h, r):
    if h > 40:
        pay = 1.5 * r * (h - 40) + (40 * r)
    else:
        pay = h * r
    return pay


print()

# next two lines originally had user input
hrs = 45
rphs = 10.50

hr = float(hrs)
rph = float(rphs)

p = computepay(hr, rph)
print('Pay', p)
print()


# calendar is imported for this at the top of page
yy = 1976
mm = 4
print(calendar.month(yy, mm))


# Python for loop is far less complex than a Java for loop!
for x in range(0, 10, 1):
    print(x, 'Sorry babu')
