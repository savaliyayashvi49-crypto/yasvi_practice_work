x=56
y=78
z=45
print("addition:",x+z)
print("subsition:",x-y)
print("maltification",x*y)
print("division:",x/z)
print("modulus'",x%z)
print("floor division:",x//z)
print("expentiation:",x**y)
opr1=23
opr2=56
opr1+=opr2
print(opr1)
opr1-=opr2
print(opr1)
opr1%=opr2
print(opr1)
opr1**=opr2
print(opr1)
opr1//=opr2
print(opr1)
#comparision opreators
print("comparision operators")
a=15
b=78
print("01.==equal:",a==b)
print("02.!=not equal",a!=b)
print("03.>greater than:",a>b)
print("04.<less than:",a<b)
print("05.<= less & equal:",a<=b)
print("06.>= greater than &equal:",a>=b)
#logical opreators
print("logical opreators")
a=True
b=False
c=False
print("01.and logical AND:",a and b)
print("02.or logical OR:",a or b)
print("03.not logical NOT:",not a)
#bitwise opreators
a=45
b=34
print("&bitwise AND:",a&b)
print("| bitwise OR:",a|b)
print("^ bitwise XOR:",a^b)
print("<< left shift:",a<<1)
print(">> right shift:",a>>1)
#condition opreators
age=20
result="ADULT"if age>=18 else "MINOR"
print(result)
#operator precedence
result=15-4*3
print(result)
#id
a=5000
b=6790
print(id(a))
print(id(b))
#identity operatar
a=[1,4,7]
b=c
c=[1,4,7]
print(b is c)
#membership opertar
numbers=[1,2,3,4,5]
print(8 in numbers)
print(4 in numbers)
