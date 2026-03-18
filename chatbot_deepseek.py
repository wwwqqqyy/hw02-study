import requests

# 配置
API_KEY = "你的DeepSeek API Key"
API_URL = "https://api.deepseek.com/v1/chat/completions"

def chat(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}]
    }
    resp = requests.post(API_URL, json=data)
    return resp.json()["choices"][0]["message"]["content"]

if __name__ == "__main__":
    user_input = input("你：")
    print("AI：", chat(user_input))
