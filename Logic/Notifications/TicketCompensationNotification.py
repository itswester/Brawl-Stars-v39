from Logic.Notifications.BaseNotification import BaseNotification
from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader


class TicketCompensationNotification:
    def decode(self: Reader):
        BaseNotification.decode(self)
        self.readVint()
        self.readVint()