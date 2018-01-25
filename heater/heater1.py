from guizero import *

# Global widgets
sld_setpoint = None
sld_deadband = None
sld_actual = None
sld_high_alarm = None
sld_low_alarm = None
txt_heater_status = Text
txt_alarm_status = Text


def calc(value):
    print(value)
    if sld_actual.value <= sld_setpoint.value - sld_deadband.value:
        txt_heater_status.value = "HEATER ON"
        txt_heater_status.text_color = "red"
    else:
        txt_heater_status.value = "HEATER OFF"
        txt_heater_status.text_color = "blue"

    sld_high_alarm.value = sld_setpoint.value + (2 * sld_deadband.value)
    sld_low_alarm.value = sld_setpoint.value - (2 * sld_deadband.value)

    alarm()


def alarm():
    if sld_actual.value <= sld_low_alarm.value:
        txt_alarm_status.value = "LOW ALARM"
        txt_alarm_status.text_color = "blue"

    elif sld_actual.value >= sld_high_alarm.value:
        txt_alarm_status.value = "HIGH ALARM"
        txt_alarm_status.text_color = "red"

    else:
        txt_alarm_status.value = "NO ALARM"
        txt_alarm_status.text_color = "black"


def main():
    global sld_setpoint, sld_deadband, sld_actual, txt_heater_status
    global sld_high_alarm, sld_low_alarm, txt_alarm_status

    window = App(title="Heater Control", width=500,
                 height=500, layout="grid")

    Text(window, text=" " * 10, grid=[0, 0])
    Text(window, text="\nTemperature Setpoint ", align="right",
         grid=[1, 1])
    sld_setpoint = Slider(window, start=70, end=90, command=calc, grid=[2, 1])

    Text(window, text="\nDeadband ", align="right",
         grid=[1, 3])
    sld_deadband = Slider(window, start=1, end=2, command=calc, grid=[2, 3])
    sld_deadband.value = 1

    Text(window, text="\nTemperature ", align="right",
         grid=[1, 5])
    sld_actual = Slider(window, start=60, end=100, command=calc, grid=[2, 5])

    Text(window, grid=[0, 6])

    txt_heater_status = Text(window, text="HEATER", align="left",
                             grid=[2, 7])

    Text(window, text="\nHigh Temperature Alarm ", align="right",
         grid=[1, 9])
    sld_high_alarm = Slider(window, start=60, end=100, command=calc, grid=[2, 9])
    sld_high_alarm.value = sld_setpoint.value + (2 * sld_deadband.value)

    Text(window, text="\nLow Temperature Alarm", align="right",
         grid=[1, 11])
    sld_low_alarm = Slider(window, start=60, end=100, command=calc, grid=[2, 11])
    sld_low_alarm.value = sld_setpoint.value - (2 * sld_deadband.value)

    Text(window, grid=[0, 12])

    txt_alarm_status = Text(window, text="NO ALARM", align="left", grid=[2, 13])

    window.display()


main()
