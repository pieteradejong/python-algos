from abc import ABC, abstractmethod

class DistanceMetric(ABC):

    @abstractmethod
    def getDistance(self):
        pass

