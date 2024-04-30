from flask import Flask, render_template, send_from_directory
import os
app = Flask(__name__)

# 設定暫存資料夾路徑
temp_folder = 'user_folder'
app.config['temp_folder'] = temp_folder
temp_dir = app.config['temp_folder']

# 建立暫存資料夾（如果不存在）
if not os.path.exists(temp_folder):
    os.makedirs(temp_folder)

@app.route('/')
def show_summary():
    return render_template('summary.html')

# 提供摘要檔案的路由
@app.route('/get_summary')
def get_summary():
    summary_path = os.path.join(temp_dir, 'summary-2.txt')
    return send_from_directory(temp_dir, 'summary-2.txt')

if __name__ == '__main__':
    app.run(debug=True, port=5001)