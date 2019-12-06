from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def hello_world():
    context = {
        "position":-9,
        'signature': "<script>alert('hello')</script>",
        'name':['相亮亮','xlll'],
        'article':'helloasd world',
        'create_time': datetime(2019,12,2,9,10,12)
    }
    return render_template('index.html', **context)

@app.route('/login/')
def login():
    return render_template('login.html')

@app.template_filter('cut')
def cut(value):
    value = value.replace("hello",'444')
    return value

@app.template_filter('handle_time')
def handle_time(time):
    if isinstance(time, datetime):
        """
        1.如果时间间隔小于1分钟就显示刚刚
        2.如果是1小时以内，就显示xxx分钟前
        3.如果是24小时内，就显示xx小时前
        4.如果小于30天，就显示xx天前
        5.否则就显示具体的时间
        """
        now = datetime.now()
        timestamp = (now - time).total_seconds()
        if timestamp < 60 :
            return '刚刚'
        elif timestamp >= 60 and timestamp < 3600:
            minutes = timestamp / 60
            return "%s分钟前" % int(minutes)
        elif timestamp >=3600 and timestamp < 3600*24:
            hours = timestamp/3600
            return "%s小时前"% int(hours)
        elif timestamp >= 60*60*24 and timestamp <60*60*24*30:
            days = timestamp//60*60*24
            return "%s天前"% int(days)
        else:
            return time.strftime("%Y/%m/%d %H:%M")

    else:
        return time

if __name__ == '__main__':
    app.run(debug=True)
