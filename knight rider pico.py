from machine import Pin
import time                                                                                                              
        
leds = []

for i in range(15,7,-1):
    leds.append(Pin(i, Pin.OUT))
    
sleep_time = 0.15


LED_sequence = [x for x in range(0,8,1)] + [x for x in range(6,0,-1)]

print(LED_sequence)



LED_values = [1,0]

while 1:
    for i in LED_sequence:  
        print(i)
        for value in LED_values: 
            leds[i].value(value) 
            time.sleep(sleep_time)
            
            
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

while True:
    if button.value():
        led.toggle()
        time.sleep(0.5)