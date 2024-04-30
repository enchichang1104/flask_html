import os
import openai
from flask import Flask, render_template

app = Flask(__name__)

openai.api_key = "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"

# 設定暫存資料夾路徑
temp_folder = 'user_folder'
app.config['temp_folder'] = temp_folder
temp_dir = app.config['temp_folder']


# Function to extract summary from a text file
def generate_keyword(file_path):
    with open(file_path, "r") as file:
        text = file.read()

        # Call OpenAI summarization model
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt="give me nine english keywords of "+text+"and add a description under the each keyword.",
            max_tokens=2000
        )

        # Extract the summary
        keywords = response.choices[0].text.strip()
        return keywords
    

def modify_keytxt(original_file_path,updated_file_path):
    # 開啟原始txt檔案
    with open(original_file_path, 'r') as f:
        lines = f.readlines()

    # 去除開頭的數字及空白行
    filtered_lines = [line.split('. ', 1)[-1].strip() for line in lines if line.strip() and line.strip()[0].isdigit()]

    # 將過濾後的內容寫入新的txt檔案
    with open(updated_file_path , 'w') as f:
        f.write('\n'.join(filtered_lines))

def read_keyword(file_path):
    keyword_explanation = {}
    with open(file_path, 'r') as file:
        for line in file:
            if '-' in line or ':' in line:
                delimiter = '-' if '-' in line else ':'
                keyword, explanation = line.split(delimiter, 1)
                keyword = keyword.strip()
                explanation = explanation.strip()
                keyword_explanation[keyword] = explanation
    return keyword_explanation

@app.route("/")
def index():

    #keywords.txt
    # summary_file = os.path.join(temp_dir, 'summary.txt')
    # question = generate_keyword(summary_file)
    # with open(os.path.join(temp_dir, 'keywords.txt'), 'w') as f:
    #     f.write(question)
    
    # final_keyword = os.path.join(temp_dir,'change_keywords.txt')
    # modify_keytxt(os.path.join(temp_dir, 'keywords.txt'),final_keyword)

    key_file = os.path.join(temp_dir,'change_keywords.txt')
    keywords_explanations = read_keyword(key_file)

    
    return render_template('Outline.html', keyword_explanation=keywords_explanations)

if __name__ == "__main__":
    app.run(debug=True, port=5001)