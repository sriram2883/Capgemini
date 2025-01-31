from abc import ABC, abstractmethod

class Mail(ABC):
    @abstractmethod
    def send(self)->None:
        pass

class Gmail(Mail):
    def send(self):
        print("Sending Gmail")

class Yahoo(Mail):
    def send(self):
        print("Sending Yahoo")

class Outlook(Mail):
    def send(self):
        print("Sending Outlook")

g = Gmail()
g.send()
y = Yahoo()
y.send()
o = Outlook()
o.send()
