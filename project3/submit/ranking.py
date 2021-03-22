from z3 import *

# l_b -> lisa ranked immediatly ahead of bob
# l_bio -> lisa major in biology

l_b     = Bool('Lisa_Next_Bob')
l_j     = Bool('Lisa_Next_Jim')
l_m     = Bool('Lisa_Next_Mary')
l_bio   = Bool('Lisa_Biology')

b_l = Bool('Bob_Next_Lisa')
b_j = Bool('Bob_Next_Jim')
b_m = Bool('Bob_Next_Mary')
b_bio = Bool('Bob_Biology')

m_l = Bool('Mary_Next_Lisa')
m_j = Bool('Mary_Next_Jim')
m_b = Bool('Mary_Next_Bob')
m_bio = Bool('Mary_Biology')

j_l = Bool('Jim_Next_Lisa')
j_m = Bool('Jim_Next_Mary')
j_b = Bool('Jim_Next_Bob')
j_bio = Bool('Jim_Biology')


s = Solver()

#Lisa is not next to Bob in the ranking
s.add(And(Not(l_b), Not(b_l)))

#Jim is ranked immediately ahead of a biology major
s.add(Or(And(j_l, l_bio), And(j_b, b_bio), And(j_m, m_bio)))

#Bob is ranked immediately ahead of Jim
s.add( b_j )

#One of the women (Lisa and Mary) is a biology major 
s.add(Or(l_bio, m_bio))
s.add( Implies(l_bio, Not(m_bio) )) # Only one
s.add( Implies(m_bio, Not(l_bio)))  # Only one

#One of the women is ranked first
#no one is immediatly ahead of her
s.add(Or(And(Not(b_l), Not(j_l), Not(m_l)), And(Not(b_m), Not(j_m), Not(l_m))))

#i have to be there
s.add(Or(l_b, l_j, l_m, b_l, m_l, j_l))
s.add(Or(b_l, b_j, b_m, l_b, m_b, j_b))
s.add(Or(m_l, m_j, m_b, l_m, b_m, j_m))
s.add(Or(j_l, j_m, j_b, l_j, b_j, m_j))

#i can only be ahead of one person
s.add(Implies(l_b, And(Not(l_j), Not(l_m))))
s.add(Implies(l_j, And(Not(l_b), Not(l_m))))
s.add(Implies(l_m, And(Not(l_b), Not(l_j))))


s.add(Implies(b_l, And(Not(b_j), Not(b_m))))
s.add(Implies(b_j, And(Not(b_l), Not(b_m))))
s.add(Implies(b_m, And(Not(b_l), Not(b_j))))

s.add(Implies(m_l, And(Not(m_j), Not(m_b))))
s.add(Implies(m_j, And(Not(m_l), Not(m_b))))
s.add(Implies(m_b, And(Not(m_l), Not(m_j))))

s.add(Implies(j_l, And(Not(j_m), Not(j_b))))
s.add(Implies(j_m, And(Not(j_l), Not(j_b))))
s.add(Implies(j_b, And(Not(j_m), Not(j_l))))

#if im ahead of one that one cannot be ahead of me
s.add(Implies(l_b, Not(b_l)))
s.add(Implies(l_j, Not(j_l)))
s.add(Implies(l_m, Not(m_l)))

s.add(Implies(b_l, Not(l_b)))
s.add(Implies(b_j, Not(j_b)))
s.add(Implies(b_m, Not(m_b)))

s.add(Implies(m_l, Not(l_m)))
s.add(Implies(m_j, Not(j_m)))
s.add(Implies(m_b, Not(b_m)))

s.add(Implies(j_l, Not(l_j)))
s.add(Implies(j_m, Not(m_j)))
s.add(Implies(j_b, Not(b_j)))

print(s.check())
print(s.model())

print("1- Mary \n2- Bob\n3- Jim \n4- Lisa Biology major ")
