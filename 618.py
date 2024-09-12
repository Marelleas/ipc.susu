n = int(input())
if n==1 or n==2:
    print("True")
else:
     fn = 1
     fprev = 1
     fk=0
     while fk<n:
         fk = fn+fprev
         fn, fprev = fk, fn 
     if n==fk:
         print("True") 
     else:
         print("False")