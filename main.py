from service.openai_service import OpenAIService
from service.config_service import ConfigService
from service.crawling_service import CrawlingService
import os
import json
from datetime import datetime
import requests

if __name__ == "__main__":
    today_time = datetime.now().strftime("%Y%m%d")

    config_service = ConfigService()
    config_service.load_config(".cred/config.json")

    #openai_service = OpenAIService(config_service.openai_api_key)
    #result = openai_service.run("안녕");
    #print(result)

    crawling_service = CrawlingService()
    for info in config_service.naver_news_infos:
        url = info["url"] + "?date=" + today_time
        category = info["category"]
        result = crawling_service.get_naver_news_titles(url,1, False)
        print(category, result)

    
    
    
