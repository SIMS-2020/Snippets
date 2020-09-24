import random
import time
import sched

def func():
    elapsedSec = time.time() - initialTime
    error = pow(growthFactorPerSec,  elapsedSec)
    currentValue = initialValue * error
    print("Current value: ", currentValue)
    print("Elapsed time: ", int(elapsedSec))

initialValue = random.randint(0,100)
initialTime = time.time()
growthFactorPerSec = 1.5
cnt = 0

print("Initial value: ", initialValue)

while cnt != 25: 
    func()
    cnt = cnt + 1
    time.sleep(1)






