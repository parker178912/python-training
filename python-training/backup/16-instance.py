# Point 實體物件的設計: 平面上座標的點
class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    # 定義實體方法
    def show(self):
        print(self.x, self.y)
    def distance(self, targetX, targetY):
        return ((self.x-targetX)**2+((self.y-targetY)**2))**0.5
p1=Point(3,4)
p1.show() # 呼叫實體方法/函式
print(p1.distance(0,0))

# FullName 實體物件的設計: 分開紀錄姓、名資料的全名
class FullName:
    def __init__(self, first, last):
        self.first=first
        self.last=last

name1=FullName("C.Y.","Cheng")
print(name1.first, name1.last)

# File 實體物件的設計: 包裝檔案的程式
class File:
    # 初始化程式
    def __init__(self, name):
        self.name=name
        self.file=None
    # 定義實體方法
    def open(self):
        self.file=open(self.name, mode="r", encoding="utf-8")
    def read(self):
        return self.file.read()
# 讀取檔案
f1=File("data1.txt")
f1.open()
data=f1.read()
print(data)