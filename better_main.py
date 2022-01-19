import math

def p0(k):

    return k**3-3*k**2+3*k-1

def p1(k):

    return -10*k**3+10*k**2-3*k

def p2(k):

    return 9*k**3+9*k**2

def p0d(k):
    return 3*k**2-6*k+3

def p1d(k):
    return -30*k**2+10*k-3

def p2d(k):
    return 27*k**2+18*k



# Computations:

n = 100

g0 = [0,1]
g1a = [0,1]
g1b = [0,1]

for k in range(2,n):

    g0.append(-sum([p*a for p,a in zip([p1(k-1),p2(k-2)],g0[-3:][::-1])])/p0(k))
    g1b.append(-sum([p*b for p,b in zip([p1(k-1),p2(k-2)],g1b[-3:][::-1])])/p0(k))
    g1a.append(-sum([p*a for p,a in zip([p1d(k-1),p2d(k-2)],g0[-3:][::-1])])/p0d(k))

answer1 = sum([a*(1/18)**i for i,a in enumerate(g0)])
answer2 = math.log(1/18)*sum([a*(1/18)**i for i,a in enumerate(g0)]) + sum([b*(1/18)**i for i,b in enumerate(g1b)])

print(f"""
F0 ANSWER: {answer1}
F1 ANSWER: {answer2}
""")

