from customtkinter import *
from time import sleep

app = CTk(fg_color='#e04032')
app.geometry('600x600')
app.title('Pomofy')

font_pomodoro = CTkFont(family='Trebuchet MS', weight='bold')

frame = CTkFrame(master=app, fg_color='#ff5f4c', corner_radius=20)
frame.place(relx=0.5, rely=0.55, anchor='center')

timer_label = CTkLabel(frame, 
                       text='00:00', 
                       text_color='white', 
                       font=(font_pomodoro, 
                             40))
timer_label.pack(pady=15, padx=50)

WORK_TIME = 25 
SHORT_BREAK_TIME = 5 
LONG_BREAK_TIME = 15 

global is_work_time, is_running
is_work_time, is_running = True, False
work_time, break_time = WORK_TIME, SHORT_BREAK_TIME

def start_timer():
    start_button.configure(state=DISABLED)
    pause_button.configure(state=NORMAL)
    is_running = True
    update_timer()

def pause_timer():
    start_button.configure(state=NORMAL)
    pause_button.configure(state=DISABLED)
    is_running = False

def update_timer():
    is_running = True
    if is_running:
        print('a')
        if is_work_time:
            work_time -= 1
            if work_time == 0:
                is_work_time = False
                break_time = SHORT_BREAK_TIME
            else:
                break_time -= 1
                if break_time == 0:
                    is_work_time, work_time = True, WORK_TIME
        print('a')

        sec = work_time % 60
        min = int(work_time/60)
        timer_label.configure(text="{:02d}:{:02d}".format(min, sec))
        print("{:02d}:{:02d}".format(min, sec))
        app.after(1, update_timer)
        



start_button = CTkButton(master=frame, 
                         text='Start', 
                         fg_color='white', 
                         hover_color='#e0e0e0',
                         text_color='#ff5f4c', 
                         font=(font_pomodoro, 10),
                         command=start_timer)
start_button.pack(pady=5, padx=25)

pause_button = CTkButton(master=frame,
                         text='Pause', 
                         fg_color='white', 
                         hover_color='#e0e0e0', 
                         text_color='#ff5f4c', 
                         font=(font_pomodoro, 10),
                         state=DISABLED,
                         )
pause_button.pack(pady=10, padx=25)

#work_time, break_time = WORK_TIME, BREAK_TIME









app.mainloop()