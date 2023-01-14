# 數字運算
# x = 2+3
# print(x)
# x//=1 # x = x+1 # 將變數中的字 +1
# print(x)

# 字串運算
# s = "Hell\"o"  # \ = 跳脫 = Hell"o
# print(s)
# s = "hello" "world"
# print(s)
# s = "Hello\nworld"
# print(s)
# s = "Hello"*3+"world"
# print(s)
# 字串會對內部的字元編號(索引)，從 0 開始算起
s = "hello"
print(s[1:4])   # 包含開頭不包含結尾，得 ell
s = "hello"
print(s[1:])    # 包含開頭的全部到結尾，得 ello
s = "hello"
print(s[:4])    # 開頭的全部到結尾前一個，得 hell