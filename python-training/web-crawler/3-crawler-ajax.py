# 抓取 PTT 電影版的網頁原始碼 (HTML)
import urllib.request as req
url="https://medium.com/_/api/home-feed"
# 建立一個 Request 物件，附加 Request Headers 的資訊
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8") # 根據觀察，取得資料是 JSON 格式而非 html

# 解析 JSON 格式的資料，取得每篇文章的標題
import json
data=data.replace("])}while(1);</x>","")
data=json.loads(data) # 把原始的 JSON 解析成字典/列表的形式
# 取得 JSON 資料中的文章標題
posts=data["payload"]["references"]["Post"]
for key in posts:
    post=posts[key]
    print(post["title"])
