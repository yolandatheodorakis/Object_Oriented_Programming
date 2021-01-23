# File name: Exercise2.10.py
# Author: Yolanda Theodorakis
# Description: Code the alarm clock, use objects.

from datetime import datetime

class AlarmClock:
    # Initializes the states for current time and 
    # alarm hours minutes and seconds
    def __init__ (self):
        self.current_time = datetime.now().time()
        self.alarm_hours = 0
        self.alarm_minutes = 0
        self.alarm_seconds = 0
        self.alarm = []

    # Gets current time
    def get_current_time (self):
        return self.current_time

    # Sets the alarm hours, minutes and seconds
    def set_alarm_hours (self):
        self.alarm_hours = input('Submit the hours for alarm: ')
    def set_alarm_minutes (self):
        self.alarm_minutes = input('Submit the minutes for alarm: ')
    def set_alarm_seconds (self):
        self.alarm_seconds = input('Submit the seconds for alarm: ')

    # Compiles hours, minutes and seconds into alarm
    def set_alarm (self):
        self.alarm = ':'.join([self.alarm_hours, self.alarm_minutes, self.alarm_seconds])

    # Gets the alarm time
    def get_alarm (self):
        return self.alarm
    

def main ():
    # Creates new object
    new_alarm_clock = AlarmClock()

    # Shows current time
    print('Current time:', new_alarm_clock.get_current_time())
    
    # Asks user to set the alarm
    new_alarm_clock.set_alarm_hours()
    new_alarm_clock.set_alarm_minutes()
    new_alarm_clock.set_alarm_seconds()
    new_alarm_clock.set_alarm()

    # Prints the set alarm
    print('Alarm at', new_alarm_clock.get_alarm())

main()
