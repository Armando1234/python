class Polynomial:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def __repr__(self):
        return "{}x^2 + {}x + c".format(self.a,self.b,self.c)

    def __add__(self,other):

        adda = self.a + other.a
        addb = self.b + other.b
        addc = self.c + other.c

        #return "{}x^2 + {}x + c".format(adda,addb,addc)
        return Polynomial(adda,addb,addc)

    def __sub__(self,other):

        adda = self.a - other.a
        addb = self.b - other.b
        addc = self.c - other.c

        #return "{}x^2 + {}x + c".format(adda,addb,addc)
        return Polynomial(adda,addb,addc)

    def __getitem__ (self, name):
        if name == 0:
            return self.c
        if name == 1:
            return self.b
        if name == 2:
            return self.a

poly1 = Polynomial(1,5,9)
poly2 = Polynomial(2,4,0) 

print(poly1[2])
print(poly2[1])

poly3 = poly1 - poly2
print(poly3)

