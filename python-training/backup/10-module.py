# 載入內建的sys模組並取得資訊
import sys as s
print(s.platform)
print(s.maxsize)

# 建立geometry模組，載入使用
import module.geometry as geometry
result1=geometry.distance(1,1,5,5)
print(result1)
result2=geometry.slope(1,2,5,6)
print(result2)

# 調整搜尋模組的路徑
import sys
print(sys.path) # 印出模組的搜尋路徑
print("----------------")
import module.geometry as geometry
print(geometry.distance(1,1,5,5))