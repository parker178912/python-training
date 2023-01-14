# 集合的運算
s1={3,4,5}
print(s1)
print(3 in s1) # True
print(10 not in s1) #True

s2={4,5,6,7}
s3=s1&s2 # 交集: 取兩個集合中相同的資料 {4,5}
s3=s1|s2 # 聯集: 取兩個集合所有的資料。但不重複 {3,4,5,6,7}
s3=s1-s2 # 差集: s1有但s2沒有 {3}
s3=s1^s2 # 反交集: 取兩個集合中，不重疊的部分 {3,6,7}

s=set("Hello") # 把字串拆解成集合: set(字串)
print("H" in s) # True

# 字典: key-value配對
dic={"apple":"蘋果","bug":"蟲蟲"}
dic["apple"]="小蘋果"
print(dic["apple"])
print("test" in dic) # 判斷 key 是否存在
del dic["apple"] # 刪除字典中的鍵值對 (key-value pair)
print(dic)

# 字典的運算
dic={x:x*2 for x in[3,4,5]} # 從列表的資料產生字典
print(dic)