class PolygonShapes:
    #def instance
    __length__ = 0
    __width__ = 0
    __area__ = 0
    __perimeter__ = 0

    #def constructor
    def __init__ (self, new_length = 0, new_width = 0):
        self.__length__ = new_length
        self.__width__ = new_width
        self.__area__ = 0
        self.__perimeter__ = 0

    def get_length(self):
        return self.__length__
    
    def get_width(self):
        return self.__width__
    
    def calculate_area(self):
        self.__area__ = self.__length__ * self.__width__
        return self.__area__
    
    def calculate_perimeter(self):
        self.__perimeter__ = (2*self.__length__) + (2*self.__width__)
        return self.__perimeter__
    
if __name__ == '__main__':
    myPolygon = PolygonShapes()
    myPolygon2 = PolygonShapes(10,10)

    print(myPolygon)
    print(myPolygon2)

    print("Poly 1:", myPolygon.get_length())
    print("Poly 2:", myPolygon2.get_length())

    print("Poly 1 Area:", myPolygon.calculate_area())
    print("Poly 2 Area:", myPolygon2.calculate_area())
    print("Poly 1 Area:", myPolygon.calculate_area())

    print("Poly 1 Perimeter:", myPolygon.calculate_perimeter())
    print("Poly 2 Perimeter:", myPolygon2.calculate_perimeter())

    myPolygon.__length__ = 10
    print(myPolygon.__length__)


