import hashlib
import os
x = -1
y = -1
for cordX in range(0, 10):
    x += 1
    y = -1
    for cordY in range(0, 10):
        y += 1
        cord = str(x) + "x" + str(y)
        cordHash = hashlib.md5(cord.encode("utf")).hexdigest()
        command = "mv " + cordHash + ".jpg " + cord + ".jpg"
        print(command)
        os.system(command)
