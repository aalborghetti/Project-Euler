"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

num , div= 600851475143, 1

while num != 1:
  div += 1
  while (num % div) == 0:
    num /= div

print(div)