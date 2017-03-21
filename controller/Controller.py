from devices.Time import *
import numpy
from controller.Global import *
import locale


class Controller:
    locale.setlocale(locale.LC_ALL, 'en_GB.utf8')

    def __init__(self):
        self.timer = Time()

    def new_update_all(self, canvas, run_time):
        canvas.gettags()
        run_time.set_text(self.timer.getTimeString())
        canvas.after(10, self.new_update_all, canvas, run_time)
