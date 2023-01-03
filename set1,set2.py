#1
n=int (input ('enter a number:'))
for i in range(1,11):print(n,'x',i,'=',n*i)

#2a
n,s=int (input ('enter a number:')),0
for i in range(i,nt1):
        s=i**(-1)
print('sum:',s)

#2b
n,s=int (input('enter a number:')),0
for i in range(1,n+1):
	st=i/(i*i)
print('sum:',s)

#2c
n,s=int (input('enter a number:')),0
for i in range(1,n+t1):
	st=i**0.5
print('sum:',s)

#3
for i in range(1,51):
    if i%15==0:print('FizzBuzz')
    elif i%5==0:print("Buzz")
    elif i%3==0:print ('Fizz')
    else:print(i)

#4 
l=[]
for i in range(1,401):
    s,m=0,i
    while m>0:
	    if (m%10)%2==0:s+=1
	    else:break
	    m=m//10
    if s==len(str(i)):l.append(i)
    else:continue
print(l)

#5
l1,l2=eval (input ('enter listl:')),eval(input("enter list2:"))
for i in range(len(l1)):
    print (l1[i],l2[-(i+1)])

#6
l1,l2=eval(input('enter listi:')),[]
for i in 11:
    if i not in l2:l2.append(i)
if l2[0]>l2[1]:maxi,sec_maxi=l2[0],l2[1]
else:maxi,sec_maxi=l2[1],l2[0]
for i in 12:
	if i>maxi:maxi,sec_maxi=i,maxi
	elif i<maxi and i>sec_maxi:sec_maxi=i
print(maxi, sec_maxi)

