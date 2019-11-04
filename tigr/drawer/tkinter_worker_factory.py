from tigr.drawer.abstract_worker_factory import AbstractWorkerFactory
from tigr.drawer.tkinter_worker import TkinterWorker


class TkInterWorkerFactory(AbstractWorkerFactory):

    def create_worker(self):
        return TkinterWorker()
