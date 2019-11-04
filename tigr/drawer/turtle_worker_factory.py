from tigr.drawer.abstract_worker_factory import AbstractWorkerFactory
from tigr.drawer.turtle_worker import TurtleWorker


class TurtleWorkerFactory(AbstractWorkerFactory):

    def create_worker(self):
        return TurtleWorker()
