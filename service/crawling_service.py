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

    def get_naver_news_titles(self, url, cnt = 1, is_include_body = True, keywords = []):
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

            if keywords and not any(kw in title for kw in keywords):
                print(f"키워드 불일치: {title}")
                continue
            
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
    def get_finance_infos(self, finance_selectors):
        result = ""
        for selector in finance_selectors:
            res = requests.get(selector["url"])
            soup = BeautifulSoup(res.text, "html.parser") 
            select = soup.select_one(selector["selector"])
            if "change_selector" in selector:
                select_change = soup.select_one(selector["change_selector"])
                change = f"{select_change.text.strip()} {selector['unit']}"
                direction = soup.select_one(selector["direction_selector"]).text.strip()  # 보통 마지막 blind가 방향
                if direction == "상승":
                    change = f"+{change}"
                elif direction == "하락":
                    change = f"-{change}"
                change = f"({change})"
            else:
                change = ""
            value = select.text.strip()
            result += f"{selector['name']}: {value}{selector['unit']} {change}\n"
        return result
