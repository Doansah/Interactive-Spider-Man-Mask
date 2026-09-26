# Interactive Miles-Morales-MASK

I have Lego Miles Morales MASK in my dorm room. I also have an esp32, and some basic electronic peripherals. Lets write some code, to make some magic. 

Functionality: 

The Eyes of Miles Morales Mask Should Light Up Based on: 

-> Motion Sensing
-> Audio: ("Hey Miles!")


### Parts Required: 

1 X ESP32 Development Board
1 X ESP32 Development Board
2 X RGB LEDs
1 X HC-SR501 PIR Motion Sensor
1 X Micro USB Cable



### Things I should know about: 
1) Deep-sleep mode 

import machine

# check if the device woke from a deep sleep
if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    print('woke from a deep sleep')

# put the device to sleep for 10 seconds
machine.deepsleep(10000)

2)  
