# Simple Groq API REST call example

import requests
import poml
import os
import re
from pathlib import Path
  
API_URL = "https://api.groq.com/openai/v1/chat/completions"
API_KEY = os.getenv("GROQ_API_KEY")
if not API_KEY:
    raise ValueError("GROQ_API_KEY environment variable not set.")

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def build_system_prompt():
    """
    Reads template.prompt.txt, then reads the image and CSV file, parses them, replaces placeholder content,
    and returns the final system prompt string. Validates to ensure it doesn't break the code.
    """
    base_dir = Path(__file__).parent
    # 1. Read template.prompt.txt
    template_path = base_dir / "template.prompt.txt"
    with open(template_path, "r", encoding="utf-8") as f:
        prompt = f.read()
    # 2. Read the image and CSV file (just get their filenames for prompt)
    image_files = ["chart_normalized_price.png", "chart_price.png"]
    csv_file = "104.xlsx"
    # 3. Replace placeholders in the template
    prompt = prompt.replace("{CSV_FILE}", csv_file)
    prompt = prompt.replace("{IMAGE1}", image_files[0])
    prompt = prompt.replace("{IMAGE2}", image_files[1])
    # 4. Validate: ensure no unreplaced placeholders remain
    if re.search(r"{[A-Z0-9_]+}", prompt):
        raise ValueError("Unreplaced placeholders found in system prompt!")
    return prompt

SYSTEM_PROMPT = build_system_prompt()
  
data = { 
         "model": "qwen/qwen3-32b",
         "temperature": 1,
         "max_completion_tokens": 1024,
         "top_p": 1,
         "stream": False,
         "stop": None,
        "messages": [ 
            {"role": "system", "content": SYSTEM_PROMPT}, 
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