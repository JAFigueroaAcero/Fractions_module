'''
Module to use fraction operators without calling functions directly

--To operate use 'a |op| b' or 'a |sim' and 'a |dec' to simplificate or convert a fraction --

'''

class Infix:
    def __init__(self, function):
        self.function = function
    def __ror__(self, other):
        return Infix(lambda x, self=self, other=other: self.function(other, x))
    def __or__(self, other):
        return self.function(other)

class Infix_i:
    def __init__(self, function):
        self.function = function
    def __ror__(self, other):
        return self.function(other)

def frac(x,y):
    return [x,y]|sim

def sum_frac(x,y):
    a = x[0]*y[1] + y[0]*x[1]
    b = y[1]*x[1]
    return [a,b]|sim

def res_frac(x,y):
    a = x[0]*y[1] - y[0]*x[1]
    b = y[1]*x[1]
    return [a,b]|sim

def mult_frac(x,y):
    return [x[0]*y[0],x[1]*y[1]]|sim

def div_frac(x,y):
    return [x[0]*y[1],x[1]*y[0]]|sim

def sim_frac(a):
    new_a = [[],[]]
    for m,n in enumerate(a):
        act = n
        new_a[m].append(0 if a[m] == 0 else 1)
        while act != 1:
            v = 2
            while v < act/2 + 1:
                if act % v == 0:
                    new_a[m].append(v)
                    act = act // v 
                    break
                else:
                    v += 1
            else:
                new_a[m].append(act)
                break
    for f in new_a[0][1::]:
        if f in new_a[1]:
            new_a[0].pop(new_a[0].index(f))
            new_a[1].pop(new_a[1].index(f))
    new_am = [1,1]
    for rep,a in enumerate(new_a):
        for n in a:
            new_am[rep] *= n
    return new_am

def dec2frac(a,p):
    x = [int(a*p),p]
    return x|sim

def dec_v(a):
    return a[0]/a[1]

f = Infix(lambda x,y: frac(x,y))       # Do frac
sim = Infix_i(lambda x: sim_frac(x))  # Simplificate frac
s = Infix(lambda x,y: sum_frac(x,y))  # Sum frac
r = Infix(lambda x,y: res_frac(x,y))  # Substract frac
x = Infix(lambda x,y: mult_frac(x,y)) # Multiplicate frac
d = Infix(lambda x,y: div_frac(x,y))  # Divide frac
dec = Infix_i(lambda x: dec_v(x))       # Converts to float
d2f = Infix(lambda x,y: dec2frac(x,y)) # Converts float to frac