from service.openai_service import OpenAIService
from service.config_service import ConfigService
from service.crawling_service import CrawlingService
import os
import json
from datetime import datetime
import os

if __name__ == "__main__":
    today_time = datetime.now().strftime("%Y%m%d")

    config_service = ConfigService()
    config_service.load_config("config/config.json")

    crawling_service = CrawlingService()
    article_list = []
    for info in config_service.naver_news_infos:
        url = info["url"] + "?date=" + today_time
        category = info["category"]
        result = crawling_service.get_naver_news_titles(url, 100, False, config_service.article_keywords)
        article_list.extend(result)
    article_result = f"[오늘의 경제 뉴스]\n {article_list}"

    finance_result = "[일일 금융 지표]\n"
    crypto_price = crawling_service.get_crypto_price(config_service.crypto_api_url, config_service.crypto_name)
    finance_result += crypto_price

    finance_infos = crawling_service.get_finance_infos(config_service.finance_selectors)
    finance_result += finance_infos

    print(article_result)
    print(finance_result)

    openai_service = OpenAIService(config_service.openai_api_key)

    user_msg = config_service.openai_prompt_user.format(
        today_time=today_time,
        finance_result=finance_result,
        article_result=article_result
    )
    system_msg = config_service.openai_prompt_system

    result = openai_service.run(user_msg, system_msg= system_msg);

   # 출력 폴더 경로
    dir_path = "output"
    file_path = os.path.join(dir_path, f"{today_time}_biz_blog.txt")

    # 폴더 없으면 생성
    os.makedirs(dir_path, exist_ok=True)

    # 파일로 저장
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(result.content)

    print(f"프롬프트가 {file_path} 파일에 저장되었습니다.")
