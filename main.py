import math

def prod(l):
            p = 1
            for a in l:
                p *= a
            return p

def diff(p,d):
    return [a*prod([i-j for j in range(0,d)]) for i,a in enumerate(p)][d:]

def ev(p):
    return lambda k : sum([a*k**i for i,a in enumerate(p)])


class Solve():
    def __init__(self, z):
        self.z = z
    def FirstOperator(self):
        p0 = [-1,3,-3,1]
        p1 = [0,-3,10,-10]
        p2 = [0,0,9,9]

        

        # Computations:

        n = 100

        g0 = [0,1]
        g1 = [0,0]
        g2 = [0,0]

        for k in range(2,n):
            g0.append(-sum([p*a for p,a in zip([ev(p1)(k-1),ev(p2)(k-2)],g0[-3:][::-1])])/ev(p0)(k))
            g1.append(-(sum([p*a for p,a in zip([ev(p1)(k-1),ev(p2)(k-2)],g1[-3:][::-1])])+sum([g0[k]*ev(diff(p0,1))(k),g0[k-1]*ev(diff(p1,1))(k-1),g0[k-2]*ev(diff(p2,1))(k-2)]))/ev(p0)(k))
            g2.append(-(sum([p*a for p,a in zip([ev(p1)(k-1),ev(p2)(k-2)],g2[-3:][::-1])])+sum([g1[k]*ev(diff(p0,1))(k),g1[k-1]*ev(diff(p1,1))(k-1),g1[k-2]*ev(diff(p2,1))(k-2)])+sum([g0[k]*ev(diff(p0,2))(k),g0[k-1]*ev(diff(p1,2))(k-1),g0[k-2]*ev(diff(p2,2))(k-2)])/2)/ev(p0)(k))

        answer1 = sum([a*(1/18)**i for i,a in enumerate(g0)])
        answer2 = math.log(1/18)*sum([a*(1/18)**i for i,a in enumerate(g0)]) + sum([b*(1/18)**i for i,b in enumerate(g1)])
        answer3 = (math.log(1/18)**2)/2*sum([a*(1/18)**i for i,a in enumerate(g0)]) + math.log(1/18)*sum([b*(1/18)**i for i,b in enumerate(g1)]) + sum([c*(1/18)**i for i,c in enumerate(g2)])

        return [answer1, answer2, answer3]
    def SecondOperator(self):
        p0 = [0, 0, 8, -8]
        p1 = [0, 54, 225, -207]
        p2 = [-729, 243, 2187, -1701]
        p3 = [0, -2187, 8019, -3645]
        p4 = [0, 0, 6561, 6561]

        # Computations:

        n = 200

        g0 = [1]
        g1 = [0,0]
        g2 = [0,1]

        for k in range(1,n):
            if k==1:
                g0.append(-sum([p*a for p,a in zip([ev(diff(p1,1))(k-1),ev(diff(p2,1))(k-2), ev(diff(p3,1))(k-3), ev(diff(p4,1))(k-4)][0:k],g0[-5:][::-1])])/ev(diff(p0,1))(k))
            else:
                g0.append(-sum([p*a for p,a in zip([ev(p1)(k-1),ev(p2)(k-2), ev(p3)(k-3), ev(p4)(k-4)][0:k],g0[-5:][::-1])])/ev(p0)(k))
            
        for k in range(2,n):
            g1.append(-(sum([p*a for p,a in zip([ev(p1)(k-1),ev(p2)(k-2), ev(p3)(k-3), ev(p4)(k-4)],g1[-5:][::-1])])+sum([g0[k-i]*ev(diff(p,1))(k-i) for i,p in zip(range(0,min(k+1,5)),[p0,p1,p2,p3,p4])]))/ev(p0)(k))
            g2.append(-sum([p*a for p,a in zip([ev(p1)(k-1),ev(p2)(k-2), ev(p3)(k-3), ev(p4)(k-4)][0:k],g2[-5:][::-1])])/ev(p0)(k))
            
        # for k in range(3,n):
        #     g2.append(-sum([p*a for p,a in zip([ev(p1)(k-1),ev(p2)(k-2)],g0[-3:][::-1])])/ev(p0)(k))
        answer1 = sum([a*self.z**i for i,a in enumerate(g0)])
        if (self.z < 0) :
            answer2 = [math.log(-self.z)*sum([a*(self.z)**i for i,a in enumerate(g0)]) + sum([b*(self.z)**i for i,b in enumerate(g1)]),math.pi*sum([a*(self.z)**i for i,a in enumerate(g0)])]
        else:
            answer2 = math.log(self.z)*sum([a*(self.z)**i for i,a in enumerate(g0)]) + sum([b*(self.z)**i for i,b in enumerate(g1)])
        answer3 = sum([a*(self.z)**i for i,a in enumerate(g2)])


        return [answer1, answer2, answer3]
    def ThirdOperator(self):

        p0 = [0, 0, -8, 8]
        p1 = [0, -2, -15, 33]
        p2 = [-1, -5, 3, 51]
        p3 = [0, -3, 19, 35]
        p4 = [0, 0, 9, 9]

        #Computations:

        n = 200

        g0 = [1]
        g1 = [0,0]
        g2 = [0,1]

        for k in range(1,n):
            if k==1:
                g0.append(-sum([p*a for p,a in zip([ev(diff(p1,1))(k-1),ev(diff(p2,1))(k-2), ev(diff(p3,1))(k-3), ev(diff(p4,1))(k-4)][0:k],g0[-5:][::-1])])/ev(diff(p0,1))(k))
            else:
                g0.append(-sum([p*a for p,a in zip([ev(p1)(k-1),ev(p2)(k-2), ev(p3)(k-3), ev(p4)(k-4)][0:k],g0[-5:][::-1])])/ev(p0)(k))
            
        for k in range(2,n):
            g1.append(-(sum([p*a for p,a in zip([ev(p1)(k-1),ev(p2)(k-2), ev(p3)(k-3), ev(p4)(k-4)],g1[-5:][::-1])])+sum([g0[k-i]*ev(diff(p,1))(k-i) for i,p in zip(range(0,min(k+1,5)),[p0,p1,p2,p3,p4])]))/ev(p0)(k))
            g2.append(-sum([p*a for p,a in zip([ev(p1)(k-1),ev(p2)(k-2), ev(p3)(k-3), ev(p4)(k-4)][0:k],g2[-5:][::-1])])/ev(p0)(k))
            
        # for k in range(3,n):
        #     g2.append(-sum([p*a for p,a in zip([ev(p1)(k-1),ev(p2)(k-2)],g0[-3:][::-1])])/ev(p0)(k))
        answer1 = sum([a*self.z**i for i,a in enumerate(g0)])
        if (self.z < 0) :
            answer2 = [math.log(-self.z)*sum([a*(self.z)**i for i,a in enumerate(g0)]) + sum([b*(self.z)**i for i,b in enumerate(g1)]),math.pi*sum([a*(self.z)**i for i,a in enumerate(g0)])]
        else:
            answer2 = math.log(self.z)*sum([a*(self.z)**i for i,a in enumerate(g0)]) + sum([b*(self.z)**i for i,b in enumerate(g1)])
        answer3 = sum([a*(self.z)**i for i,a in enumerate(g2)])


        return [answer1, answer2, answer3]
    def FourthOperator(self):
        p0 = [0, 0, 9, -9]
        p1 = [0, 3, 10, 10]
        p2 = [-1, -3, -3, -1]

        #Compuatations:

        n = 200

        g0 = [0, 1]
        g1 = [0, 0]
        g2 = [0, 0]

        for k in range(1,n):
            if k==1:
                g0.append(-sum([p*a for p,a in zip([ev(diff(p1,1))(k-1),ev(diff(p2,1))(k-2)][0:k],g0[-3:][::-1])])/ev(diff(p0,1))(k))
            else:
                g0.append(-sum([p*a for p,a in zip([ev(p1)(k-1),ev(p2)(k-2)][0:k],g0[-3:][::-1])])/ev(p0)(k))
            
        for k in range(2,n):
            g1.append(-(sum([p*a for p,a in zip([ev(p1)(k-1),ev(p2)(k-2)],g1[-3:][::-1])])+sum([g0[k-i]*ev(diff(p,1))(k-i) for i,p in zip(range(0,min(k+1,5)),[p0,p1,p2])]))/ev(p0)(k))
            g2.append(-sum([p*a for p,a in zip([ev(p1)(k-1),ev(p2)(k-2)][0:k],g2[-3:][::-1])])/ev(p0)(k))

        answer1 = sum([a*self.z**i for i,a in enumerate(g0)])
        if (self.z < 0) :
            answer2 = [math.log(-self.z)*sum([a*(self.z)**i for i,a in enumerate(g0)]) + sum([b*(self.z)**i for i,b in enumerate(g1)]),math.pi*sum([a*(self.z)**i for i,a in enumerate(g0)])]
        else:
            answer2 = math.log(self.z)*sum([a*(self.z)**i for i,a in enumerate(g0)]) + sum([b*(self.z)**i for i,b in enumerate(g1)])
        answer3 = sum([a*(self.z)**i for i,a in enumerate(g2)])


        return [answer1, answer2, answer3]


    
print(f"""

FIRST OPERATOR:
F0 ANSWER: {Solve(1/18).FirstOperator()[0]}
F1 ANSWER: {Solve(1/18).FirstOperator()[1]}
F2 ANSWER: {Solve(1/18).FirstOperator()[2]}

SECOND OPERATOR:
F0 ANSWER: {Solve(8/81).SecondOperator()[0]}
F1 ANSWER: {Solve(8/81).SecondOperator()[1]}
F2 ANSWER: {Solve(8/81).SecondOperator()[2]}

THIRD OPERATOR:
F0 ANSWER: {Solve(-64/81).ThirdOperator()[0]}
F1 ANSWER: {Solve(-64/81).ThirdOperator()[1]}
F2 ANSWER: {Solve(-64/81).ThirdOperator()[2]}

FOURTH OPERATOR:
F0 ANSWER: {Solve(((math.sqrt(41)*3)-9)/16).FourthOperator()[0]}
F1 ANSWER: {Solve(((math.sqrt(41)*3)-9)/16).FourthOperator()[1]}
F2 ANSWER: {Solve(((math.sqrt(41)*3)-9)/16).FourthOperator()[2]}
""")

