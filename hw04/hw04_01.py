from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    html_str = """

<!DOCTYPE html>
 <html lang="kr">
 <head>
 <meta charset="UTF-8">
 <script
src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
<title>넓이 계산</title>
 </head>
 <body>
 <form id="form_id" action="javascript:post_query()">
 <h2>평수 계산하기</h2>
 <label>평 :
 <input type="text" name="p" value="1">
 <button type="submit">출력</button>
 </form>
 <div id="results"></div>
 <script>
 function post_query() {
 $.ajax({
 type: "GET",
 url: "http://127.0.0.1:5000/change/pung/",
 data: $("#form_id").serialize(),
 success: update_result,
 dataType: "html"
 });
 }
 function update_result(data) {
 $("#results").html(data);
 }
 </script>
 </body>
 </html>


    """

    return html_str



@app.route('/change/pung/')
def pung_html():
    p = request.args.get("p")
    html_str = f"{(int(p) * 3.3):.6g}㎡</strong><br></n>{(int(p) / 3025):.6g}ha"
    return html_str


app.run(debug=True)
