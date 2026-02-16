from abc import ABC, abstractmethod
class Notification(ABC):
    @abstractmethod
    def send(self,message):
        pass
class Email(Notification):
    def send(self,message):
        print("Email sent")
class Sms(Notification):
    def send(self, message):
        print("SMS sent")
class Push(Notification):
    def send(self, message):
        print("Sent push noti")
def notify(notification: Notification, message:str):
    notification.send(message)
email=Email()
sms=Sms()
pu=Push()
notify(email,"Hello")
notify(sms,"Hai")
notify(pu,"Bye")