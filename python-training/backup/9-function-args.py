# 參數的預設資料
def power(base,exp=0):
    print(base**exp)
power(3,3)
power(4)

# 使用參數名稱對應
def divide(n1,n2=1):
    print(n1/n2)
divide(2,4)
divide(n2=4,n1=2)

# 無限(不定)參數資料(tuple形式)
def avg(*ns):
    print(ns)
avg(3,4)

def avg(*ns):
    sum=0
    for n in ns:
        sum+=n
    print(sum/len(ns))  
avg(3,4)
avg(3,5,10)
avg(1,4,-1,-8)