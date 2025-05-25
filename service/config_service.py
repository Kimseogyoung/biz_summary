import json

class ConfigService():
    # def __init__(self):
    def load_config(self, path):
        with open(path, "r", encoding="utf-8") as f:
            self.config = json.load(f)

        self.openai_api_key = self.config["openai_api_key"]
        self.gpt_model = self.config["gpt_model"]
        self.crypto_api_url = self.config["crypto_api_url"]
        self.crypto_name = self.config["crypto_name"]
        self.exchange_url = self.config["exchange_url"]
        self.dollar_selector = self.config["dollar_selector"]
        self.gold_selector = self.config["gold_selector"]
        self.news_url = self.config["news_url"]
        self.news_title_selectors = self.config["news_title_selectors"]
        self.naver_news_infos = self.config["naver_news_infos"]

    def get_config(self, key):
        return self.config[key]
