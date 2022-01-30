from SendData import SendData
from Notification import Notification
from PushNotification import PushNotification


def main():
    sd1 = SendData(Notification())
    sd1.action()

    sd2 = SendData(PushNotification())
    sd2.action()
    

main()