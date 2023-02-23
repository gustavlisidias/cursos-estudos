balance = 320000
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate / 12.0
lowBound = balance / 12
hiBound = (balance*(1+monthlyInterestRate)**12)/12.0
epsilon = 0.01

newBalance = balance
while abs(newBalance) > epsilon:
    minPay = (lowBound + hiBound) / 2
    newBalance = balance
    for month in range(12):
        monthlyUnpaid = newBalance - minPay
        newBalance = monthlyUnpaid + (monthlyInterestRate * monthlyUnpaid)
    if newBalance > epsilon:
        lowBound = minPay
    elif newBalance < epsilon:
        hiBound = minPay
print ("Lowest Payment: ", round(minPay, 2))