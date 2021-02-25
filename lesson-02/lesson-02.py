class Point:
    x = 1
    y = 1

    def __init__(self, x=0, y=0):
        print(f'Вызов функции-конструктора и инициализация объекта {self.__str__()}')
        self.x = x
        self.y = y

    def __del__(self):
        print(f'Объект {self.__str__()} был удален,т.к. нет ни одной активной ссылки на него')

    def set_coords(self, x, y):
        self.a = x
        self.b = y


pt = Point()
pt1 = Point(100)
pt2 = Point(250, -350)

print(pt.__dict__, pt1.__dict__, pt2.__dict__, sep='\n')
