from customtkinter import *
from alarm_controller import AlarmController
from spotify_controller import SpotifyController
import spotify_creds

WORK_TIME = 30*60
SHORT_BREAK_TIME = 5*60
LONG_BREAK_TIME = 15
CLIENT_ID = spotify_creds.CLIENT_ID
CLIENT_SECRET = spotify_creds.CLIENT_SECRET
REDIRECT_URI = "http://localhost:8888/callback"
PLAYLIST_URI = "spotify:playlist:37i9dQZF1DWZeKCadgRdKQ"

ALARME = 'alarm_sound.mp3'


class InterfacePomodoro:
    def __init__(self):
        self.alarm = AlarmController(ALARME)
        self.spotify_controller = SpotifyController(
            CLIENT_ID, 
            CLIENT_SECRET, 
            REDIRECT_URI, 
            PLAYLIST_URI)
        self.session = self.spotify_controller.authenticator()
        

        self.app = CTk(fg_color='#e04032')
        self.app.geometry()
        self.app.geometry('600x600')
        self.app.title('Pomofy')
        self.font_pomodoro = CTkFont(family='Trebuchet MS', weight='bold')

        self.frame = CTkFrame(master=self.app, fg_color='#ff5f4c', corner_radius=20)
        self.frame.place(relx=0.5, rely=0.55, anchor='center')

        #Total time
        self.total_time = 0

        self.total_time_label = CTkLabel(self.app,
                                         text=f'Study total time: {self.total_time} min.',
                                         text_color='white',
                                         font=(self.font_pomodoro, 25))
        self.total_time_label.place(relx=0.5, rely=0.35, anchor='center')
        
        # Temporizador
        self.timer_label = CTkLabel(self.frame, 
                       text='00:00', 
                       text_color='white', 
                       font=(self.font_pomodoro, 
                             75))
        self.timer_label.pack(pady=15, padx=50)

        # Botões
        self.start_button = CTkButton(master=self.frame, 
                         text='START', 
                         fg_color='white', 
                         hover_color='#e0e0e0',
                         text_color='#ff5f4c', 
                         font=(self.font_pomodoro, 20),
                         command=self.start_timer)
        self.start_button.pack(pady=5, padx=25)

        self.pause_button = CTkButton(master=self.frame,
                                text='PAUSE', 
                                fg_color='white', 
                                hover_color='#e0e0e0', 
                                text_color='#ff5f4c', 
                                font=(self.font_pomodoro, 20),
                                state=DISABLED,
                                command=self.pause_timer
                                )
        self.pause_button.pack(pady=10, padx=25)

        self.work_time, self.break_time = WORK_TIME, SHORT_BREAK_TIME
        self.is_work_time, self.is_running = True, False

        self.app.mainloop()

    def start_timer(self):
        self.start_button.configure(state=DISABLED)
        self.pause_button.configure(state=NORMAL)
        self.is_running = True
        self.spotify_controller.play_tracks(self.session) # Inicia a música no spotify
        self.update_timer()

    def pause_timer(self):
        self.pause_button.configure(state=DISABLED)
        self.start_button.configure(state=NORMAL)
        self.is_running = False


    def update_timer(self):
        if self.is_running:
            if self.is_work_time:
                self.work_time -= 1
                if self.work_time == 0:
                    self.spotify_controller.pause(self.session) # Pausa a música no spotify
                    self.alarm.play()
                    self.is_work_time = False
                    self.break_time = SHORT_BREAK_TIME
                    self.total_time += WORK_TIME
                    self.total_min = int(self.total_time / 60)
                    self.total_time_label.configure(text=f'Study total time: {self.total_min} min.')
            else:
                self.break_time -= 1
                if self.break_time == 0:
                    self.alarm.play()
                    self.spotify_controller.resume(self.session)
                    self.is_work_time, self.work_time = True, WORK_TIME

            minutes, seconds = divmod(self.work_time if self.is_work_time else self.break_time, 60)
            self.timer_label.configure(text="{:02d}:{:02d}".format(minutes, seconds))
            self.app.after(1000, self.update_timer)
        


InterfacePomodoro()
