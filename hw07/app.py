from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/to_eunbin_page')
def to_eunbin_page():
    return render_template('to_eunbin_page.html')

@app.route('/to_juyoung_page')
def to_juyoung_page():
    return render_template('to_juyoung_page.html')

if __name__ == '__main__':
    app.run(debug=True)
