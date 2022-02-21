import plotly.express as px
theAnnualRate = .04
PrincipalA = 550000
termInYears = 30
FirstFiveYearsRate = .03
SecondFiveYearRate = .04
Remainder = .05

#Arrays
DailyBalance = []
DailyInterest = []
DailyPayment = []
FortnightPayment = []
MonthlyPayment = []

DayOfMonthlyPayment = []

def CalculateMonthlyPayment(PrincipalAmount,rate,termInYears):
    a = (rate * PrincipalAmount)
    b = (1 + (rate /12))
    c = -12 * termInYears
    p = a / (12 * (1 - pow(b, c)))
    return p


def ExcelIteration(MonthlyPayment,Term,LoanAmount,FirstFive,SecondFive,Remainder,extraPayments):
    Balance = []
    Principal = []
    Interest = []
    TotalInterest = 0
    NumberOfMonths = Term * 12

    for i in range(int(NumberOfMonths)):
        if(i<=60):
            if(LoanAmount > 0):
                InterestIteration = LoanAmount * FirstFive/12
                PrincipalIteration = MonthlyPayment - InterestIteration
                Interest.append(InterestIteration)
                Principal.append(PrincipalIteration)
                LoanAmount = LoanAmount -PrincipalIteration - extraPayments
                Balance.append(LoanAmount)
                TotalInterest += InterestIteration
        if (i > 60 and i <= 120):
            if (LoanAmount > 0):
                InterestIteration = LoanAmount * SecondFive/ 12
                PrincipalIteration = MonthlyPayment - InterestIteration
                Interest.append(InterestIteration)
                Principal.append(PrincipalIteration)
                LoanAmount = LoanAmount - PrincipalIteration - extraPayments
                Balance.append(LoanAmount)
                TotalInterest += InterestIteration
        if (i > 120):
            if (LoanAmount > 0):
                InterestIteration = LoanAmount * Remainder/ 12
                PrincipalIteration = MonthlyPayment - InterestIteration
                Interest.append(InterestIteration)
                Principal.append(PrincipalIteration)
                LoanAmount = LoanAmount - PrincipalIteration - extraPayments
                Balance.append(LoanAmount)
                TotalInterest += InterestIteration
    return Balance,Principal,Interest,TotalInterest

MonthlyAmount = CalculateMonthlyPayment(PrincipalA,FirstFiveYearsRate,termInYears)
extraRepayment = 2700
#extrar
A=ExcelIteration(MonthlyAmount,termInYears,PrincipalA,FirstFiveYearsRate,SecondFiveYearRate,Remainder,extraRepayment)
print(A[0])

fig = px.bar(y = [A[1],A[2]])
fig.show()

fig2 = px.bar(y = A[0])
fig2.show()

print("MonthlyPayment:", MonthlyAmount)
print("Total Payments per month: ",MonthlyAmount + extraRepayment)
print("Total Interest: ",A[3] )
