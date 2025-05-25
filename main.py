from service.openai_service import OpenAIService
from service.config_service import ConfigService
import os
import json

if __name__ == "__main__":
    config_service = ConfigService()
    config_service.load_config(".cred/config.json")

    openai_service = OpenAIService(config_service.openai_api_key)
    result = openai_service.run("안녕");
    print(result)
    
    
    
