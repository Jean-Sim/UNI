import sympy as sp
import matplotlib.pyplot as plt

r = sp.symbols('r')
p0 = 0.7*10**8
e = sp.E
R = 5
M = (4*sp.pi*(r**2)*p0*e**(-r/R))
IM = sp.integrate(M, r)
val = []
def masse(R_):
     return  -IM.subs(r, 0) + IM.subs(r, R_)
for i in range(101):
    val.append(masse(i))

plt.plot(range(101), val)
plt.xlabel('r in kpc')
plt.ylabel('M in msun')
plt.show()


am, an, a0 = sp.symbols('am an a0')
eq = sp.Eq(an, am * ((am/a0)/sp.sqrt(1+(am/a0)**2)))
eq2 = sp.solve(eq, am)
sp.pprint(eq2[-1])

AM = eq2[-1]
ein_kparsec = 3.0857 * 10**19
m_sun = 1.989 * 10**30
G = 6.67430 * 10**-11
print(float(G))

def a_to_v(a, r):
    return sp.sqrt(r*a)

A0 = 1.2*10**-10
val2 = []
val3 = []

for i in range(100):
    val2.append(a_to_v(AM.subs(a0, A0).subs(an, ((G*masse(i)*m_sun)/(i*ein_kparsec)**2)), i*ein_kparsec)/1000)
    val3.append(a_to_v((G*masse(i)*m_sun)/(i*ein_kparsec)**2, i*ein_kparsec)/1000)

print(val2)
plt.plot(range(100), val2, 'b+')
plt.plot(range(100), val3, 'r+')
plt.xlabel('r in kpc')
plt.ylabel('v in km/s')
plt.show()



