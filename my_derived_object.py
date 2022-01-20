import trial
class MyDerivedObject(MyObject):
    def __init__(self):
        super().__init__()
    def __str__(self):
        return self.greeting
