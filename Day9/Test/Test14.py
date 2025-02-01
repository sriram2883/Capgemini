class Notification:
    def send(self, message):
        pass

class EmailNotification(Notification):
    def send(self, message):
        print("Email notification: "+message)

class SMSNotification(Notification):
    def send(self, message):
        print("SMS notification: "+message)

emailObj = EmailNotification()
emailObj.send("You have an email")
smsObj = SMSNotification()
smsObj.send("You have an SMS")