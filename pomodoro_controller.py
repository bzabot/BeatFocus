from alarm_controller import AlarmController
from spotify_controller import SpotifyController
from timer_controller import TimerController

class PomodoroController():
    # Parâmetros
    CLIENT_ID = "6db25025c4cb46ea9617038e59800006"
    CLIENT_SECRET = "43c9dc3d476a481eb7979885b8044b09"
    REDIRECT_URI = "http://localhost:8888/callback"
    PLAYLIST_URI = "spotify:playlist:37i9dQZF1DWZeKCadgRdKQ"

    ALARME = 'alarm_sound.mp3'

    tempo_foco = 5
    tempo_pausa = 5


    def __init__(self):
        self.alarm = AlarmController(PomodoroController.ALARME)
        self.spotify_controller = SpotifyController(
            PomodoroController.CLIENT_ID, 
            PomodoroController.CLIENT_SECRET, 
            PomodoroController.REDIRECT_URI, 
            PomodoroController.PLAYLIST_URI)
        self.session = self.spotify_controller.authenticator()
        self.timer = TimerController(PomodoroController.tempo_foco, PomodoroController.tempo_pausa)


    def start_session(self):
        self.spotify_controller.play_tracks(self.session)
        
        
    def focus_time(self):
        self.timer.countdown_timer('foco')
        self.spotify_controller.pause(self.session)
        self.alarm.play()


    def pause_time(self):
        self.timer.countdown_timer('pausa')
        self.alarm.play()
        self.spotify_controller.resume(self.session)

        


if __name__ == '__main__':
    pomodoro = PomodoroController()
    n_sessions = 5
    pomodoro.start_session()
    for i in range(n_sessions):
        pomodoro.focus_time()
        pomodoro.pause_time()


