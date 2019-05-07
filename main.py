
import math

################################################################################
## Class Quad
################################################################################

class Quad( object ):
    
    def __init__( self, AB=None, DA=None, A=None ):
        """
        Initialize an object of type Quad.
        """
        
        self.__sideAB = AB
        self.__sideDA = DA
        self.__angleA = A
        self.__valid = False
        self.__validate()
      

    def __validate( self ):
        if isinstance(self.__sideAB,(int,float)) and isinstance(self.__sideDA,(int,float)) and self.__sideAB>0 and self.__sideDA>0:
            if self.__angleA in range(1,360):
                self.__valid = True
            else:
                self.__valid = False
            
               
        # Determine if a Quad is valid.
        #
        
    
    
    def __repr__( self ):
        """
        Return a string (the representation of a Quad).
        """

        return self.__str__()

    def __str__( self ): 
        """
        Return a string (the representation of a Quad).
        """
        

        return f"AB = {self.__sideAB} DA = {self.__sideDA} A = {self.__angleA}"
    def is_valid( self ):
        """
        Return a Boolean (is the Quad valid?).
        """
        
        return self.__valid

    def is_rectangle( self ):
        """
        Return a Boolean (is the Qua pass # REPLACEd a rectangle?)
        """
        if self.__sideAB != self.__sideDA:
            return True
        return False
        
       

    def is_rhombus( self ): 
        """
        Return a Boolean (is the Quad a rhombus?)
        """
        if self.__sideAB == self.__sideDA and self.__angleA != 90:
            return True
        return False
       

    def is_square( self ):


        """
        Return a Boolean (is the Quad a square)?
        """
        
        if self.__sideAB == self.__sideDA and self.__angleA == 90:
            return True
        return False

    def sides( self ):
        """
        Return a tuple containing the Quad's four sides.
        """

        return (self.__sideAB,self.__sideDA,self.__sideAB,self.__sideDA)

    
       
    
    def angles( self ):
        """
        Return a tuple containing the Quad's four angles(in degrees) 
        """            
        return (self.__angleA,self.__angleA,self.__angleA)

    def perimeter( self ):
        """
        Return a float representing the Quad's perimeter.
        """

        return 2*(self.__sideAB + self.__sideDA)
    def area( self ):
        """
        Return a float representing the Quad's area. self.__angleA
        """

        return self.__sideAB * self.__sideDA * math.sin(math.radians(self.__angleA))

    def scale( self, factor=1.0 ):
        """
        Scale all four of a Quad's sides by the same factor.
        """
   
        return self.__sideAB*self.__sideDA*factor

a = Quad(20,6,30)

print(a.area())
