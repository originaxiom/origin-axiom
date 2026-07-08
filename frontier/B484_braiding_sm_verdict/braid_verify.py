#!/usr/bin/env python3
"""B484: figure-eight braid on Fibonacci anyons; trace=-3/phi; eigenvalues golden not SM;
density (Freedman-Larsen-Wang) forbids 'braiding = gauge group'."""
import numpy as np
phi=(1+np.sqrt(5))/2
s1=np.diag([np.exp(-4j*np.pi/5),np.exp(3j*np.pi/5)])
F=np.array([[1/phi,1/np.sqrt(phi)],[1/np.sqrt(phi),-1/phi]])
s2=F@s1@F
B=np.linalg.inv(s1)@s2@np.linalg.inv(s1)@s2
print("tr =",np.trace(B).real,"= -3/phi =",-3/phi)
print("eigen-phases(deg):",[round(np.degrees(np.angle(e)),2) for e in np.linalg.eigvals(B)])
print("Fibonacci dims:",[1,1,2,3,5,8,13],"-> SU(2),SU(3),SU(5),SU(8),SU(13); dense=universal=NOT a gauge group")
