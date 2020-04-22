import numpy_financial as npf
import numpy as np

current = np.ceil(npf.nper(0.0375/12,-400,10182))
potential = np.ceil(npf.nper(0.022/12,-400,10182))

print(current, potential)

pay_per = np.arange(current)+1
ipmts_curr = npf.ipmt(0.0375/12, pay_per, current, 10182)
impts_pot = npf.ipmt(0.022/12,pay_per, current,10182)
print(ipmts_curr,sum(ipmts_curr))
print(impts_pot,sum(impts_pot))

