#Вычислим площадь фигуры (area)

class Rectangle:
  def __init__(self, width, heigth):
    self.width = width
    self.heigth = heigth
  def getWidth(self):
    return self.width
  def getHeigth(self):
    return self.heigth
  def getArea(self): # вычисляем площадъ
    return self.width * self.heigth
