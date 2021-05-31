from pyDatalog import pyDatalog

pyDatalog.create_terms("Wife","Spouse","Daughter","Female","Male",'m','j','p', 'P', 'Q', 'R') #introduction of terms to be used

+Wife(m ,j)                                   #defining the relations given in question
+Spouse(j ,m)
+Daughter(p,j)


Female(P) <= ( Wife(P, Q) )                      
Female(P) <= (Daughter(P, Q) )
Male(P)  <= Spouse(P, Q)
Daughter(P,R) <= (Daughter(P, Q) & Wife(R, Q) )


print('Is Pinky a Female?')
print(bool(Female(p)))

print('Is Pinky a male?')
print(bool(Male(p)))

print("List all females.")
print(Female(P))
print("List all males.")
print(Male(P))


print("Is Pinky the daughter of Mary?")
print(bool(Daughter(p , m)))