#Импорт
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')


#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    email = request.form.get('email')
    text = request.form.get('text')
    button_html = request.form.get('button_html')
    button_ds = request.form.get('button_ds')
    return render_template('index.html', button_python=button_python,text=text,email=email,button_ds=button_ds,button_html=button_html)


if __name__ == "__main__":
    app.run(debug=True)