class Student:
  def __init__(self, name):
    self.name = name

  def __str__(self):
    return f'Student object (name {self.name})'

  __repr__ = __str__


s = Student('Michael')
print(s)


class Fib():
  def __init__(self):
    self.a = 0
    self.b = 1

  def __iter__(self):
    return self

  def __next__(self):
    self.a, self.b = self.b, self.a + self.b
    if self.a > 100000:
      raise StopIteration()
    return self.a

  def __getitem__(self, n):
    if isinstance(n, int):
      a, b = 1, 1
      for i in range(n):
        a, b = b, a + b
      return a
    if isinstance(n, slice):
      start = n.start
      stop = n.stop
      if start is None:
        start = 0
      L = []
      a, b = 1, 1
      for i in range(start, stop):
        L.append(a)
        a, b = b, a + b
      return L


# for n in Fib():
#   print(n)
f = Fib()
print(f[1])
print(f[0:5])
