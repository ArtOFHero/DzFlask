from flask import Flask, render_template, request
import datetime

app = Flask(__name__)


#Главная страница
@app.route('/home')
@app.route('/')
def home():
    return render_template('/home.html', utc_dt=datetime.datetime.today().strftime("%d.%m.%Y"), b=datetime.datetime.today().strftime("%H:%M:%S"))


@app.route('/summary')
def summary():
    return render_template('/summary.html')


@app.route('/comments')
def comments():
    comments = ['Это первый комментарий.',
               'Это второй комментарий',
               'Это третий комментарий',
               'Это четвёртый комментарий.'
               ]
    return render_template('/comments.html', comments=comments)


if __name__ == '__main__':
    app.run(debug=True)