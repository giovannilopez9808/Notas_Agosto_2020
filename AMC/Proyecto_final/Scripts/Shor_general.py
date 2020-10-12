from qiskit import ClassicalRegister, QuantumRegister, QuantumCircuit, Aer, execute
import Our_Qiskit_Functions as oq
import numpy as np
import math as m
import random
import matplotlib
import matplotlib.pyplot as plt
N = 55
Q = m.ceil( m.log(N,2) )
L = 2**Q
a = int( 2+ (N-3)*random.random() )
r = oq.r_Finder(a,N)
#=================================================
print('N = ',N,'Q = ',Q,'a = ',a,'Searching For: r =',r)
if( oq.Euclids_Alg(a,N) > 1 ):
    print('\na happens to have a factor in common with N: ',oq.Euclids_Alg(a,N))
else:
    q1 = QuantumRegister(Q,name='q1')
    q2 = QuantumRegister(Q,name='q2')
    an = QuantumRegister(Q-1,name='a')
    c1 = ClassicalRegister(Q,name='c1')
    c2 = ClassicalRegister(Q,name='c2')
    qc = QuantumCircuit(q1,q2,an,c1,c2,name='qc')
#----------------------------------------------
    for i in np.arange(Q):
        qc.h(q1[int(i)])
    oq.Mod_Op(Q,qc,q1,q2,an,a,N)
    qc.measure(q2,c2)
    oq.QFT_dgr(qc,q1,Q)
    qc.measure(q1,c1)
    M = oq.Measurement(qc,shots=1,print_M=False,return_M=True)
    S = int(oq.From_Binary(list(list(M.keys())[0][0:Q]),'R'))
    #----------------------------------------------
    print('\nSystem One Measurement:|'+list(M.keys())[0][0:Q]+'>')
    print('\nS = ',S,'L = ',L)
    if( S!= 0):
        r = oq.Evaluate_S(S,L,a,N)
        if( r!=0 ):
            print('\nFound the period r = ',r)
            if( ((r)%2 == 0) and ( a**(int(r/2))%N != int(N-1) )):
                f1 = oq.Euclids_Alg(int(a**(int(r/2))+1),N)
                f2 = oq.Euclids_Alg(int(a**(int(r/2))-1),N)
                print('\nFactors of N: ',int(f1),' ',int(f2))
            else:
                if( (r)%2 != 0 ):
                    print('\nr does not meet criteria for factoring N: r is not even')
                else:   
                    print('\nr does not meet criteria for factoring N: a^(r/2) (mod N) = N-1')
        else:
            print('\nCould not find the period using S, start over')
    else:
        print('\nMeasured S = 0, start over')