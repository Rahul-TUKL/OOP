#******************************************Good Example of Polymorphism*************************************************************
from abc import ABC, abstractmethod
class NotificationService(ABC):
    @abstractmethod
    def send_notification(self, message:str):
        pass

class EmailService(NotificationService): 
    def send_notification(self, message):
        print (f"sending email: {message}")

class MobileService(NotificationService):
    def send_notification(self, message):
        print (f"sending Text Message: {message}")

class Order:
    def __init__(self, notification_service: NotificationService):
        self.notification_service = notification_service

    def create(self):
        # perform order creation logic, e.g. validate order details, check product stock and save to database
        self.notification_service.send_notification("Hi, Your order has been placed and will be with you within 2-5 working days")

order=Order(MobileService())
order.create()
order=Order(EmailService())
order.create()


#************************************************BAD Example***********************************************************************************
# class EmailSender:
#     def send(self, message):
#         print (f"sending email: {message}")

# class Order:
#     def create(self):
#         # perform order creation logic, e.g. validate order details, check product stock and save to database
#         email =EmailSender() #Direct instance
#         email.send("Hi, Your order has been placed and will be with you within 2-5 working days")

# order=Order()
# order.create()