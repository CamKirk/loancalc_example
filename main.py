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
def payments_remaining(int_rate,payment,princ):
	return np.ceil(npf.nper(int_rate/12,payment,princ)

def calc_total_interest(int_rate,payment_periods,princ):
	pay_per = np.arange(payment_periods)+1
	return sum(npf.ipmt(int_rate/12,pay_per,payment_periods,princ))

def calc_loan_info(princ,int_rate,payment):
	periods_remaining = payments_remaining(int_rate,payment,princ)
	interest_remaining = calc_total_interest(int_rate,periods_remaining,princ)
	return [periods_remaining, interest_remaining]
