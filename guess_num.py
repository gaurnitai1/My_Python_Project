#!/usr/bin/env python3
import random
def guess_num(x):
 random_num=random.randint(1,x)
 guess_num=0
 while guess_num!=random_num:
  guess_num=int(input(f"guess the number between 1 and {x}:"))
  if guess_num<random_num:
   print("sorry ,it is too low")
  elif guess_num>random_num:
   print("sorry,it is too high")
 print(f"Yea!, you have gussed right, the number {random_num}")
guess_num(10)
