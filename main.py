class Horse:
    """Класс лошади"""
    x_distance = None       # пройденный путь.
    sound = None            # звук, который издаёт лошадь.

    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'

    def run(self, dx):
        """Метод увеличивает x_distance на dx, где dx - изменение дистанции"""
        if not isinstance(dx, (int, float)):
            raise TypeError("Операнд dx должен иметь тип 'int' или 'float'")
        self.x_distance += dx

class Eagle:
    """Класс орла"""
    y_distance = None       # высота полёта
    sound = None            # звук, который издаёт орёл

    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'   # звук, который издаёт орёл

    def fly(self, dy):
        """Метод увеличивает y_distance на dy, где dy - изменение дистанции"""
        if not isinstance(dy, (int, float)):
            raise TypeError("Операнд dy должен иметь тип 'int' или 'float'")
        self.y_distance += dy

class Pegasus(Horse, Eagle):
    """Класс Пегаса"""
    def __init__(self):
        """Метод инициализирует дочерний класс Pegasus
        и вызывает инициализаторы базовых классов родителей в порядке наследования"""
        Horse.__init__(self)
        Eagle.__init__(self)

    def move(self, dx, dy):     # где dx и dy изменения дистанции
        """Метод запускает наследованные методы run и fly соответственно"""
        if not isinstance(dx, (int, float)):
            raise TypeError("Операнд dx должен иметь тип 'int' или 'float'")
        if not isinstance(dy, (int, float)):
            raise TypeError("Операнд dy должен иметь тип 'int' или 'float'")
        self.run(dx)
        self.fly(dy)



    def get_pos(self):
        """Метод возвращает текущее положение пегаса в виде кортежа - (x_distance, y_distance)
        в том же порядке."""
        return self.x_distance, self.y_distance

    def voice(self):
        """Метод печатает значение унаследованного атрибута sound"""
        print(self.sound)


# Пример работы программы:
p1 = Pegasus()
print(Pegasus.mro())
print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
