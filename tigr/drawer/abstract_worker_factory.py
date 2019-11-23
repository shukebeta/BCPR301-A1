from abc import ABC, abstractmethod

# the factory method interface in factory method pattern: the abstract creator
class AbstractWorkerFactory(ABC):
    """
    Define an interface for creating an object, but let subclasses decide
    which class to instantiate. Factory Method lets a class defer instantiation
    to subclasses
    """
    @abstractmethod
    def create_worker(self):
        pass
