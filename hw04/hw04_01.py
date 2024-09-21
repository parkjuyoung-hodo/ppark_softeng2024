from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    html_str = """


<!DOCTYPE html>
<<<<<<< HEAD
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
=======
<html lang="kr">
<head>
    <meta charset="UTF-8">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <title>면적 계산</title>
</head>
<body>
    <form id="form_id" action="javascript:post_query()">
        <h2>면적 계산하기</h2>
        <label>평수:
            <input type="text" name="p">
            <button type="submit">평 -> ㎡ 및 ha</button>
        </label>
        <br>
        <label>㎡:
            <input type="text" name="m2">
            <button type="button" onclick="post_m2_query()">㎡ -> 평 및 ha</button>
        </label>
        <br>
        <label>ha:
            <input type="text" name="ha">
            <button type="button" onclick="post_ha_query()">ha -> 평 및 ㎡</button>
        </label>
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
>>>>>>> 8e684a5 (3주차 과제 코드)

    function post_m2_query() {
        const m2 = $("input[name='m2']").val();
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:5000/change/m2/",
            data: { m2: m2 },
            success: update_result,
            dataType: "html"
        });
    }

    function post_ha_query() {
        const ha = $("input[name='ha']").val();
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:5000/change/ha/",
            data: { ha: ha },
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

<<<<<<< HEAD


@app.route('/change/pung/')
def pung_html():
    p = request.args.get("p")
    html_str = f"{(int(p) * 3.3):.6g}㎡</strong><br></n>{(int(p) / 3025):.6g}ha"
    return html_str


=======
@app.route('/change/pung/')
def pung_html():
    p = request.args.get("p")
    m2 = (int(p) * 3.3)
    ha = (int(p) / 3025)
    html_str = f"{m2:.6g} ㎡<br>{ha:.6g} ha"
    return html_str


@app.route('/change/m2/')
def m2_html():
    m2 = request.args.get("m2")
    p = (int(m2) / 3.3)
    ha = (int(m2) / 10000)
    html_str = f"{p:.6g} 평<br>{ha:.6g} ha"
    return html_str


@app.route('/change/ha/')
def ha_html():
    ha = request.args.get("ha")
    p = (int(ha) * 3025)
    m2 = (int(ha) * 10000)
    html_str = f"{p:.6g} 평<br>{m2:.6g} ㎡"
    return html_str

>>>>>>> 8e684a5 (3주차 과제 코드)
app.run(debug=True)
