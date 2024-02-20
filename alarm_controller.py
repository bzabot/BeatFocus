from playsound import playsound
from time import sleep

class AlarmController():
    def __init__(self, alarm):
        self.alarm = alarm
        
    def play(self):
        playsound(self.alarm)


if __name__ == '__main__':
    alarm = AlarmController('alarm_sound.mp3')
    alarm.play()