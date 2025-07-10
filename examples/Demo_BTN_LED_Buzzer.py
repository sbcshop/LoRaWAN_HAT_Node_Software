'''Demo code to Test onboard Buttons, LED, and Buzzer'''

#import required modules
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

BT1 = 23 
BT2 = 24
buzz = 25

GPIO.setup(BT1,  GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BT2,  GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buzz,  GPIO.OUT)

print("Press Any Buttons")

try: 
    while True:
        bt1_val = GPIO.input(BT1)
        bt2_val = GPIO.input(BT2)
        print(f"Button 1: {bt1_val}, Button 2: {bt2_val}")
        
        if bt1_val==0:
            print ("BT1 Pressed")
            GPIO.output(buzz, GPIO.HIGH)
            sleep(0.3)
            
        elif bt2_val==0:
            print ("BT2 Pressed")
            GPIO.output(buzz, GPIO.HIGH)
            sleep(0.3)
        
        else:
            #Turn OFF 
            GPIO.output(buzz, GPIO.LOW)
        
        sleep(0.1)

except KeyboardInterrupt:
    print("Clean up GPIOs")
    GPIO.cleanup()    

            
    


