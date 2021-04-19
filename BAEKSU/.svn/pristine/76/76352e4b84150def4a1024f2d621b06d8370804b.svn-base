import requests 
from bs4 import BeautifulSoup

class Scrap:
    def __init__(self):
        self.temp_list = []
            
    def job_list(self, job_name):
        keyword = {'웹개발자':'404',
                   '앱개발자':'404',
                   '데이터베이스':'402',
                   '게임':'405',
                   'AI빅데이터':'417',
                   '서버보안':'402'}
        
        URL = f'https://www.saramin.co.kr/zf_user/search?cat_cd='+keyword[job_name]
        response = requests.get(URL)
        response.encoding = "UTF-8"
        
        html = response.text  
        soup = BeautifulSoup(html, 'html.parser')  
        
        job_openings = soup.find_all('h2',{'class':'job_tit'}) 
        companys = soup.find_all('strong',{'class':'corp_name'}) 
        
        ahead = 'https://www.saramin.co.kr/zf_user/jobs/relay/view?isMypage=no&rec_idx='
        
        cnt = 0
        for idx, jo in enumerate(job_openings) :
            job_title = jo.a['title']
            job_link = ahead+jo.a['href'][50:58]
            company_name = companys[idx].a['title']
            
            temp = {"scrap_seq" : idx
                   ,"scrap_name": job_title
                   ,"scrap_comp": company_name
                   ,"scrap_url" : job_link }
            
            self.temp_list.append(temp)
            
        return self.temp_list
        
    def news_list(self, news_category):
        keyword = {'IT일반':'230',
                   '컴퓨터':'283',
                   '모바일':'731',
                   '인터넷':'226', 
                   '보안':'732'
                }
        
        headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
                }
        
        URL = f'https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2='+keyword[news_category]
        response = requests.get(URL, headers=headers)
        response.encoding = "euc-kr"
        
        html = response.text  
        soup = BeautifulSoup(html, 'html.parser')  
        
        news_titles = soup.find_all('ul',{'class':'type06_headline'}) 
        
        for i in news_titles :
            for j in i.children :
                if str(type(j))=="<class 'bs4.element.Tag'>":
                    try :
                        news_title = j.findChild("img")['alt']
                    except :
                        news_title = j.findChild("a").text
                    news_url = j.findChild("a")['href']
                    temp_dict = {'news_title': news_title
                               ,'news_url': news_url
                               }
                    self.temp_list.append(temp_dict)
    
        return self.temp_list
    
    
#if __name__ == "__main__":    
#    Scrap().news_list('컴퓨터')


