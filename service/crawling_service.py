from bs4 import BeautifulSoup
import requests

class CrawlingService:

    # 네이버버
    # ✅ 뉴스 본문 크롤링
    def get_naver_news_body(self,url):
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")
        tag = soup.select_one("#dic_area")
        return tag.text.strip() if tag else ""

    def get_naver_news_titles(self, url, cnt = 1, is_include_body = True):
        headers = {"User-Agent": "Mozilla/5.0"}

        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")

        # 뉴스 제목 + 링크 추출
        articles = soup.select(".sa_text_title")[:cnt]

        result = []
        for i, a in enumerate(articles, 1):
            title = a.text.strip()
            link = a['href']
            body = ""
            if is_include_body:
                body = self.get_news_body(link)
            result.append({
                "제목": title,
                "내용": body,
                "링크": link,
            })
        return result

    # 암호화폐
    def get_crypto_price(self, url, crypto_name):
        res = requests.get(url).json()
        price = res[0]['trade_price']
        change_rate = res[0]['signed_change_rate'] * 100
        return f"{crypto_name}: {price:,.0f}원 ({change_rate:+.2f}%)"
    
    # 환율 + 금 시세
    def get_exchange(self, url, exchange_selectors):
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        result = ""
        for selector in exchange_selectors:
            select = soup.select_one(selector["selector"])
            value = select.text.strip()
            result += f"{selector['name']}: {value}원\n"
        return result
