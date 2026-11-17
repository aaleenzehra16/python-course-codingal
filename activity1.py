def total_calc(bill_amount,tip_perc):
    tip_paid=(tip_perc/100) *bill_amount
    return tip_paid
print(total_calc(150,20))
