# Protected modifier

class protected1:
    def __init__(self):
        self._marks = 44
    def _protectedfuntion(self):
        return "losser"

class doubleprotected1(protected1):
    pass

a = protected1()
b = doubleprotected1()

print(a._marks)
print(a._protectedfuntion())

print(b._marks)
print(b._protectedfuntion())

