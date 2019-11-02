from tigr.drawer.abstract_worker_factory import AbstractWorkerFactory
from tigr.drawer.tkinter_worker import TkinterWorker
from tigr.drawer.turtle_worker import TurtleWorker


class ConcreteWorkerFactory(AbstractWorkerFactory):

    def create_turtle_worker(self) -> TurtleWorker:
        return TurtleWorker()

    def create_tkinter_worker(self) -> TkinterWorker:
        return TkinterWorker()
