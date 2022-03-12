# ----------------------------------------
# Welcome IB Examiner!
# This is the code I used to 
# 1. Calculate the coefficients a_i, b_i and c_i
# 2. Use the coefficients to obtain the F_0(z), F_1(z) and F_2(z) functions
# 3. Use the functions to plot the graphs seen in my EE
# 
# I hope you like it :D
# ----------------------------------------

from cProfile import label
import math

import numpy as np

import matplotlib.pyplot as plt



def prod(l):

            p = 1

            for a in l:

                p *= a

            return p



def diff(p,d):

    return [a*prod([i-j for j in range(0,d)]) for i,a in enumerate(p)][d:]



def ev(p):

    return lambda k : sum([a*k**i for i,a in enumerate(p)])



class Solve2():

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

        return [g0,g1,g2]

    

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

            

        return [g0,g1,g2]

   

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

            

        return [g0,g1,g2]

    def FourthOperator(self):

        p0 = [0, 0, 9, -9]

        p1 = [0, 3, 10, 10]

        p2 = [-1, -3, -3, -1]



        #Compuatations:

        n = 200



        g0 = [1]

        g1 = [0, 0]

        g2 = [0, 1]



        for k in range(1,n):

            if k==1:

                g0.append(-sum([p*a for p,a in zip([ev(diff(p1,1))(k-1),ev(diff(p2,1))(k-2)][0:k],g0[-3:][::-1])])/ev(diff(p0,1))(k))

            else:

                g0.append(-sum([p*a for p,a in zip([ev(p1)(k-1),ev(p2)(k-2)][0:k],g0[-3:][::-1])])/ev(p0)(k))

            

        for k in range(2,n):

            g1.append(-(sum([p*a for p,a in zip([ev(p1)(k-1),ev(p2)(k-2)],g1[-3:][::-1])])+sum([g0[k-i]*ev(diff(p,1))(k-i) for i,p in zip(range(0,min(k+1,5)),[p0,p1,p2])]))/ev(p0)(k))

            g2.append(-sum([p*a for p,a in zip([ev(p1)(k-1),ev(p2)(k-2)][0:k],g2[-3:][::-1])])/ev(p0)(k))



        return [g0,g1,g2]



[g0,g1,g2] = Solve2().FirstOperator() 

print(g1)



f0 = lambda z : sum([a*z**i for i,a in enumerate(g0)])

f1 = lambda z : sum([a*z**i for i,a in enumerate(g0)])*np.log(z) + sum([a*z**i for i,a in enumerate(g1)])

f2 = lambda z : sum([a*z**i for i,a in enumerate(g0)])*(np.log(z))**2/2 + sum([a*z**i for i,a in enumerate(g1)])*np.log(z) + sum([a*z**i for i,a in enumerate(g2)])



F = lambda z : [3*math.pi**2 * f0(z) + 0*f1(z) - 6 * f2(z), 6*math.pi*f1(z)]




xs = np.linspace(0,1/9,200)



#plt.plot(1/xs,f0(xs))

#plt.plot(1/xs,f1(xs))

#plt.plot(1/xs,f2(xs))



plt.plot(xs,F(xs)[0], label="Real part")
plt.axvline(x=1/9, color="red", linestyle='--', label="z=1/9")
plt.plot(xs,-F(xs)[1], linestyle=":" ,label="Imaginary part")
plt.legend(loc="upper left")
plt.xlabel("z")
plt.ylabel("F(z)")
plt.savefig('graph.png')

plt.show()


