# LoRaWAN_HAT_Node_Software

<img src="https://github.com/sbcshop/LoRaWAN_HAT_Node_Software/blob/main/images/feature_banner.png"  width= "" height= "">

Transform your Raspberry Pi into a powerful LoRaWAN Node with our plug-and-play HAT featuring the RAK3172 module and TFT display. This provides a convenient and versatile solution for accelerating your IoT development projects with LoRaWAN networks. You can easily switch onboard module into LoRaWAN Mode for connecting with server platforms like The Things Network (TTN), Chirpstack, Actility, etc. or P2P Mode to implement your own customized long-range LoRa network quickly. Module complies with Classes A, B, and C of the LoRaWAN 1.0.3 specifications.

This Github provides getting started guide for LoRaWAN Raspberry Pi HAT Node.

### Feature:
- HAT compatible with 40 Pin Header of the Raspberry Pi series
- Serial Interface between Raspberry Pi and LoRaWAN module for communication
- 1.14” TFT display for visual interactions with resolution of 240x135 pixels
- Display Appearance: RGB, Colors: 65K/262K
- Having ST7789 display driver using SPI interface
- Easy-to-use AT command set via UART interface
- Type C interface for Standalone access to LPWAN module for configuration
- Two programmable Buttons for Additional control features
- Buzzer to add audio alert in projects

**RAK3172 LoRaWAN Module Specifications:**
- RAK3172 is based on STM32WLE5CCU6 chip
- Complies with Class A, B, & C of LoRaWAN 1.0.3 specifications, ensuring interoperability and compliance with industry standards.
- Module Available with Supported bands: EU433, CN470, IN865, EU868, AU915, US915, KR920, RU864, and AS923-1/2/3/4
- LoRaWAN activation by OTAA/ABP
- LoRa Point-to-Point (P2P) communication to build your own LoRa Network
- Easy-to-use AT command set via UART interface
- Long-range - around 15 km* with optimized antenna
  

### Hardware Overview:
<img src="https://github.com/sbcshop/LoRaWAN_HAT_Node_Software/blob/main/images/pinout.png" width="" height=""> 

### Interfacing Details:
Following GPIO pins consumed when LoRaWAN HAT Node connected on Raspberry Pi,

<img src="https://github.com/sbcshop/LoRaWAN_HAT_Node_Software/blob/main/images/interfacing_details.png" width="662" height="402"> 

## Getting Started with Raspberry Pi LoRaWAN HAT Node 
 - For this connect HAT on Raspberry Pi and set jumper on RAK-Pi side as shown below. Also, make sure to connect suitable Antenna using SMA connector onboard.

   <img src="https://github.com/sbcshop/LoRaWAN_HAT_Node_Software/blob/main/images/lorawan_HAT_Node_withPI.jpeg" width="" height="">

 * Download and setup your Raspberry Pi with OS, you can follow the Getting Started [Link](https://www.raspberrypi.com/documentation/computers/getting-started.html) to perform OS installation.
 * You will have to enable Serial and SPI interface in Raspberry Pi, find instruction [here](https://github.com/sbcshop/Pitalk_4G_HAT_Software/blob/main/Documents/Serial%20Interface%20Enable%20RPi.pdf) 
 * Download complete github to Raspberry Pi,
   ```
   git clone https://github.com/sbcshop/LoRaWAN_HAT_Node_Software.git
   ```
    <img src="https://github.com/sbcshop/Rainy_UHF_HAT_Software/blob/main/images/git_download.jpg" width="490" height="90">

 * Open anyone [example](https://github.com/sbcshop/Rainy_UHF_HAT_Software/tree/main/examples) code in python IDE like IDLE, Thonny, etc. and run

    <img src="https://github.com/sbcshop/Rainy_UHF_HAT_Software/blob/main/images/run_examples.png" width="480" height="288">

    <img src="https://github.com/sbcshop/Rainy_UHF_HAT_Software/blob/main/images/output.png" width="480" height="288">

## RAK3172 Module Standalone 
* You can access RAK3172 module directly. For this hat without Pi and also change jumper selection to USB-RAK side as shown below,
  
  <img src="https://github.com/sbcshop/LoRaWAN_HAT_Node_Software/blob/main/images/hat_node_standalone.png" width="375" height="280">

* Connect device to PC/laptop using Type C. Now you can follow steps mentioned [here](https://github.com/sbcshop/LoRaWAN_Breakout_Software) to use RAK3172 module standalone like breakout for changing configuration or [Firmware update](https://github.com/sbcshop/LoRaWAN_Breakout_Software/blob/main/documents/Firmware%20Update%20Procedure%20with%20WisToolBox.pdf).
  


## Resources
  * [Schematic](https://github.com/sbcshop/LoRaWAN_HAT_Node_Hardware/blob/main/Design%20Data/LORAWAN%20HAT%20NODE%20SCH.pdf)
  * [Hardware Files](https://github.com/sbcshop/LoRaWAN_HAT_Node_Hardware)
  * [Getting Started with Raspberry Pi](https://www.raspberrypi.com/documentation/computers/getting-started.html)
  * [RAK3172 AT Command Reference ](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/at-command-manual/)
  * [CH340 Driver Installation Guide](https://github.com/sbcshop/NFC_Module/blob/main/documents/CH340%20Driver%20installation%20steps.pdf)
    
## Related Products  

  * [LoRaWAN for Raspberry Pi Pico](https://shop.sb-components.co.uk/products/lorawan-for-raspberry-pi-pico)

  * [LoRaWAN RP2040 USB Dongle](https://shop.sb-components.co.uk/products/lorawan-rp2040-usb-dongle)
  
  * [LoRaWAN Breakout Board](https://shop.sb-components.co.uk/products/lorawan-breakout)

  * [LoRaWAN For ESP32](https://shop.sb-components.co.uk/products/lorawan-for-esp32)
  
  * [LoRaWAN Gateway HAT for Raspberry Pi](https://shop.sb-components.co.uk/products/lorawan-gateway-hat)
   

## Product License

This is ***open source*** product. Kindly check LICENSE.md file for more information.

Please contact support@sb-components.co.uk for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=300">
</p>
