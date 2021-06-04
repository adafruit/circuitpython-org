# print microcontroller cpu temperature 
import microcontroller # import the microcontroller lib
import time

# infinite loop to keep checking the temperature.
while True:
    # get the current temperature
    current_temp = microcontroller.cpu.temperature 
    # print out the temperature in celsius
    print("Current Temp(Celsius): ",current_temp) 
    # print converted temperature in fahrenheit
    print("Current Temp(Farhenheit):", current_temp * (9/5) + 32) 
    time.sleep(1) # sleep for 1 second