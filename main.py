import os, time, brickpi3

# Initialize the EV3 Brick
BP = brickpi3.BrickPi3()

# Initialize EV3 touch sensor and motors
BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.TOUCH)
touchButton = 0

# Without a delay reading sensor data can cause an error
time.sleep(0.5)

# Quite loop when CTRL+C is pressed
try:

    # Create a loop to react to buttons
    while True:

        # Get touch sensor status
        touchButton = BP.get_sensor(BP.PORT_1)
            
        # If the touch sensor is pressed
        if touchButton:

            # Power functions motors and lights can be powered using motor code
            BP.set_motor_power(BP.PORT_A, 100)
            BP.set_motor_power(BP.PORT_B, 100)
        
        # If the touch sensor is released
        else:

            # Power functions motors and lights can be powered using motor code
            BP.set_motor_power(BP.PORT_A, 0)
            BP.set_motor_power(BP.PORT_B, 0)

        # Loop delay
        time.sleep(0.1)

# Result of CTRL+C
except KeyboardInterrupt:
    
    # Unconfigure the sensors
    BP.reset_all() 