import math as m
import numpy as np
import math as m
import random
import matplotlib
import matplotlib.pyplot as plt
from qiskit import ClassicalRegister, QuantumRegister, QuantumCircuit, Aer, execute
S_simulator = Aer.backends(name='statevector_simulator')[0]
M_simulator = Aer.backends(name='qasm_simulator')[0]

def Measurement(quantumcircuit, **kwargs):
    '''
    Executes a measurement(s) of a QuantumCircuit object for tidier printing
    Keyword Arguments:
    shots (integer) - number of trials to execute for the measurement(s)
    return_M (Bool) - indictaes whether to return the Dictionary object containng measurement resul
    print_M (Bool) - indictaes whether to print the measurement results
    column (Bool) - prints each state in a vertical column
    '''
    p_M = True
    S=1
    ret = False
    NL = False
    if 'shots' in kwargs:
        S = int(kwargs['shots'])
    if 'return_M' in kwargs:
        ret = kwargs['return_M']
    if 'print_M' in kwargs:
        p_M = kwargs['print_M']
    if 'column' in kwargs:
        NL = kwargs['column']
    M1 = execute(quantumcircuit, M_simulator, shots=S).result().get_counts(quantumcircuit)
    M2 = {}
    k1 = list(M1.keys())
    v1 = list(M1.values())
    for k in range(len(k1)):
        key_list = list(k1[k])
        new_key = ''
        for j in range(len(key_list)):
            new_key = new_key+key_list[len(key_list)-(j+1)]
            M2[new_key] = v1[k]
    if(p_M):
        k2 = list(M2.keys())
        v2 = list(M2.values())
        measurements = ''
        for i in range( len(k2) ):
            m_str = str(v2[i])+'|'
            for j in range(len(k2[i])):
                if( k2[i][j] == '0' ):
                    m_str = m_str+'0'
                if( k2[i][j] == '1' ):
                    m_str = m_str+'1'
                if( k2[i][j] == ' ' ):
                    m_str = m_str+'>|'
                m_str = m_str+'>   '
            if(NL):
                m_str = m_str + '\n'
            measurements = measurements + m_str
        print(measurements)
    if(ret):
        return M2

#<----------------------------------------------------------->
#<------------------Operaciones matematicas------------------>
#<----------------------------------------------------------->

def Binary(N, total, LSB):
    import math as m
    import numpy as np
    '''
    Input:
    N (integer)
    total (integer)
    LSB (string)
    Returns the base-2 binary equivilant of N according to left or right least significant bit notation
    '''
    qubits = int(m.log(total,2))
    b_num = np.zeros(qubits)
    for i in range(qubits):
        if( N/((2)**(qubits-i-1)) >= 1 ):
            if(LSB=='R'):
                b_num[i] = 1
            if(LSB=='L'):
                b_num[int(qubits-(i+1))] = 1
            N = N - 2**(qubits-i-1)
    B = []
    for j in range(len(b_num)):
        B.append(int(b_num[j]))
    return B


def From_Binary(S, LSB):
    '''
    Input:
    S (string or array)
    LSB (string)
    Converts a base-2 binary number to base-10 according to left or right least significant bit notation
    '''
    num = 0
    for i in range(len(S)):
        if(LSB=='R'):
            num = num + int(S[int(0-(i+1))]) * 2**(i)
        if(LSB=='L'):
            num = num + int(S[int(i)]) * 2**(i)
    return num

def X_Transformation(qc, qreg, state):
    '''
    Input:
    qc (QuantumCircuit)
    qreg (QuantumRegister)
    state (array)
    Applies the neccessary X gates to transform 'state' to the state of all 1's
    '''
    for j in range(len(state)):
        if( int(state[j])==0 ):
            qc.x( qreg[int(j)] )

