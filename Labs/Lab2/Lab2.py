class Polynomial:
    def __init__(self, coefs =[]):
        self.coefs = coefs
        if coefs == None:
            return "P(x) = 0"

    def __repr__(self):
        poly_String = " "
        if self.coefs == 0:
            return str(0)
        for i in range(len(self.coefs)-1, 0, -1):
            if self.coefs[i] != 0:
                poly_String+=  str(self.coefs[i]) + "x"
                if i > 1:
                    poly_String+= "^" + str(i) + "+"
        if len(self.coefs) != 1:
            poly_String+="+"
        poly_String+= str(self.coefs[0])
        return poly_String
      

    def eval(self, val):
        if self.coefs == 0:
            return 0
        res = self.coefs[0]
        for i in range(1, len(self.coefs)):
            res+= self.coefs[i] * val ** i
        return res

    def addition(self,rhs):
        add_list = []
        if len(self.coefs) > len(rhs.coefs):
            for i in range(len(self.coefs)):
                if i > len(rhs.coefs):
                    add_list.append(self.coefs[i])
                else:
                    add_list.append(self.coefs[i] + rhs.coefs)
        else:
            for i in range(len(rhs.coefs)):
                if i > len(self.coefs):
                    add_list.append(rhs.coefs[i])
                else:
                    add_list.append(rhs.coefs[i] + self.coefs)
        return  Polynomial(add_list)

   


    def multiplication(self,rhs):
        new_lst =[0] * (len(self.coefs) + len(rhs.coefs))
        for i in range(len(self.coefs)):
            for i in range(len(rhs.coefs)):
                new_lst[i+j] = self.coefs * rhs.coefs
        return Polynomial(self.new_lst)

    def polySequence(self, start, end, step=1):
        for i in range(start, end, step):
            yield self.eval(i)

coef =[1,2]
p =Polynomial(coef)
for val in p.polySequence(0,5):
    print(val)


