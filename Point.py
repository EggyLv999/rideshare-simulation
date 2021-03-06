#shamelessly looted from http://www1.cmc.edu/pages/faculty/alee/python/points.py
import math
from math import radians, cos, sin, asin, sqrt



#*********************************************************
# class Point starts here
#
class Point(object):
    # Documentation string
    """
       The class Point represents a 2D point
       Class attributes:    points
       Instance attributes: x
                            y
    """

    # Class attributes:
    #
    # To access a class attribute, use dot notation, e.g., Point.points
    # as is done in __init__ below.
    # Note: there is only one copy of a class attribute
    #       whereas there is a copy of instance attribute in
    #       every Point instance.
    points = []

    # Constructors
    def __init__(self):
        self.x = 0
        self.y = 0
        Point.points.append(self)

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        Point.points.append(self)

    # toString method in Java for those who are familiar with Java
    # Generating a string representation of a Point object
    def __str__(self):
       return '(%g, %g)' % (self.x, self.y)
       # return '(' + str(self.x) + ', ' + str(self.y) + ')'

    # Special names methods. . .
    # With this method defined, we can use + to add two point objects
    # as in p1 + p2 which is equivalent to p1.__add__(p2)
    # See http://docs.python.org/ref/specialnames.html for others
    # Also see http://docs.python.org/reference/ for general language
    # reference
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # With this method defined, two point objects can be compared with
    # >, <, and ==.
    def __cmp__(self, other):
        # compare them using the x values first
        if self.x > other.x: return 1
        if self.x < other.x: return -1

        # x values are the same... check y values
        if self.y > other.y: return 1
        if self.y < other.y: return -1

        # y values are the same too. . . it's a tie
        return 0

    def list(self):
        return [self.x,self.y]

    # Other general methods
    def distance_from_origin(elf):
        return math.sqrt(elf.x * elf.x + elf.y * elf.y)

    def distance(self, other):
        dx = math.fabs(self.x - other.x)
        dy = math.fabs(self.y - other.y)
        return math.sqrt(dx * dx + dy * dy)

    def isIn1stQuad(self):
        return (self.x > 0) and (self.y > 0)

    def haversine(self, other):
        """
        Calculate the great circle distance between two points 
        on the earth (specified in decimal degrees)
        """
        # convert decimal degrees to radians 
        lon1, lat1, lon2, lat2 = map(radians, [self.y, self.x, other.y, other.x])

        # haversine formula 
        dlon = lon2 - lon1 
        dlat = lat2 - lat1 
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a)) 
        r = 6371 # Radius of earth in kilometers. Use 3956 for miles
        return c * r
        
    # class Point ends here
    #*********************************************************