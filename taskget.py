from flask import Flask,request

app=Flask(__name__)

@app.route("/testfun")
def test():
    get_name=request.args.get("get_name")
    mob=request.args.get("mobile")
    mail=request.args.get("mail")
    return "this is my first function for get {}{}{}".format(get_name,mob,mail)

if "__name__"=="__main__":
    app.run(port=5002)
