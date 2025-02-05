def is_prime(n):
   """
   Check if a number is prime.
   """
   if n <= 1:
       return False
   if n==2:
     return True
   if n % 2 == 0:
     return False
   for i in range(3, int(n**0.5) + 1, 2):
     if n % i == 0:
       return False
   return True
 

def is_perfect(n):
  if n <= 1:
    return False
  sum_div=1
  for i in range(2, int(n**0.5) + 1):
    if n%i==0:
      sum_div+=i + n//i
  return sum_div==n

def is_armstrong(n):
  if n < 0:
    return False
  num_str = str(n)
  length = len(num_str)
  return sum(int(digit)**length for digit in num_str) == n

def digit_sum(n):
  """
  Calculate the sum of digits of a number.
  """
  return sum(int(digit) for digit in str(abs(n)))
 
 
  
