from flask import Flask,render_template,request

app = Flask(__name__)

@app.before_request
def count_spider():
    if "requests" in request.headers.get("User-Agent"):
        return "检测到requests爬虫请求！"


@app.route('/')
def begin_exam():  # put application's code here
    return render_template("index.html")


@app.route("/weather")
def weather():
    return render_template("2-weather.html")


@app.route("/movie")
def movie():
    return render_template("3-movie.html")


@app.route("/book")
def book():
    return render_template("4-book.html")

@app.route("/suv")
def suv():
    return render_template("1-suv.html")

@app.route("/phone")
def phone():
    return render_template("5-phone.html")

@app.route("/computer")
def computer():
    return render_template("6-computer.html")

@app.route("/air")
def air():
    return render_template("7-air.html")

@app.route("/fridge")
def fridge():
    return render_template("8-fridge.html")

@app.route("/desktop")
def desktop():
    return render_template("9-desktop.html")

@app.route("/huawei")
def huawei():
    return render_template("10-huawei.html")

@app.route("/camera")
def camera():
    return render_template("11-camera.html")

@app.route("/television")
def television():
    return render_template("12-television.html")

@app.route("/people")
def people():
    return render_template("13-people.html")

@app.route("/mp3")
def mp3():
    return render_template("14-mp3.html")

@app.route("/headset")
def headset():
    return render_template("15-headset.html")

@app.route("/echarts_show/pie_book.html")
def pie_book2():
    return render_template("../echarts_show/pie_book.html")

if __name__ == "__main__":
    app.run(debug=True)