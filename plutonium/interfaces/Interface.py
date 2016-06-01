

class Interface:
    def open(self):
        raise NotImplementedError()

    def close(self):
        raise NotImplementedError()

    def transaction(self):
        raise NotImplementedError()
