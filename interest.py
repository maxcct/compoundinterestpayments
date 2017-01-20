def calc_year(balance, mP, monthly_interest):
    for month in range(1, 13):
        balance -= mP
        balance += (monthly_interest * balance)
    return balance

def min_payment(balance, annual_interest_rate):
    monthly_interest = annual_interest_rate / 12
    mPmin = balance / 12
    mPmax = (balance * ((1 + monthly_interest)**12))/12
    mP = (mPmin + mPmax) / 2
    modified_balance = calc_year(balance, mP, monthly_interest)
    while abs(modified_balance) > 0.01:
        if modified_balance < 0:
            mPmax = (mP + mPmax) / 2
            mP = (mPmin + mPmax) / 2
        else:
            mPmin = (mP + mPmin) / 2
            mP = (mPmin + mPmax) / 2
        modified_balance = calc_year(balance, mP, monthly_interest)
    return 'Lowest Payment: ' + str((round(mP, 2)))
