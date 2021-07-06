import cv_19
import city_cv_19
import time
import cv_center
import cv_news
from flask import Flask, render_template, request,send_from_directory
from datetime import date,timedelta

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.jinja_env.add_extension('jinja2.ext.loopcontrols') 
app.jinja_env.globals.update(
    zip=zip, 
    enumerate=enumerate, 
) 



@app.route('/')
def index():   
    city = ["서울","부산","경기","광주","대구","대전","울산","세종","강원","충북","충남","전북","전남","경북","경남","제주"]
    today_1 = date.today()
    today = today_1.strftime("%Y%m%d")
    yesterday_1 = today_1 - timedelta(days=1)
    yesterday = yesterday_1.strftime("%Y%m%d")
    time1 = time.strftime("%H%M")
    time2 = time.strftime("%H%M")
    time1 = int(time1)
    time2 = int(time2)
    data1 = cv_19.get_cv_19_data(today,today)
    data2 = city_cv_19.get_city_cv_19_data(today,today)
    if not data1 or not data2:
        yesterday_1 = today_1 - timedelta(days=1)
        yesterday = yesterday_1.strftime("%Y%m%d")
        time1 = time.strftime("%H%M")
        time2 = time.strftime("%H%M")
        time1 = int(time1)
        time2 = int(time2)
        data1 = cv_19.get_cv_19_data(yesterday,yesterday)
        data2 = city_cv_19.get_city_cv_19_data(yesterday,yesterday)
    
    newsData = cv_news.cvNews() 
    return render_template("index.html",data1=data1,data2=data2,city=city,newsData=newsData) 
    
@app.route('/center',methods=['GET','POST'])
def center():   
    result = cv_center.mapCreate('시')
    size = 0
    if request.method == 'POST':
        loc = request.form['loc']
        result = cv_center.mapCreate(loc)
        size = 1
    return render_template("center.html",result=result,size = size)

if __name__ == "__main__":
    app.run(debug=True)


