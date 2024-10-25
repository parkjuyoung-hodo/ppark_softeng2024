from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route('/')
def index_page():
    return render_template('index.html', title='Home')

@app.route('/to_eunbin_page')
def to_eunbin_page():
    return render_template('to_eunbin_page.html', title="to_eunbin_page")

@app.route('/to_juyoung_page')
def to_juyoung_page():
    return render_template('to_juyoung_page.html', title="to_juyoung_page")

@app.route('/blog')
def blog_list():

    df = pd.read_csv("data.csv")
    post_list = []
    for i, row in df.iterrows():
        post_list.append({
            "title": row["title"],
            "content": row["content"],
            "date": row["date"]
        })

    print(post_list)
    return render_template('blog.html', title="blog post",posts=post_list)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)