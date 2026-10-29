# 1. Variables and data types
a = 11
b = 11.5
c = "Python"
d = [1, 2, 3]                  # list
e = {"name": "Sathish", "age": 23}  # dict
f = {1, 2, 3}                  # set
g = (10, 20, 30)               # tuple


print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))
print(f, type(f))
print(g, type(g))


# 2. Sales report
sales = [12000, 0, 8500, 15000, -200, 9800]
total = 0


for x in sales:
    if x <= 0:
        print("Skipped invalid value", x)
        continue


    total += x
    print("Added", x, "total", total)


    if total > 30000:
        break


# 3. Check target
if total > 30000:
    print("Target reached. Stopped at", total)
elif total == 30000:
    print("Target reached exactly at", total)
else:
    print("Target not reached")