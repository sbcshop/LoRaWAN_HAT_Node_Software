'''
Code to Get/Set Device EUI, AppEUI (Join EUI), and AppKey
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

# Global variables to hold credentials
DEVEUI_ = ''
APPEUI_ = ''
APPKEY_ = ''


def send_command(command):
    uart.write((command + '\r\n').encode())
    time.sleep(0.2)

def module_response_check():
    global DEVEUI_, APPEUI_, APPKEY_
    timeout = time.time() + 2  # read for 2 seconds max

    while time.time() < timeout:
        if uart.in_waiting:
            response = uart.readline().decode('utf-8', 'ignore').strip()
            if response:
                print(f"Module Response : {response}")

                if response.startswith("AT+DEVEUI="):
                    DEVEUI_ = response.split('=')[1]
                elif response.startswith("AT+APPEUI="):
                    APPEUI_ = response.split('=')[1]
                elif response.startswith("AT+APPKEY="):
                    APPKEY_ = response.split('=')[1]
        else:
            time.sleep(0.1)

def get_IDkey():
    # Get DEVEUI, APPEUI, APPKEY
    send_command('AT+DEVEUI=?')
    module_response_check()

    send_command('AT+APPEUI=?')
    module_response_check()

    send_command('AT+APPKEY=?')
    module_response_check()

    # Print neatly formatted credentials
    print("\n========== LoRaWAN Node Credentials ==========")
    print(f"DEVEUI  : {DEVEUI_}")
    print(f"APPEUI  : {APPEUI_}")
    print(f"APPKEY  : {APPKEY_}")
    print("==============================================")

def set_IDkey(deveui, appeui, appkey):
    send_command(f"AT+DEVEUI={deveui}")
    time.sleep(0.2)

    send_command(f"AT+APPEUI={appeui}")
    time.sleep(0.2)

    send_command(f"AT+APPKEY={appkey}")
    time.sleep(0.2)


# --------- Main Code Execution ---------

send_command('AT')
module_response_check()

# Ensure LoRaWAN mode
send_command('AT+NWM=1')
module_response_check()

# Retrieve and display current credentials
get_IDkey()

# To set new credentials, uncomment and modify:
'''
DEVEUI_ = 'BC1F09FFFE1AF310'    # Replace with your DEVEUI
APPEUI_ = 'BC1F09FFF9153170'    # Replace with your APPEUI
APPKEY_ = 'BC1F09FFFE1AF318AC1F09FFF9153170'  # Replace with your APPKEY

set_IDkey(DEVEUI_, APPEUI_, APPKEY_)
get_IDkey()  # Confirm update
'''


