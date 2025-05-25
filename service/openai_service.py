from openai import OpenAI

class OpenAIService():
    def __init__(self, api_key):
        self.api_key = api_key
        self.client = OpenAI(api_key=self.api_key)

    def run(self, msg, model = "gpt-4o-mini", system_msg = ""):
        messages=[]
        if system_msg:
            messages.append({
                "role": "system",
                "content": system_msg
            })
        messages.append({
            "role": "user", "content": msg
        })
        completion = self.client.chat.completions.create(
        model=model,
        store=True,
        messages=messages)

        return completion.choices[0].message