class SendData:
    def __init__(self, notif_class):
        self.notif_class = notif_class

    def action(self):
        self.notif_class.notify()