# # 儲存檔案
# # <1>一般寫法
# file=open("data.txt", mode="w", encoding="utf-8") # utf=8為中文編碼
# file.write("Hello File\nSecond line\n測試中文")
# file.close()
# # <2>最佳實務寫法
with open("data.txt", mode="w", encoding="utf-8") as file:
    file.write("測試中文\n好棒棒")

# 讀取檔案
with open("data.txt", mode="r", encoding="utf-8") as file:
    data=file.read()
print(data)

# 把檔案中的數字資料，一行一行的讀取出來，並計算總合
with open("data.txt", mode="w", encoding="utf-8") as file:
    file.write("5\n3")
sum=0
with open("data.txt", mode="r", encoding="utf-8") as file:
    for line in file:
        sum+=int(line)
print(sum)

# 使用JSON格式讀取、複寫檔案
import json
with open("config.json", mode="r") as file:
    data=json.load(file)
print("name: ", data["name"])
data["name"]="New Name"
print("name: ", data["name"])
print("version: ", data["version"])
with open("config.json", mode="w") as file:
    data=json.dump(data, file)