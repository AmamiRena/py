from math import floor
from progress_b.prog_class import prog
import time

class progBar(prog):
    def __init__(self,iterations,track_time=True,width=30,bar_char='█',stream=2,title='',monitor=False,update_interval=None):
        prog.__init__(self,iterations,track_time,stream,title,monitor,update_interval)
        self.bar_width=width
        self._adjust_width()
        self.bar_char=bar_char
        self.last_progress=0
        self._print_labels()
        self._print_progress_bar(0)
        if monitor:
            try:
                self.process.cpu_percent()
                self.process.memory_percent()
            except AttributeError:
                self.process.get_cpu_percent()
                self.process.get_memory_percent()
        if self.item_id:
            self._print_item_id()
    
    def _adjust_width(self):
        if self.bar_width>self.max_iter:
            self.bar_width=int(self.max_iter)
    
    def _print_labels(self):
        self._stream_out('0% {} 100%\n'.format(' '*(self.bar_width-6)))
        self._stream_flush()

    def _print_progress_bar(self,progress):
        remaining=self.bar_width-progress
        self._stream_out('[{}{}]'.format(self.bar_char*int(progress),' '*int(remaining)))
        self._stream_flush()
    
    def _print(self,force_flush=False):
        progress=floor(self._calc_percent()/100*self.bar_width)
        if self.update_interval:
            do_update=time.time()-self.last_time>=self.update_interval
        elif force_flush:
            do_update=True
        else:
            do_update=progress>self.last_progress
        
        if do_update and self.active:
            self._stream_out('\r')
            self._print_progress_bar(progress)
            if self.track:
                self._print_eta()
            if self.item_id:
                self._print_item_id()
        self.last_progress=progress