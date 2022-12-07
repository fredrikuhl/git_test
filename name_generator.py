import time

for i in range(0, 10000):
    i = i + i**i
    print(i)
    time.sleep(0)

print("I cant believe you waited this long!")