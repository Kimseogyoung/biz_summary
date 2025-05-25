from openai import OpenAI

class OpenAIService():
    def __init__(self, api_key):
        self.api_key = api_key
        self.client = OpenAI(api_key=self.api_key)

    def run(self, msg, model = "gpt-4o-mini"):
        completion = self.client.chat.completions.create(
        model=model,
        store=True,
        messages=[
            {"role": "user", "content": msg}
        ]
        )

        print(completion.choices[0].message);