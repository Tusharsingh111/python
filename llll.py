
i=10
a=[]
while i>0:
    print("enter number")
    num=input()
    a.append(num)
    i=i-1
    print("enter a number")
    n=input()
    i=9
    count=0
    while i>=0:
        if n==a[i]:
            print("yes")
            count=count+1
            i=i-1
            if count==0:
                print("no")


"""
if n in a:
    print("yes")
else:
    print("no")
i = 20
a = []
while i>0:
  print("Enter number")
  num = input()
  a.append(num)
  i = i-1
odd = 0
even = 0
zero = 0
positive = 0
negative = 0
i = 19
while i>=0:
  if a[i] == 0:
    zero = zero+1
  elif a[i]>0:
    positive = positive + 1
    if a[i]%2 == 0:
      even = even + 1
    else:
      odd = odd + 1
  else:
    negative = negative + 1
    if a[i]%2 == 0:
      even = even + 1
    else:
      odd = odd + 1
  i = i-1
print( "EVEN :",even,"ODD :",odd,"ZERO :",zero,"POSITIVE :",positive,"NEGA
       """

