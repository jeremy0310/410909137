rom flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():
    x = "<h1>資管二A游欣婕的求職相關資訊</h1>"
    x += "<a href=/about>個人簡介</a><br>"
    x += "<a href=/work>ERP系統工作相關介紹</a><br>"
    x += "<a href=/test>職涯測驗分析</a><br>"
    x += "<a href=/myself>自傳履歷</a><br>"
    return x


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/work")
def work():
    return render_template("work.html")
    

@app.route("/test")
def test():
    return render_template("test.html")

@app.route("/myself")
def myself():
    return render_template("myself.html")

if __name__ == "__main__":
    app.run()