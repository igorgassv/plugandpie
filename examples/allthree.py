import time
import datetime
from plugandpie.drivers.accelerometers.MMA8452Q import MMA8452Q

accelerometer = MMA8452Q()

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)

# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel(channel):
    adc = spi.xfer2([1,(8+channel)<<4,0])
    data = ((adc[1]&3) << 8) + adc[2]
    return data

# Function to convert data to voltage level,
# rounded to specified number of decimal places.
def ConvertVolts(data,places):
    volts = (data * 3.3) / float(1023)
    volts = round(volts,places)
    return volts

# Function to calculate temperature from
# TMP36 data, rounded to specified
# number of decimal places.
def ConvertTemp(data,places):
    temp = ((data * 330)/float(1023))-50
    temp = round(temp,places)
    return temp

# Define sensor channels
light_channel = 0
temp_channel = 1

# Define delay between readings
delay = 0.5

# Indicate new reading in text file
with open("test.txt","a") as out_file:
    out_file.write("-----------------------\n")
    out_file.close

while True:
    # Read the light sensor data
    light_level = ReadChannel(light_channel)
    light_volts = ConvertVolts(light_level,2)

    # Read the temperature sensor data
    temp_level = ReadChannel(temp_channel)
    temp_volts = ConvertVolts(temp_level,2)
    temp = ConvertTemp(temp_level,2)

    #Read accelerometer data
    x,y,z = accelerometer.get_xyz()
    x = accelerometer.get_xyz()[x]
    y = accelerometer.get_xyz()[y]
    z = accelerometer.get_xyz()[z]


    # Print out results
    print("--------------------------------------------")
    print (datetime.datetime.now().strftime("%I:%M:%S"))
    print(("Light : {} ({}V)".format(light_level,light_volts)))
    print(("Temp : {} ({}V) {} deg C".format(temp_level,temp_volts,temp)))
    #print("x: ", x, "y: ", y, "z: ", z)
    print(("x: {:.3f} y: {:.3f} z: {:.3f}".format(x,y,z)))

    # save to file
    with open("test.txt", "a") as out_file:
        out_file.write(datetime.datetime.now().strftime("%I:%M:%S"))
        out_file.write(("\nLight : {}".format(light_level)))
        out_file.write(("\nTemp : {} ({} degC)\n".format(temp_level,temp)))
        #out_file.write("x: " +  x + "y: " + y + "z: " + z)
        out_file.write(("x: {:.2f} y: {:.2f} z: {:.2f}\n\n".format(x,y,z)))
        out_file.close()

    # Wait before repeating loop
    time.sleep(delay)
