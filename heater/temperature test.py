from guizero import *
from gpiozero import CPUTemperature

"""
Display the reading from a DS18B20 temperature sensor
connected on the default GPIO pin #4

The reading will be refreshed automatically in a 
GUI window every 2 seconds
"""

# Global widget
txt_temp_reading = None

# Global constant
temp = None


class TemperatureSensor(CPUTemperature):
    @property
    def closed(self):
        return 0

    @property
    def temperature(self):
        # Open the sensor's data file
        with open(self.sensor_file, 'r') as f:
            # Get the second field on the second line and scale it
            return float(f.readlines()[1].split("=")[1]) / 1000


def refresh():
    # Convert from Celsius to Fahrenheit
    txt_temp_reading.value = round(temp.temperature * 9 / 5 + 32, 2)

    # Refresh every 2 seconds
    txt_temp_reading.after(2, refresh)


def main():
    global temp, txt_temp_reading

    # Absolute path to the file with the temperature probe data
    temp = TemperatureSensor('/sys/bus/w1/devices/28-000008e5904d/w1_slave')

    window = App(title="Temperature", width=250, height=100, layout="grid")

    Text(window, text=" " * 90, size=4, grid=[0, 0])

    txt_temp_reading = Text(window, size=16, grid=[1, 1])

    Text(window, size=4, grid=[1, 2])

    PushButton(window, text="   QUIT   ", command=quit, grid=[1, 3])

    # Start refreshing the display
    txt_temp_reading.after(2, refresh)

    window.display()


main()