#7
ll=['Jan','Feb','Mar', 'Apr', 'May', 'Jun', 'Jul','Aug', 'Sep', 'Oct', 'Nov', 'Dec']
l2=[31, 28,31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print(l2[l1.index(input('enter month name(first 3 letters with lst letter in Caps:'))])

#8
l1,EvenSum, OddAverage, c=eval (input ('enter a list of integers:')),0,0,0
for i in range(len(11)):
	if i%2==0:EvenSum+=l1[i]
	else:
	    OddAverage+=l1[i]
	    c+=1
print ('Even sum: ',EvenSlum, '\n', 'Odd Average: ', OddAverage/c)

#9
l1,s=eval(input('enter a list of float values:')), []
for i in range(len(l1)):
	if round(l1[i]) not in l1:l1[i]=round(l1[i])
	elif round(l1[i]) in l1:s.append(l1[i])
for i in range(len(s)):l1.remove(s[i])
print (l1)

#10
l1,s=eval (input ("enter list:")),[]
for i in range(len(l1)):
        try:
            for j in range(i+1,len(11)):
                    if str(l1[i])[1]<str(l1[j])[1]:l1[i],l1[j]=l1[j],l1[i]
                    elif str(l1[i])[1]==str(l1[j])[1]:l1.remove(l1[4])
        except :continue
print(l1)

#A1
nl,n2=int (input ('enter a number:')),int(input('enter a second number:'))
print(nl+n2)

#2
n1,n2=int (input ('enter height:')),int(input('enter base:'))
print ('area:',n1*n2/2)

#3
n1=int(input ("enter number: "))
print ('sqrt:',n1**0.5)

#4
nl,n2,n3=int(input('enter x^2 coeff:')),int(input('enter x coeff:')),int(input('enter constant:'))
print('val1:',((-n2)+(n2**2-4*n1*n3) **0.5)/2*n1)
print('val2:',((-n2)-(n2**2-4*n1*n3)**0.5)/2*n1)

#5
n1=int (input ('enter temp in Fahrenheit:'))
print('celsius temp:',(n1-32)*5/9)

#6
n1,n2=int(input('enter divident:')),int(input('enter divisors:'))
print('quotient:',n1//n2,'\nrenainder:',nl%n2)

#7
t=10,12
u,v=t
print('before swapping')
print('u:',u,'v:',v)
u,v=v,u
print('after swapping')
print ('u:',u,'v:',v)

#8
n1,n2,n3=int(input('enter a no.:')),int(input('enter a no.:')),int(input('enter a no.:'))
print ('avg:',(nl+n2+n3)/3)

#9
nl,n2,n3=float(input('enter principle:')),int(input('enter time period(yrs):')),float(input('enter ROI:'))
print ('SI:',(n1*n2*n3) /100)

#10
n1,n2,n3=float(input('enter basic pay:')),float(input('enter hra:')),float(input('enter da:'))
n4=float(input('enter deductions:'))
print('gross pay:',(nl+n2+n3-n4))

#B1
n1=int(input ("enter age:"))
if n1<18:print('not eligible to vote')
else:print('eligible to vote')

#2
n1=int(input('enter no.:'))
if n1%2==0:print('even')
else:print('odd')

#3
n1,n2=int(input ('enter no.:')),int(input('enter another no.:'))
if n1>n2:print('largest:',n1)
elif n1==n2:print('both are equal' )
else:print ('largest:',n2)

#4
n1=input("enter no.:")
if n1.isupper():print(n1.lower())
else:print (n1.upper())

#5
n1=int(input ("enter year:'"))
if n1%4==0:print("leap year")
else:print('not leap year')

#6
n1=int(input('enter no.:'))
if n1>0:print(n1+1)
else:print(n1-1)

#7
n1,n2,op=int(input ('enter no.:')),int(input ("enter second no.:")),input('enter operator:')
if op=='+':print (n1+n2)
elif op=='-':print (n1-n2)
elif op=='*':print (n1*n2)
elif op=='/':print(n1/n2)

#8    
n1,grade=int(input('enter marks:')),''
if nl>90:grade='A'
elif nl<40:grade='F'
else:grade='B'
print ('Grade:', grade)

#9
n1,n2,n3=int(input('enter a no.:')),int(input('enter a no.:')),int(input("enter a no.:"))
if n1>n2 and n1>n3:large=n1
elif n2>n1 and n2>n3:large=n2
else:large=n3
print('largest no.:', large)

#10
n1=input('enter a no.:')
if n1.islower():print ("lower")
elif n1.isupper ():print ("upper")
elif n1.isdigit():print("digit")

#Write the output that you obtain for the following Python questions
#1
n1=int(input('enter no.:'))
if n1%2==0:print ('even')
else:print ('odd')

#2
n1,n2=input ('enter a no.:'),input('enter a no.:')
if n1>n2:print(nl)
else:print(n2)

#3
n1=input("enter no.:")
if n1.isupper():print(n1.lower())
else:print(n1.upper())

#4
n1=int(input('enter a no.:'))
if n1%35==0:print('divisible by 5 and 7')
else:print('not divisible by 5 and 7')

#5
n1=int(input("enter year:"))
if n1%4==O:print ("leap year")
else:print('not leap year')

#6
n1,n2,n3=int (input('enter 1st side:')),int(input('enter 2nd side:')),int(input('enter 3rd side:'))
if n1==n2 and n2==n3:print('equilateral triangle')
elif n1==n2 or n2==n3 or n1==n3:print('isoceles triangle')
else:print('scalene triangle')

#7
n1,n2,n3=int(input('enter 1st side:')),int(input('enter 2nd side:')),int(input('enter 3rd side:'))
if n1**2+n2**2==n3**2 or n2**2+n3**2==n1**2 or n1**2+n3**2==n2**2:print('Right angled triangle')
else:print('Not right angled triangle')

#8
n1=int(input("enter no.:"))
if n1>0:print(n1+1)
else:print(n1-1)

#9
nl,n2,op=int(input('enter no.:')),int(input ("enter second no.:")),input('enter operator:')
if op=='+':print (n1+n2)
elif op=='-':print(n1-n2)
elif op=='*':print(n1*n2)
elif op=='/':print (nl/n2)

#10
n1,grade=int(input('enter marks:')),''
if n1>90:grade='A'
elif n1<40:grade='F'
else:grade='B'
print ('Grade:', grade)

#11
n1=input("enter a no.:")
if n1.islower():print("lower")
elif n1.isupper():print("upper")
elif n1.isdigit():print("digit")

#12
n1,n2,n3=int(input('enter a no.:')),int(input('enter a no.:')),int(input('enter a no.:'))
if n1>n2 and n1>n3:large=n1
elif n2>n1 and n2>n3:large=n2
else:large=n3
print('largest no.:', large)

#13
n1=eval(input("enter something:"))
n2=input ("enter something:")
print (n1, type(n1))
print (n2, type(n2))

#While Loop
#1
n1,n2,i,f=eval(input('enter base:')),int(input('enter power:')),0,1
while i<n2:
    f*=n1
    i+=1
print(n1,'^',n2,'="',f)

#2
i=1
while i<100:
    if i%3==0 or i%4==0:print(i)
    i+=1

#3
i,f=int(input('enter a no.:')),0
while i>0:
    print (str(10**f)+'\'s place:',i%10)
    i//=10
    f+=1

#4
n1,n2,i=int(input ("enter divident:")),int(input('enter divisor:')),0
while n1>=n2:
    n1-=n2
    i+=1
print ('quotient:',i, 'remainder:',n1)
 
#5
n1,s=int(input ('enter a no.:')),0
i,n2=len(str(n1))-1,n1
while n2>0:
    a=n2%10
    n2//=10
    s+=a*(10**i)
    i-=1
if s==n1:iprint('palindrome no.')
else:print('not a palindrome no.')
  
#6
n1,s=int (input ('enter a no.:')),0
i,n2=len(str(n1)),n1
while n2>0:
    a=n2%10
    n2//=10
    s+=a**i
if s==n1:print('armstrong no.')
else:print('not a armstrong no.')

#7
n1,n2=int(input('enter a no.:')),int(input('enter another no.:'))
s,i,l=min(n1,n2),1, []
while i<=s:
    if n1%i==0 and n2%i==0:l.append(i)
    i+=1
print('GCD:',max(l))

#8
s,f,i=0,1,0
while True:
    n=input()
    if n=='q':break
    else:
        s+=int(n)
        f*=int(n)
    i+=1
print ('avg:',s/i, 'product:',f)

#9
n1=int(input("enter a no.:")) 
n2,i=round(n1/2),0
while i<=10:
    s=O
    s+=0.5*(n2+(n1/n2))
    n2=s
    i+=1
print (s)

#For Loop
#1a
for i in range(1,10):
    for j in range(1,6):
        if i<=5:
            if i>=j:print('*',end=' ')
            else:print(' ',end='')
        if i>5:
            if i+j<=10:print('*',end=' ')
            else:print(' ',end='')
    print()
#1b 
for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()

#1c
for i in range(1,8):
    for j in range(7-i):
        print(end=' ')
    x=1
    for j in range(1,i+1):
        print(x,end=' ')
        x=x*(i-j)//j
    print()

#2
n,s=input('enter a word:'),''
for i in range(len(n)-1,-1,-1):
    s+=n[i]
print(s)

#3
n,e,o=eval(input("enter a list of series of no.s:")),0,0
for i in n:  
    if i%2==0:e+=1
    else:o+=1
print ('even count:',e,'odd count:',o)

#4
datalist=[1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12],{"class":'V', "section":'A'}]
for i in datalist:
    print (i, type (i))

#5
for i in range(7):
    if i==3 or i==6:continue
    else:print(i)

#6
for i in range(1,51):
    if i%15==0:print ("FizzBuzz")
    elif i%5==0:print('Buzz')
    elif i%3==0:print('Fizz')
    else:print(i)

#7
l=[]
for i in range(100,401):
    n,c=i,0
    while n>O:
        if (n%10)%2==0:
            n//=10
            c+=1
        else:break
    if c==len(str(i)):l.append(str(i))
    else:continue
print (','.join(1))

#8
n=int(input('enter a number:'))
for i in range(1,11):print(n,'x',i, '=',n*i)

#9a
n,s=int(input('enter a number:')),0
for i in range(i,n+1):
    s+=i**(-1)
print ('sum:',s)

#9b
x,n,s=int(input('enter a no.:')),int(input('enter a no. of terms:')),1
for i in range(2,n+1):
    s+=x**i/i
print (s)

#10
x,c=int(input('enter a no. of terms:')),0
for i in range(2,x):
    if x%i==O:c+=1
if c==O:print('prime no.')
else:print('composite no.')
