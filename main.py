import math

p0 = [0, 0, 8, -8]
p1 = [0, 54, 225, -207]
p2 = [-729, 243, 2187, -1701]
p3 = [0, 2187, 8019, -3645]
p4 = [0, 0, 6561, 6561]

z = 8/81

def prod(l):
    p = 1
    for a in l:
        p *= a
    return p

def diff(p,d):
    return [a*prod([i-j for j in range(0,d)]) for i,a in enumerate(p)][d:]

def ev(p):
    return lambda k : sum([a*k**i for i,a in enumerate(p)])

# Computations:

n = 100

g0 = [0,1,0,0]
g1 = [0,0,0,0]
g2 = [0,1,0,0]

for k in range(2,n):
    g0.append(-sum([p*a for p,a in zip([ev(p1)(k-1),ev(p2)(k-2), ev(p3)(k-3), ev(p4)(k-4)],g0[-3:][::-1])])/ev(p0)(k))
    g1.append(-(sum([p*a for p,a in zip([ev(p1)(k-1),ev(p2)(k-2)],g1[-3:][::-1])])+sum([g0[k]*ev(diff(p0,1))(k),g0[k-1]*ev(diff(p1,1))(k-1),g0[k-2]*ev(diff(p2,1))(k-2)]))/ev(p0)(k))
    #g2.append(-(sum([p*a for p,a in zip([ev(p1)(k-1),ev(p2)(k-2)],g2[-3:][::-1])])+sum([g1[k]*ev(diff(p0,1))(k),g1[k-1]*ev(diff(p1,1))(k-1),g1[k-2]*ev(diff(p2,1))(k-2)])+sum([g0[k]*ev(diff(p0,2))(k),g0[k-1]*ev(diff(p1,2))(k-1),g0[k-2]*ev(diff(p2,2))(k-2)])/2)/ev(p0)(k))
for k in range(3,n):
    g2.append(-sum([p*a for p,a in zip([ev(p1)(k-1),ev(p2)(k-2)],g0[-3:][::-1])])/ev(p0)(k))
answer1 = sum([a*(z)**i for i,a in enumerate(g0)])
answer2 = math.log(z)*sum([a*(z)**i for i,a in enumerate(g0)]) + sum([b*(z)**i for i,b in enumerate(g1)])
#answer3 = (math.log(z)**2)/2*sum([a*(z)**i for i,a in enumerate(g0)]) + math.log(z)*sum([b*(z)**i for i,b in enumerate(g1)]) + sum([c*(z)**i for i,c in enumerate(g2)])
answer3 = sum([a*(z)**i for i,a in enumerate(g2)])
print(f"""
F0 ANSWER: {answer1}
F1 ANSWER: {answer2}
F2 ANSWER: {answer3}
""")