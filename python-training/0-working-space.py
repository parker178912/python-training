# 抓取 PPT 電影版的網頁原始碼(HTML)
import urllib.request as req
url = "https://www.ptt.cc/bbs/movie/index.html"
# 建立一個 Request 物件，附加Request Headers 的資訊
request = req.Request(url, headers={
  "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50"
}) #讓程式看起來像人，header由網頁按f12找，在index.html裡的request headers，找裡面的user-agent
with req.urlopen(request) as response:
  data = response.read().decode("utf-8")
#print(data)  #網頁程式
  
import bs4
root = bs4.BeautifulSoup(data, "html.parser") #讓beautifulsoup協助我們做篩選
#print(root.title.string) #網頁標題
titles = root.find_all("div", class_= "title") #尋找所有class="title" 的div標籤
#print(titles.a.string) #a是代表<a...，然後取文字
for title in titles:
  if title.a != None:
    print(title.a.string)