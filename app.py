from flask import Flask, render_template, request, redirect
app = Flask(__name__)

usernames = ["missjo", "rohan", "jasraj", "andrew", "rahul", "yutika"]
password = "password"

error_feedback = ""

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/check', methods=["POST"])
# for security reasons!
def formProcess():
  global error_feedback
  un = request.form.get('username')
  if un in usernames:
    error_feedback = "The username is invalid."
    return redirect("/error")
  else:
    pw1 = request.form.get('password1')
    pw2 = request.form.get('password2')
    if pw1 != pw2:
      error_feedback = "The passwords do not match."
      return redirect("/error")
    else:
      usernames.append(un)
      return redirect("/success")

@app.route("/signin", methods=["POST"])
def signin():
  global error_feedback
  un = request.form.get('susername')
  if un in usernames:
    # good!
    pw = request.form.get('spassword')
    if pw == password:
      # log in!
      return redirect("/login")
    else:
      error_feedback = "Invalid credentials."
      return redirect("/error")
  else:
    error_feedback = "Invalid username."
    return redirect("/error")

@app.route("/error")
def err():
  return render_template("error.html", msg=error_feedback)

@app.route("/success")
def success():
  return render_template("success.html")

@app.route("/login")
def login():
  return render_template("loggedin.html")

if __name__ == '__main__':
  app.run()