balance = 10000
annualInterestRate = 0.2

def min_payment(balance, annualInterestRate):
    modified_balance = balance
    mInterest = annualInterestRate / 12
    mPmin = balance / 12
    mPmax = (balance * ((1 + mInterest)**12))/12
    mP = (mPmin + mPmax) / 2
    tries = 1
    for m in range(1, 13):
        modified_balance -= mP
        modified_balance += (mInterest * modified_balance)
    while abs(modified_balance) > 0.01:
        print(str(tries))
        tries += 1
        if modified_balance < 0:
            mP = (mP + mPmin) / 2
            modified_balance = balance
        else:
            mP = (mP + mPmax) / 2
            modified_balance = balance
        for m in range(1, 13):
            modified_balance -= mP
            modified_balance += (mInterest * modified_balance)
            if tries > 3000000 and m == 12:
                return 'Balance: ' + str(modified_balance) + '; Lowest Payment: ' + str(mP) + '. mPmin: ' + str(mPmin) + '; mPmax: ' + str(mPmax) + '; ' + str((mP + mPmin) / 2)
    return 'Balance: ' + str(modified_balance) + '; Lowest Payment: ' + str(mP)
