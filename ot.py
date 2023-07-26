hrs = input("Enter hours:")
rte = input("Enter rate:")

h = float(hrs)
r = float(rte)

if h <= 40:
    print(h * r)
elif h > 40:
    print(40 * r + (h - 40) * 1.5 * r)
