from abc import ABC
from contextlib import contextmanager


class DatabaseInterface(ABC):

    @contextmanager
    def get_session(self):
        try:
            yield self.session
        except:
            self.session
            raise
        finally:
            self.session.close()