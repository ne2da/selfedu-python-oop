class Point:
    """Класс для представления двухмерной точки на плоскости"""
    x = 1
    y = 1


Point.z = 1
print(Point.__doc__)
print(Point.__dict__)

pt = Point()
pt.x = 100
pt.y = 200

print(pt, pt.x, pt.y)

print(hasattr(pt, 'z'))
print(getattr(pt, 'y'))
print(setattr(pt, 'z', 0.5))
print(pt.__dict__)
delattr(pt, 'z')
print(pt.__dict__)

print(isinstance(pt, Point))
