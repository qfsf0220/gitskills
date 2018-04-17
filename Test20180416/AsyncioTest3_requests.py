import concurrent.futures as cf
import  asyncio
import requests
from    bs4 import BeautifulSoup

def get_title(i):
    url = 'https://movie.douban.com/top250?start={}&filter='.format(i*25)
    r =requests.get(url)
    soup= BeautifulSoup(r.content,'html.parser')
    lis = soup.find("ol",class_="grid_view").find_all("li")
    for i in lis:
        title= i.find('span',class_="title").text
        print(title)

async def main():
    with cf.ThreadPoolExecutor(max_workers=10) :
        loop = asyncio.get_event_loop()
        futures = (loop.run_in_executor(None,get_title,i) for i in range(10))
        for i in await asyncio.gather(*futures):
            pass
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
