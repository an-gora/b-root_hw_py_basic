def mult(a, n):
   if a<0 or n<0:
      raise ValueError('This function works only with postive integers')
   else:
      if a == 0:
         return 0
      elif a == 1:
         return n
      else:
         return n + mult(a-1, n)

print(mult(3, 100))