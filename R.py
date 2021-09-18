import time


t1 = time.time()

x = "reporters malfunction"
x1 = "and this can be prooved"
x2 = "they didn't function at all during the covid pandemic"
x3 = "proof"

print(bool(x))
print(bool(x1))
print(bool(x2))
print(bool(x3))


t2 = time.time()
t = t2 - t1
print("Elapsed time is : ", t, " seconds")
