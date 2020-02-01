import time
import board
import busio
import adafruit_mpu6050

i2c = busio.I2C(board.SCL, board.SDA)
mpu = adafruit_mpu6050.MPU6050(i2c)

# This example is meant to be used with the serial plotter which makes
# it easier to see how the readings change with different settings.
# Make sure to poke and prod the sensor while the demo is running to
# generate some intersting data!

while True:
    # first show some 'normal' readings

    mpu.sleep = False
    mpu.cycle = False

    for count in range(0, 100):
        print(mpu.acceleration)
        time.sleep(0.010)

    # Next, set a slow cycle rate so the effect can be seen clearly.
    mpu.cycle_Rate = adafruit_mpu6050.Rate.CYCLE_5_HZ
    # ensure that we're not sleeping or cycle won't work
    mpu.sleep = False
    # Finally, enable cycle mode
    mpu.cycle = True

    for count in range(0, 100):
        print(mpu.acceleration)
        time.sleep(0.010)

    # Finally enable sleep mode. Note that while we can still fetch
    #  data from the measurement registers, the measurements are not
    #  updated. In sleep mode the accelerometer and gyroscope are
    #  deactivated to save power, so measurements are halted.

    mpu.cycle = False
    mpu.sleep = True

    for count in range(0, 100):
        print(mpu.acceleration)
        time.sleep(0.010)
