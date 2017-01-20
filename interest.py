def min_payment(balance, annualInterestRate):
    modified_balance = balance
    mInterest = annualInterestRate / 12
    mPmin = balance / 12
    mPmax = (balance * ((1 + mInterest)**12))/12
    mP = (mPmin + mPmax) / 2
    for m in range(1, 13):
        modified_balance -= mP
        modified_balance += (mInterest * modified_balance)
    while abs(modified_balance) > 0.01:
        if modified_balance < 0:
            mP = (mP + mPmin) / 2
            modified_balance = balance
        else:
            mP = (mP + mPmax) / 2
            modified_balance = balance
        for m in range(1, 13):
            modified_balance -= mP
            modified_balance += (mInterest * modified_balance)
    return 'Balance: ' + str(modified_balance) + '; Lowest Payment: ' + str(mP)
