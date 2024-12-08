from flask import Flask, render_template, request, redirect
app = Flask(__name__)

usernames = ["missjo", "rohan", "jasraj", "andrew", "rahul", "yutika"]
password = "password"

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/check', methods=["POST"])
def formProcess():
  un = request.form.get('username')
  if un in usernames:
    return redirect("/error")
  else:
    pw1 = request.form.get('password1')
    pw2 = request.form.get('password2')
    if pw1 != pw2:
      return redirect("/error")
    else:
      usernames.append(un)
      return redirect("/success")

@app.route("/error")
def err():
  return render_template("error.html")

@app.route("/success")
def success():
  return render_template("success.html")

if __name__ == '__main__':
  app.run()