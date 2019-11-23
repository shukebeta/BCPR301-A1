from tigr.drawer.abstract_worker_factory import AbstractWorkerFactory
from tigr.drawer.tkinter_worker import TkinterWorker

# one of the concrete creators
class TkInterWorkerFactory(AbstractWorkerFactory):

    def create_worker(self):
        return TkinterWorker()
