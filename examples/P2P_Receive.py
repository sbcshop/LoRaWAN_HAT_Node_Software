# P2P Receive Demo code 
'''
    In P2P device default is in Tx mode to save Power,
    P2P LoRa RX configurable duration value is from 1 to 65533 ms.
    
    For example,
    You can set 30000 ms and so the device will listen and wait for LoRa P2P Packets for 30 seconds.
    Automatically disable RX mode and switch to TX mode after the timeout.
    If the device did not receive any packets within the time period, then the callback after timeout is +EVT:RXP2P RECEIVE TIMEOUT.
    
    Specific functionality for =>
    65535 -> listen to P2P LoRa packets without a timeout, but stops when P2P LoRa packet is received and automatically switch to TX mode again.
    65534 -> continuous listen to P2P LoRa packets without any timeout and without moving to Tx mode.
    0     -> It disables LoRa P2P RX mode and switches to TX mode.
'''
import serial
import time

# UART setup
baudrate = 115200 #default baudrate of Rainy UHF module
port = '/dev/ttyS0' # use for RPi 4 and previous version
#port = '/dev/ttyAMA0' # uncomment to use with  RPi 5

ser = serial.Serial(port, baudrate=baudrate, timeout=1)

rx_mode = 1  # Track receive mode

def send_command(command):
    ser.write((command + '\r\n').encode())
    time.sleep(0.5)
    return ser.readline()

def activate_p2p_receive():
    # Listen to P2P LoRa packets without timeout, switch back to TX after receiving
    res = send_command('AT+PRECV=65535')
    print("[INFO] Entered P2P Receive Mode")
    print("Waiting for incoming data...")

def parse_received_data(response):
    global rx_mode
    try:
        if isinstance(response, bytes):
            response = response.decode('utf-8', 'ignore').strip()
            print(f"[UART] {response}")

        if "+EVT:RXP2P" in response:
            parts = response.strip().split(":")
            if len(parts) >= 4:
                rssi = parts[2]
                data_value = parts[-1]
                print("Received Data Payload:", data_value)
                print("RSSI:", rssi, "dBm")

                # After receiving, reset receive mode
                rx_mode = 0
                time.sleep(1)

    except Exception as e:
        print("Parsing error:", e)

# Initial setup
print("Initializing P2P Receive...")
activate_p2p_receive()

# Main loop
try:
    while True:
        if ser.in_waiting:
            response = ser.readline()
            parse_received_data(response)

        if rx_mode == 0:
            activate_p2p_receive()
            rx_mode = 1
            print("[INFO] Re-entered RX mode...")

        time.sleep(0.2)

except KeyboardInterrupt:
    print("Exiting...")
    ser.close()

