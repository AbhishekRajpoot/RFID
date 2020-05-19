from time import sleep
import sys
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()

try:
    while True:
        name = input('Enter Product Name:  ')
        price = input('Enter Product Price:  ')
        print("Hold a tag near the reader")
        reader.write(name)
        reader.write(price)
        sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()
    raise