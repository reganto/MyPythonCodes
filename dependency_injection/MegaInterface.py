from abc import ABCMeta, abstractmethod


class MegaInterface(metaclass=ABCMeta):
    @abstractmethod
    def notify(self):
        pass
