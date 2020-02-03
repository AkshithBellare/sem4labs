class Fraction:
    
    #constructor
    def __init__(self, numerator, denominator): 
        self.numerator = numerator
        self.denominator = denominator
   
    #gives string representation
    def __str__(self):
        return str(self.numerator) + '/' + str(self.denominator)

    #calculates gcd
    def greatCD(self,num1,num2):
        if num1 > num2:
            return self.greatCD(num2,num1)
        if num1 == 0:
            return num2
        return self.greatCD(num1%num2,num1)

    #overloading *
    def __add__(self,other):
        den = self.denominator * other.denominator
        num = self.numerator * other.denominator + self.denominator * other.numerator       
        g = self.greatCD(den,num)
        return Fraction(num//g,den//g)

    #overloading *
    def __mul__(self,other):
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator
        g = self.greatCD(den,num)
        return Fraction(num//g,den//g)
    
    #overloading =
    def __eq__(self,other):
        num1Reduced = self.greatCD(self.numerator,self.denominator)
        num1 = self.numerator // num1Reduced
        den1 = self.denominator // num1Reduced
        num2Reduced = self.greatCD(other.numerator,other.denominator)
        num2 = other.numerator // num2Reduced
        den2 = other.denominator // num2Reduced
        if num1 == num2 and den1 == den2:
            return "Equal"    
        else:
            return "Unequal"

    def multiply(self,other):
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator
        g =self.greatCD(num,den)
        return Fraction(num//g,den//g)

    def inverse(self):
        return Fraction(self.denominator,self.numerator)

    def equal(self,other):
        num1gcd = self.greatCD(self.numerator,self.denominator)
        num2gcd = self.greatCD(other.numerator,other.denominator)
        num1 = self.numerator // num1gcd
        den1 = self.denominator //num1gcd
        num2 = other.numerator // num2gcd
        den2 = other.denominator // num2gcd
        if num1 == num2 and den1 == den2:
            return "Equal"
        return "Unequal"
 
    def add(self,other):
        den = self.denominator * other.denominator
        num = self.numerator * other.denominator + self.denominator * other.numerator
        return Fraction(num,den)

def main():
    f1 = Fraction(144,48)
    f2 = Fraction(12,4)
    print(f1.equal(f2))

if __name__ == "__main__":
    main()