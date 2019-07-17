# Pomodoro clock v1.0
# author - Jesse Wade
# date - Dec 2018

import tkinter as tk
import datetime

class Countdown(tk.Frame):
    '''A Frame with label to show the time left, an entry to input the seconds to count
    down from, and a start button to start counting down.'''
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.show_widgets()
        self.seconds_left = 0
        self._timer_on = False

    def show_widgets(self):

        self.label.pack()
        self.start.pack()

    def create_widgets(self):

        self.label = tk.Label(self, bg='lightgreen', font=("Verdana", 20), text="Ready to Work?", width=14)
        self.start = tk.Button(self, text="More Work!", command=self.start_button)

    def countdown(self):
        '''Update label based on the time left.'''

        self.label['text'] = str(self.convert_seconds_left_to_time()).lstrip('0:')
        self.label['bg'] = 'lightgreen'

        if self.seconds_left:
            self.seconds_left -= 1
            self._timer_on = self.after(1000, self.countdown)
        else:
            self._timer_on = False
            self.label['text'] = "Take a break!"
            self.label['bg'] = 'indian red'

    def start_button(self):
        '''Start counting down.'''
        
        self.seconds_left = int(1500)   # 1500 seconds = 25 minutes
        self.stop_timer()                           # 2. to prevent having multiple
        self.countdown()                            #    timers at once

    def stop_timer(self):
        '''Stops after schedule from executing.'''
        
        if self._timer_on:
            self.after_cancel(self._timer_on)
            self._timer_on = False

    def convert_seconds_left_to_time(self):

        return datetime.timedelta(seconds=self.seconds_left)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Pomodoro")
    root.resizable(False, False)
    root.attributes("-topmost", True)

    countdown = Countdown(root)
    countdown.pack()

    root.mainloop()
