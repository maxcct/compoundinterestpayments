# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 22:55:53 2017

@author: Max
"""

balance = 5000
annualInterestRate = 0.2

def min_payment(balance, annualInterestRate):
    modified_balance = balance
    mInterest = annualInterestRate / 12
    mPmin = balance / 12
    mPmax = (balance * ((1 + mInterest/100)**12))/12
    mP = (mPmin + mPmax) / 2
    while abs(modified_balance) > 0.1:
        if modified_balance < 0:
            mP = (mP + mPmin) / 2
            modified_balance = balance
        else:
            mP = (mP + mPmax) / 2
            modified_balance = balance
        for m in range(1, 13):
            modified_balance -= mP
            modified_balance += (mInterest * modified_balance) / 100
    return 'Balance: ' + str(modified_balance) + '; Lowest Payment: ' + str(mP)