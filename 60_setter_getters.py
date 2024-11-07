
class Concept:
    def __init__(self, iden):
        self._iden = iden
    def reveal(self):
        print(f"Identity is {self._iden}")
    
    @property
    def time_value(self):
        return 10*self._iden

    @time_value.setter
    def time_value(self, new_iden):
        self._iden = new_iden/10



ob = Concept(20)
ob.time_value = 50
print(ob.time_value)
ob.time_value()

class MyClass:
  def __init__(self, value):
      self._value = value
    
  def show(self):
    print(f"Value is {self._value}")
    
  @property
  def ten_value(self):
      return 10* self._value
    
  @ten_value.setter
  def ten_value(self, new_value):
      self._value = new_value/10

obj = MyClass(10)
obj.ten_value = 67
print(obj.ten_value)
obj.show()