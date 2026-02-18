from abc import ABC, abstractmethod
class Noti(ABC):
    @abstractmethod
    def send(self,message:str)->None:
        pass
class Email(Noti):
    def send(self, message:str)->None:
        print("Email sent")
class SMS(Noti):
    def send(self, message:str)->None:
        print("SMS sent")
class NotificationService:

    def __init__(self, notification: Noti):
        self._notification = notification

    def notify_user(self, message: str) -> None:
        self._notification.send(message)

if __name__ == "__main__":
    email_service = NotificationService(Email())
    email_service.notify_user("Your order has been shipped!")

    sms_service = NotificationService(SMS())
    sms_service.notify_user("Your OTP is 123456")