def n_Control_U(qc, control, anc, gates):
    '''
    Input:
    qc (QuantumCircuit)
    control (QuantumRegister)
    anc (QuantumRegister)
    gates (array of the form [[string,QuantumRegister[i]],[],...])
    Performs the list of control gates on the respective target qubits as a higher order N-control operation
    '''
    if( len(gates)!=0 ):
        instructions = []
        active_ancilla = []
        q_unused = []
        n = len(control)
        q = 0
        a = 0
        while( (n > 0) or (len(q_unused)!=0) or (len(active_ancilla)!=0) ):
            if( n > 0 ):
                if( (n-2) >= 0 ):
                    instructions.append( [control[q], control[q+1], anc[a]] )
                    active_ancilla.append(a)
                    a = a + 1
                    q = q + 2
                    n = n - 2
                if( (n-2) == -1 ):
                    q_unused.append( q )
                    n = n - 1
            elif( len(q_unused) != 0 ):
                if(len(active_ancilla)>1):
                    instructions.append( [control[q], anc[active_ancilla[0]], anc[a]] )
                    del active_ancilla[0]
                    del q_unused[0]
                    active_ancilla.append(a)
                    a = a + 1
                else:
                    instructions.append( [control[q], anc[active_ancilla[0]], anc[a]] )
                    del active_ancilla[0]
                    del q_unused[0]
                    c_a = anc[a]
            elif( len(active_ancilla)!=0 ):
                if( len(active_ancilla) > 2 ):
                    instructions.append( [anc[active_ancilla[0]], anc[active_ancilla[1]], anc[a]] )
                    active_ancilla.append(a)
                    del active_ancilla[0]
                    del active_ancilla[0]
                    a = a + 1
                elif( len(active_ancilla)==2):
                    instructions.append([anc[active_ancilla[0]], anc[active_ancilla[1]], anc[a]] )
                    del active_ancilla[0]
                    del active_ancilla[0]
                    c_a = anc[a]
                elif( len(active_ancilla)==1):
                    c_a = anc[active_ancilla[0]]
                    del active_ancilla[0]
        for i in range( len(instructions) ):
            qc.ccx( instructions[i][0], instructions[i][1], instructions[i][2] )
        for j in range(len(gates)):
            control_vec = [ gates[j][0], c_a ]
            for k in range( 1, len(gates[j])):
                control_vec.append( gates[j][k] )
            if( control_vec[0] == 'X' ):
                qc.cx( control_vec[1], control_vec[2] )
            if( control_vec[0] == 'Z' ):
                qc.cz( control_vec[1], control_vec[2] )
            if( control_vec[0] == 'PHASE' ):
                qc.cu1( control_vec[2], control_vec[1], control_vec[3] )
            if( control_vec[0] == 'SWAP' ):
                qc.cswap( control_vec[1], control_vec[2], control_vec[3] )
        for i in range( len(instructions) ):
            qc.ccx( instructions[0-(i+1)][0], instructions[0-(i+1)][1], instructions[0-(i+1)][2] )
   
def QFT(qc, q, qubits, **kwargs):
    '''
    Input:
    qc (QuantumCircuit)
    q (QuantumRegister)
    qubits (integer)
    Keyword Arguments:
    swap (Bool) - Adds SWAP gates after all of the phase gates have been applied
    Assigns all the gate operations for a Quantum Fourier Transformation
    155156
    '''
    R_phis = [0]
    for i in range(2,int(qubits+1)):
        R_phis.append( 2/(2**(i)) * m.pi )
    for j in range(int(qubits)):
        qc.h( q[int(j)] )
        for k in range(int(qubits-(j+1))):
            qc.cu1( R_phis[k+1], q[int(j+k+1)], q[int(j)] )
    if 'swap' in kwargs:
        if(kwargs['swap'] == True):
            for s in range(m.floor(qubits/2.0)):
                qc.swap(q[int(s)],q[int(qubits-1-s)])

