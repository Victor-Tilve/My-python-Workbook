'''
link: https://stackoverflow.com/questions/40269969/cross-thread-update-observer-pattern-non-blocking

New to SO, please forgive any etiquette errors (point out if there are!). I'm working on a script that 
is running on the programs main UI thread. That being said, I need to avoid all blocking calls to ensure 
user can still interact. I do not have access to the UI event loop so any busy loop solutions aren't possible 
in my situation.

I have a simple background thread that is communicating to another app and gathering data, and storing in a 
simple array for consumption. Each time this data is updated I need to use the data to modify the UI (this must
run in main thread). Ideally the background thread would emit a signal each time the data is updated then in 
the main thread a listener would handle this and modify the UI. A busy loop is not an option everything must 
be asyncronous/event based.

I have the data gathering continuossly running in the background using threading.timer(..). However since this runs
in a seperate thread, the UI operations need to be called externally to this.

'''


import threading

class Observable(object):

    def __init__(self):
        self.observers = []

    def register(self, observer):
        if not observer in self.observers:
            self.observers.append(observer)

    def unregister(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def unregister_all(self):
        if self.observers:
             del self.observers[:]

    def update_observers(self, *args, **kwargs):
        for observer in self.observers:
            observer.update(*args, **kwargs)
        thread = threading.Timer(4,self.update_observers).start()

from abc import ABCMeta, abstractmethod

class Observer(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self, *args, **kwargs):
        pass

class myObserver(Observer):  
    def update(self, *args, **kwargs):
        '''update is called in the source thread context'''
        print(str(threading.current_thread()))

observable = Observable()

observer = myObserver()
observable.register(observer)

observable.update_observers('Market Rally', something='Hello World')