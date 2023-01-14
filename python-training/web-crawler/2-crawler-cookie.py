# 抓取 PTT 八卦版的網頁原始碼 (HTML)
from pkgutil import get_data
import urllib.request as req
def getdata(url):      
    # 建立一個 Request 物件，附加 Request Headers 的資訊
    request=req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39",
        "cookie":"over18=1" # 加上 cookie
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    # 解析原始碼，取得每篇文章的標題
    import bs4
    root=bs4.BeautifulSoup(data, "html.parser")
    titles=root.find_all("div", class_="title")
    for title in titles:
        if title.a!= None:
            print(title.a.string)
    # 抓取上一頁網址
    nextlink=root.find("a", string="‹ 上頁")
    return nextlink["href"]

pageurl="https://www.ptt.cc/bbs/Gossiping/index.html"
count=0
while count<5:
    pageurl="https://www.ptt.cc"+getdata(pageurl)
    count+=1
print(pageurl)