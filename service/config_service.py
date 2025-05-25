import json

class ConfigService():
    # def __init__(self):
    def load_config(self, path):
        with open(path, "r", encoding="utf-8") as f:
            self.config = json.load(f)

        openai_cred_path = self.config["cred_path"]
        openai_cred_system_path = self.config["openai_prompt_system_path"]
        openai_cred_user_path = self.config["openai_prompt_user_path"]

        with open(openai_cred_path, "r", encoding="utf-8") as f:
            config = json.load(f)
            self.openai_api_key = config["openai_api_key"]
            print(self.openai_api_key)

        with open(openai_cred_system_path, "r", encoding="utf-8") as f:
            self.openai_prompt_system = f.read()
            print(self.openai_prompt_system)

        with open(openai_cred_user_path, "r", encoding="utf-8") as f:
            self.openai_prompt_user = f.read()

        self.gpt_model = self.config["gpt_model"]
        self.crypto_api_url = self.config["crypto_api_url"]
        self.crypto_name = self.config["crypto_name"]
        self.finance_selectors = self.config["finance_selectors"]
        self.naver_news_infos = self.config["naver_news_infos"]
        self.article_keywords = self.config["article_keywords"]

    def get_config(self, key):
        return self.config[key]
