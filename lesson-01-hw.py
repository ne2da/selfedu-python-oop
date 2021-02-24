class Point3D:
    x=1
    y=2
    z=3

pt1 = Point3D()
pt2 = Point3D()
pt3 = Point3D()

print(id(pt1), id(pt2), id(pt3))
print(pt1 == pt2)
print(pt1 is pt3)

print(pt1.__dict__)
print(pt2.__dict__)
print(pt3.__dict__)

print(pt1.x, pt1.y, pt1.z)
print(pt2.x, pt2.y, pt2.z)
print(pt3.x, pt3.y, pt3.z)

print(Point3D.__dict__)

Point3D.y = 228

print(pt1.x, pt1.y, pt1.z)
print(pt2.x, pt2.y, pt2.z)
print(pt3.x, pt3.y, pt3.z)

print(Point3D.__dict__)

del Point3D.z

print(hasattr(pt1, 'z'), hasattr(pt2, 'z'), hasattr(pt3, 'z'))

setattr(pt3, 'x', 111)
Point3D.x = 1984

print(getattr(pt1, 'x'), getattr(pt2, 'x'), getattr(pt3, 'x'), getattr(Point3D, 'x'))