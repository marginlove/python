import decimal
from decimal import Decimal
b=0.35
print(b)
b=b+0.1
print(b)
b=0.1
print(b)
b=1/11
print(b)
b=decimal.Decimal(1)/decimal.Decimal(11)
print(b)
decimal.getcontext().prec=50
e=Decimal(1)/Decimal(11)
print(e)
decimal.getcontext().prec=60
e=Decimal(1)/Decimal(11)
print(e)
