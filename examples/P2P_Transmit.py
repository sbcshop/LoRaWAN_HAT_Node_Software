'''Demo P2P Transmit Code '''
import time
import serial
import RPi.GPIO as GPIO

# GPIO setup
GPIO.setmode(GPIO.BCM)
BUTTON1_PIN =23
BUTTON2_PIN = 24
BUZZER_PIN = 25

GPIO.setup(BUTTON1_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON2_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# UART setup
baudrate = 115200 #default baudrate of Rainy UHF module
port = '/dev/ttyS0' # use for RPi 4 and previous version
#port = '/dev/ttyAMA0' # uncomment to use with  RPi 5

ser = serial.Serial(port, baudrate=baudrate, timeout=1)

def send_command(command):
    ser.write((command + '\r\n').encode())
    time.sleep(0.2)
    response = ser.read_all().decode()
    print(f"> {command}")
    print(f"< {response.strip()}")
    if "+EVT:TXP2P" in response:
        print("Transmit Success")
    return response

def p2p_setup_module():
    print("Initializing LoRaWAN HAT...")
    res = send_command('AT')
    #print(res)
    
    res = send_command('AT+NWM=0')       # Set to P2P mode
    #print(res)
    
    res = send_command('AT+PRECV=0')     # Stop any previous receive
    #print(res)
    
    res = send_command('AT+P2P=903000000:7:0:0:14:5')  # US915 P2P settings
    #print(res)

    res = send_command("AT+P2P=?")
    #print(res)
    print("Setup complete.\n")

# Start
p2p_setup_module()

print("Ready! Press Button 1 or 2 to send data.\n")

try:
    while True:
        if GPIO.input(BUTTON2_PIN) == GPIO.LOW:
            print("Button 2 Pressed!")
            GPIO.output(BUZZER_PIN, GPIO.HIGH)
            send_command('AT+PSEND=02')
        elif GPIO.input(BUTTON1_PIN) == GPIO.LOW:
            print("Button 1 Pressed!")
            GPIO.output(BUZZER_PIN, GPIO.HIGH)
            send_command('AT+PSEND=01')
        else:
            GPIO.output(BUZZER_PIN, GPIO.LOW)
        time.sleep(0.5)

except KeyboardInterrupt:
    print("Exiting...")
    GPIO.cleanup()
    ser.close()

