class Counter:
    k = []

    def __init__(self):
        self.counter = 0

    def __setattr__(self, name, value):
        if name != 'counter':
            if name not in self.k:
                self.counter += 1
                self.k.append(name)
        super().__setattr__(name, value)

    def __delattr__(self, name):
        self.counter -= 1
        self.k.remove(name)
        super().__delattr__(name)
