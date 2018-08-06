from types import MethodType


class Student():
  __slots__ = ('name', 'age')  # 允许添加的属性


s = Student()
s.name = 'Michael'
print(s.name)


def set_age(self, age):
  self.age = age


s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

s2 = Student()
# s2.set_age(30)


def set_score(self, score):
  self.score = score


Student.set_score = set_score


s.set_score(100)
print(s.score)
