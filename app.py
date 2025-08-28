import os
from flask import Flask, render_template

app = Flask(__name__)  # 默认加载templates和static，无需显式声明

people = [
    {"name":"张昕妮","title":"部长"},{"name":"张咸亮","title":"副部长"},
    {"name":"林子琪","title":"副部长"},{"name":"徐梣恩","title":"后勤组组长"},
    {"name":"翁珊妮","title":"唱歌组组长"},{"name":"陈羲芝","title":"乐器组组长"},
    {"name":"洪雅镁","title":"乐器组组长"},{"name":"俞昕玲","title":"舞蹈组组长"}
]
images = [f"{i}.jpg" for i in range(1,12)]

@app.route('/')
def index(): return render_template('index.html', images=images, people=people)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT',5000)), debug=False)