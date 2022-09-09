def is_Happy_num(n):
  past = set()
  while n != 1:
        n = sum(int(i)**2 for i in str(n))
        if n in past:
            print("is not a happy number")
        past.add(n)
  print("it is a happy number")
n=int(input("enter a number"))
print("it is a happy number")
