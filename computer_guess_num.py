#!/usr/bin/env python3
import random
def guess(x):
 low=1
 high=x
 feedback=""
 while feedback!="c":
  guess=random.randint(low,high)
  feedback=input(f"Is {guess} number is too high(H), too low(L),correct(C):".lower())
  if feedback=="h":
   high=guess-1
  elif feedback=="l":
   low=guess+1
 print("Yeh, Computer has guessesd  correct number")
guess(10)