def QFT_dgr(qc, q, qubits, **kwargs):
    '''
    Input:
    qc (QuantumCircuit)
    q (QuantumRegister)
    qubits (integer)
    Keyword Arguments:
    swap (Bool) - Adds SWAP gates after all of the phase gates have been applied
    Assigns all the gate operations for a Quantum Fourier Transformation
    '''
    if 'swap' in kwargs:
        if(kwargs['swap'] == True):
            for s in range(m.floor(qubits/2.0)):
                qc.swap( q[int(s)],q[int(qubits-1-s)] )
    R_phis = [0]
    for i in range(2,int(qubits+1)):
        R_phis.append( -2/(2**(i)) * m.pi )
    for j in range(int(qubits)):
        for k in range(int(j)):
            qc.cu1(R_phis[int(j-k)], q[int(qubits-(k+1))], q[int(qubits-(j+1))] )
        qc.h( q[int(qubits-(j+1))] )

def Euclids_Alg(a, b):
#    Computes the greatest common denominator between a and b using Euclid's Algorithm
    if(a>b):
        num1 = a
        num2 = b
    if(b>a):
        num1 = b
        num2 = a
    if(b==a):
        gcd = a
        r_old = 0
    r_new = int( num1%num2 )
    r_old = int( num2 )
    while(r_new!=0):
        r_old = r_new
        r_new = int( num1%num2 )
        num1 = num2
        num2 = r_new
    gcd = r_old
    return gcd

def Mod_Op(Q, qc, q1, q2, anc, a, N):
 #   Applies the Modulo Multiplication operator for Shor's algorithm
    mods = Modulo_f(Q,a,N)
    for j in range( 2**Q ):
        q1_state = Binary( j, 2**Q, 'L' )
        q2_state = Binary( mods[j], 2**Q ,'L' )
        gates = []
        for k in range(Q):
            if(q2_state[k]==1):
                gates.append(['X',q2[int(k)]])
        X_Transformation(qc,q1,q1_state)
        n_Control_U(qc, q1, anc, gates)
        X_Transformation(qc,q1,q1_state)
        
def ConFrac(N, **kwargs):
    '''
    Input:
    N (float)
    Keyword Arguments:
    q2 (QuantumRegister)
    a_max (integer) - the maximum number of iterations to continue approximating
    return_a (Bool) - if True, returns the array a containing the continued fraction information
    Evaluates the non-integer number N as the quantity p/q, where p and q are integers
    '''
    imax = 20
    q=3
    p=2
    r_a = False
    if 'a_max' in kwargs:
        imax = kwargs['a_max']
    if 'return_a' in kwargs:
        r_a = kwargs['return_a']
    a = []
    a.append( m.floor(N) )
    b = N - a[0]
    i = 1
    while((round(b,10)!= 0) and (i < imax) ):
        n = 1.0/b
        a.append( m.floor(n) )
        b = n - a[-1]
        i = i + 1
        #------------------------------
    a_copy = []
    for ia in np.arange(len(a)):
        a_copy.append(a[ia])
    for j in np.arange(len(a)-1):
        if( j == 0 ):
            p = a[-1] * a[-2] + 1
            q = a[-1]
            del a[-1]
            del a[-1]
        else:
            p_new = a[-1] * p + q
            q_new = p
            p = p_new
            q = q_new
            del a[-1]
    if(r_a == True):
        return q,p,a_copy
    else:
        return q,p


def r_Finder(a, N):
#    Exhaustively computes the period r to the modulo power function a^x (mod N)
    value1 = a**1 % N
    r = 1
    value2 = 0
    while( (value1 != value2) or (r >1000) ):
        value2 = a**(int(1+r)) % N
        if( value1 != value2 ):
            r = r + 1
    return r

def Primality(N):
    '''
    Input:
    N (integer)
    Returns True is N is a prime number, otherwise False
    '''
    is_prime = True
    if( (N==1) or (N==2) or (N==3) ):
        is_prime = True
    elif( (N%2==0) or (N%3==0) ):
        is_prime = False
    elif( is_prime==True ):
        p = 5
        while( (p**2 <= N) and (is_prime==True) ):
            if( (N%p==0) or (N%(p+2)==0)):
                is_prime = False
            p = p + 6
    return is_prime



