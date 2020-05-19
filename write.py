from time import sleep
import sys
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()

try:
    while True: # for multiple tags
        name = input("Enter Product Name:")
        print("Hold a tag near the reader")
        reader.write(name)
        sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()
    raise
