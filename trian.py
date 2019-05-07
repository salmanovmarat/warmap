import math

################################################################################
## Class Triangle
################################################################################

class Triangle( object ):
    
    def __init__( self, sideA=0.0, sideB=0.0, sideC=0.0 ):
        """
        Initialize an object of type Triangle.
        """
        
        self.__sideA = sideA
        self.__sideB = sideB
        self.__sideC = sideC
        self.__valid = False

        pass # REPLACE

    def __validate( self ):
        if isinstance(self.__sideA,(int,float)) and isinstance(self.__sideB,(int,float)) and isinstance(self.__sideC,(int,float)):
            if(self.__sideA + self.__sideB)>self.__sideC:
                self.__valid = True
            else:
                self.__valid = False
        #
        # Check the three sides to determine if a Triangle is valid.
        #

     
    
    def __repr__( self ):
        """
        Return a string (the representation of a Triangle).
        """

        return self.__str__()

    def __str__( self ):
        """
        Return a string (the representation of a Triangle).
        """

        return f"{self.__sideA} =sideA {self.__sideB} = sideB {self.__sideC} = sideC"

    def is_valid( self ):
        """
        Return a Boolean (is the Triangle valid?).
        """
        
        return self.__valid

    def is_equilateral( self ):
        """
        Return a Boolean (is the Triangle an equilateral triangle?)
        """
        
        return self.__valid

    def is_isosceles( self ):
        """
        Return a Boolean (is the Triangle an isosceles triangle?)
        """
    
        return self.__valid

    def is_scalene( self ):
        """
        Return a Boolean (is the Triangle a scalene triangle?)
        """
        
        return self.__valid

    def sides( self ):
        """
        Return a tuple containing the Triangle's three sides.
        """
    
        return (self.__sideA,self.__sideB,self.__sideC)
    
    def angles(self):
        """
        Return a tuple containing the Triangle's three angles (in degrees) 
        """
        
        pass # REPLACE

    def perimeter( self ):
        """
        Return a float representing the Triangle's perimeter.
        """

        return (self.__sideA + self.__sideB + self.__sideC)/2
    
    def area( self ):
        """
        Return a float representing the Triangle's area.
        """

        return math.sqrt(self.perimeter()*(self.perimeter()-self.__sideA)*(self.perimeter()-self.__sideB)*(self.perimeter()-self.__sideC))

    def scale( self, factor=1.0 ):
        """
        Scale all three of a Triangle's sides by the same factor.
        """

        pass # REPLACE
     



a = Triangle(4,10,8)
print(a.area())