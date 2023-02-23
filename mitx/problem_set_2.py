# Constants
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

# Variables
yearRange = range(1, 13)
monthlyInterestRate = annualInterestRate / len(yearRange)
minimunPayment = unpaidBalance = interest = remainingBalance = 0

for i in yearRange:
    balance  += interest - minimunPayment
    minimunPayment = balance * monthlyPaymentRate
    unpaidBalance = balance - minimunPayment
    interest = (annualInterestRate / len(yearRange) * unpaidBalance)
    remainingBalance = balance - (minimunPayment - interest)
    
    # print(balance, minimunPayment, unpaidBalance, interest)
    # print(f'Month {i} Remaining balance: {remainingBalance}')
        
print('Remaining balance:', round(remainingBalance, 2))