def Evaluate_S(S, L, a, N):
    '''
    Input:
    S (integer)
    L (integer)
    a (integer)
    N (integer)
    Attempts to use the measured state |S> to find the period r
    '''
    Pairs = [[S,L]]
    for s in range(3):
        S_new = int( S - 1 + s)
        for l in range(3):
            L_new = int( L - 1 + l)
            if( ((S_new!=S) or (L_new!=L)) and (S_new!=L_new) ):
                Pairs.append( [S_new,L_new] )
    #---------------------------Try 9 combinations of S and L, plus or minus 1 from S & L
    period = 0
    r_attempts = []
    found_r = False
    while( (found_r==False) and (len(Pairs)!=0) ):
        order=1
        S_o = Pairs[0][0]
        L_o= Pairs[0][1]
        q_old = -1
        q = 999
        while q_old!=q:
            q_old = int(q)
            q,p = ConFrac(S_o/L_o,a_max=order+1)
            new_r = True
            for i in np.arange(len(r_attempts)):
                if( q == r_attempts[i] ):
                    new_r = False
            if(new_r):
                r_attempts.append( int(q) )
                r_bool = Mod_r_Check(a,N,q)
                if( r_bool ):
                    found_r = True
                    q_old = q
                    period = int(q)
            order+=1
        del Pairs[0]
    #---------------------------Try higher multiples of already attempted r values
    r_o = 0
    while( (found_r == False) and (r_o < len(r_attempts)) ):
        k = 2
        r2 = r_attempts[r_o]
        while( k*r2 < N ):
            r_try = int(k*r2)
            new_r = True
            for i2 in np.arange(len(r_attempts)):
                if( r_try == r_attempts[i2] ):
                    new_r = False
            if(new_r):
                r_attempts.append( int(r_try) )
                r_bool = Mod_r_Check(a,N,r_try)
                if( r_bool ):
                    found_r = True
                    k = N
                    period = int(r_try)
            k = k + 1
        r_o = r_o + 1
    #---------------------------If a period is found, try factors of r for smaller periods
    if( found_r == True ):
        Primes = []
        for i in range(2,period):
            if( Primality(int(i)) ):
                Primes.append(int(i))
        if( len(Primes) > 0 ):
            try_smaller = True
            while( try_smaller==True ):
                found_smaller = False
                p2 = 0
                while( (found_smaller==False) and (p2 < len(Primes)) ):
                #print('p2: ',p2)
                #print( 'period: ',period,'',Primes[p2] )
                    try_smaller = False
                    if( period/Primes[p2] == m.floor( period/Primes[p2] ) ):
                        r_bool_2 = Mod_r_Check(a,N,int(period/Primes[p2]))
                        if( r_bool_2 ):
                            period = int(period/Primes[p2])
                            found_smaller = True
                            try_smaller = True
                    p2 = p2 + 1
    return period

def Modulo_f(Q, a, N):
    '''
    Input:
    Q (integer)
    a (integer)
    N (integer)
    Produces an array of all the final modulo N results for the power function a^x (mod N)
    '''
    mods = [1]
    for i in range(1,2**Q):
        if(i==1):
            mods.append(a**i%N)
            num = a**i%N
        if(i>1):
            mods.append((num*a)%N)
            num =(num*a)%N
    return mods


def Mod_r_Check(a, N, r):
    '''
    Input:
    a (integer)
    N (integer)
    r (integer)
    Checks a value of r, returning True or False based on whether it correctly leads to a factor of N
    '''
    v1 = a**(int(2)) % N
    v2 = a**(int(2+r)) % N
    if( (v1 == v2) and (r<N) and (r!=0) ):
        return True
    else:
        return False