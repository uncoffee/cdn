from flask import Flask, make_response , render_template,request , redirect, url_for
text = None

@app.route("/" , methods = ["get"])

@app.route("/plz/text" , methods = ["get"])
if text == None:
    #tcp通信してデータを持ってくる。
    text = result
    
return render_template("index.html",text = text)