# Simple Groq API REST call example

import requests
import poml
import os
  
  
API_URL = "https://api.groq.com/openai/v1/chat/completions"
API_KEY = os.getenv("GROQ_API_KEY")
if not API_KEY:
    raise ValueError("GROQ_API_KEY environment variable not set.")

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}
 

# SYSTEM_PROMPT = "You are an expert assistant that provides clear and concise answers."

system_prompt = poml.poml("input/template.poml",  context=None, chat=True)
# print("System Prompt:", system_prompt)
data = {
        # "model": "gemma2-9b-it",
        
         "model": "qwen/qwen3-32b",
         "temperature": 1,
         "max_completion_tokens": 1024,
         "top_p": 1,
         "stream": False,
         "stop": None,
    "messages": [ 
        {"role": "system", "content":  system_prompt[0]["content"]}, 
        {"role": "user", "content":  "analyze the stock prices of AAPL in the table and gimme summary."}
    ]
}

 

response = requests.post(API_URL, headers=headers, json=data)
print("Response Status Code:", response.status_code)

if response.status_code == 200:
    response_json = response.json()
    output = response_json['choices'][0]['message']['content']
    print(output)
    with open("output/result.md", "w", encoding="utf-8") as f:
        f.write(output)
else:
    print("Error:", response.status_code, response.text)