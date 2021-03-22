
from z3 import *

l1 = Bool('l1')
l2 = Bool('l2')
l3 = Bool('l3')

t1 = Bool('t1')
t2 = Bool('t2')
t3 = Bool('t3')

s = Solver()

#Signs
s.add(Or(t1, t2, l2))
s.add( Implies(t1, And(Not(t2),Not(l2) ) )) 
s.add( Implies(t2, And(Not(t1),Not(l2) ) )) 
s.add( Implies(l2, And(Not(t1),Not(t2) ) )) 

#make sure only two tigers
s.add(Or(t1, t2, t3))
s.add(Implies(Not(t1), And(t2, t3) ))
s.add(Implies(Not(t2), And(t1, t2) ))
s.add(Implies(Not(t3), And(t1, t2) ))

#make sure only one lady
s.add( Or(l1,l2,l3) )
s.add(Implies(l1, And( Not(l2), Not(l3) )) )
s.add(Implies(l2, And( Not(l1), Not(l3) )) )
s.add(Implies(l3, And( Not(l1), Not(l2) )) )

#make sure only one in room
s.add(Implies(l1, Not(t1) ))
s.add(Implies(t1, Not(l1)))

s.add(Implies(l2, Not(t2)))
s.add(Implies(t2, Not(l2)))

s.add(Implies(l3, Not(t3)))
s.add(Implies(t3, Not(l3)))


s.add(Not(l1))
print(s.check())


print(" Room1: Lady \n Room2: Tiger \n Room3: Tiger")
