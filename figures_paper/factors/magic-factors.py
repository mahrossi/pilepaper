from sys import argv
from math import tanh, exp, pi
from numpy import array

convertcmHertz=2.998e10*2*pi

kb=8.6173324E-5 #eV/K

#eps_zero=14.39964558783 # eV/A

eps_zero=0.0055263494 #e/(A*V)

hbar=6.58211928E-16 #eV.s               

c=2.998e18 #A/s

inp=open(argv[1])

choice=argv[2]

temperature=float(argv[3])

beta=1./(temperature*kb)

#toeangsqt=3.57106
toeangsqt=1

#print beta*hbar

spectrum = [map(float, line.split()) for line in inp]
#print spectrum[0][0], spectrum[0][1]

if choice=='qt':
   new=[[entry[0], entry[1]/(3*c*eps_zero*hbar*entry[0]*convertcmHertz)*tanh(beta*hbar*entry[0]*convertcmHertz/2.) ] for entry in spectrum]
elif choice=='classic':
   new=[[entry[0], entry[1]*beta/(6*c*eps_zero)] for entry in spectrum]

#normalize
new_intens=array([i[1] for i in new])

#print new_intens

#new_intens=new_intens/new_intens.max()

for i,j in zip(new, new_intens):
    print i[0], j/toeangsqt

