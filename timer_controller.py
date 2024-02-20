import time

class TimerController():
    def __init__(self, focus_time, pause_time):
        self.focus_time = focus_time
        self.pause_time = pause_time

        
    def countdown_timer(self, state):
        if state == 'foco':
            timer = self.focus_time
        elif state == 'pausa':
            timer = self.pause_time
        #print(f'Iniciando tempo de {state}...')
        for i in range(timer, 0, -1):
            sec = i % 60
            min = int(i/60)
            #print(f"{min:02}:{sec:02}")
            time.sleep(1)
        #print(f'Fim do tempo de {state}.')
        return(f"{min:02}:{sec:02}")


if __name__ == '__main__':
    timer = TimerController(10, 5)
    timer.countdown_timer('pausa')