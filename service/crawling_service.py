from bs4 import BeautifulSoup
import requests

class CrawlingService:
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