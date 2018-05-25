class Method1(object):
    def __init__(self):
        self.arg = 0

    def add(self,d):
        self.arg += d
        return self
    def minus(self,d):
        self.arg -= d
        return self
