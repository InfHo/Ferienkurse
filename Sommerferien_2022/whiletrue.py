import random
import time

def einsnull():
    text = ""
    for i in range(70):
        text = text + str(random.randint(0,1))
    print(text)

        
while True:
    einsnull()
    time.sleep(0.09)
