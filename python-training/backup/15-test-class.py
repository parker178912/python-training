# 定義類別與類別屬性(封裝在類別中的變數和函式)
# 定義一個類別IO，有兩個屬性 supportedSrs 和 read
class IO:
    supportedSrs=["console", "file"]
    def read(src):
        if src not in IO.supportedSrs:
            print("Not supported")
        else:
            print("Read from", src)
# 使用類別
print(IO.supportedSrs)
IO.read("file")
IO.read("internet")