''' Simple Data Send on TTN Server

To Register Setup and Register Gateway on TTN Server :
https://github.com/sbcshop/LoRaWAN_Gateway_HAT_Software

To create application & register endnode on TTN Server checkout instructions:
https://github.com/sbcshop/LoRaWAN_Breakout_Software/tree/main/lorawan_application_TTN

To get/set LoRaWAN Endnode credentials using code => 
https://github.com/sbcshop/LoRaWAN_HAT_Node_Software/blob/main/examples/lorawan_endnode_config.py
'''


import serial
import time
import RPi.GPIO as GPIO

# ---------- CONFIGURATION and UART setup ----------
baudrate = 115200 #default baudrate of Rainy UHF module
port = '/dev/ttyS0' # use for RPi 4 and previous version
#port = '/dev/ttyAMA0' # uncomment to use with  RPi 5

# Setup Serial
uart = serial.Serial(port, baudrate, timeout=1)


def send_command(command):
    uart.write((command + '\r\n').encode())
    time.sleep(1)
    response = uart.read_all().decode().strip()
    print(f"Response: {response}")
    return response

def check_join_status(timeout=5):
    print("Checking Join Status...")
    send_command('AT+NJS=?')
    start = time.time()
    
    while (time.time() - start) < timeout:
        if uart.in_waiting:
            response = uart.readline().decode().strip()
            print(f"Read: {response}")
            if 'AT+NJS=1' in response:
                print("Already Connected to Network")
                return True
        else:
            print(".", end='', flush=True)
        time.sleep(0.2)

    return False

def join_network():
    attemptCnt = 0
    status = False

    while not status:
        if uart.in_waiting:
            response = uart.readline().decode().strip()
            print(response)
            if '+EVT:JOINED' in response or 'AT+NJS=1' in response:
                print("Connected to Network")
                status = True
                break
        else:
            print(".", end='', flush=True)
            attemptCnt += 1
            if attemptCnt > 20:
                break
        time.sleep(1)

    if not status:
        print("Join Failed! Restart Node")
        while True:
            time.sleep(1)

def send_data(port, data, joined=True):
    data = str(data)
    port = str(port)
    
    if len(data) % 2 != 0:
        data = '0' + data
        
    cmd = f"AT+SEND={port}:{data}"
    print(f"Sending: {cmd}")
    
    if joined:
        send_command(cmd)
        print("Data Sent!")
    else:
        print("Not connected to network.")

# --------- Main Program ---------
status = check_join_status()

if not status:
    print("\nNOT JOINED! Trying to connect...")
    send_command('AT+NWM=1')
    send_command('AT+JOIN=1:0:10:8')
    join_network()
    status = True

while True:
    print("\nUploading Data...")
    send_data(1, "34", joined=status)
    time.sleep(20)






