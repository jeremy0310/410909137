from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():
    x = "<h1>企管四B陳昭毅的求職相關資訊</h1>"
    x += "<a href=/aboutme>個人簡介</a><br>"
    x += "<a href=/work>ERP系統工作相關介紹</a><br>"
    x += "<a href=/UCAN>職涯測驗分析</a><br>"
    x += "<a href=/future>自傳履歷</a><br>"
    return x

@app.route("/aboutme")
def about():
    return render_template("aboutme.html")

@app.route("/work")
def work():
    return render_template("work.html")
    

@app.route("/UCAN")
def test():
    return render_template("UCAN.html")

@app.route("/future")
def myself():
    return render_template("future.html")

if __name__ == "__main__":
    app.run()