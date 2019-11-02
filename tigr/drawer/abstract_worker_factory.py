from abc import ABC, abstractmethod
from tigr.drawer.tkinter_worker import TkinterWorker
from tigr.drawer.turtle_worker import TurtleWorker


class AbstractWorkerFactory(ABC):
    """
    The Abstract Factory interface declares a set of methods that return
    different abstract products. These products are called a family and are
    related by a high-level theme or concept. Products of one family are usually
    able to collaborate among themselves. A family of products may have several
    variants, but the products of one variant are incompatible with products of
    another.
    """
    @abstractmethod
    def create_turtle_worker(self) -> TurtleWorker:
        pass

    @abstractmethod
    def create_tkinter_worker(self) -> TkinterWorker:
        pass
