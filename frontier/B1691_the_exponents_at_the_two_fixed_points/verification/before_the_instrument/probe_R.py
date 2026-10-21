import time; t=time.time()
from series import *
th2, th3, th4 = theta2(), theta3(1), theta3(-1)
den = th2 * th3 * th4
R = [-(th2 * th2) * den.inv(), -(th4 * th4) * den.inv(), (th3 * th3) * S.c(0, 1) * den.inv()]
print('orders', [c.ord() for c in R], 'leads', [c.lead() for c in R])
RR = R[0] * R[0] + R[1] * R[1] + R[2] * R[2]
print('R.R ord', RR.ord(), 'time', round(time.time() - t, 1))
# eta^3 check: den = 2 x prod(1 - x^8n)^3
