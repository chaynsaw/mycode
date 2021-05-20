#!/usr/bin/python3
from flask import Flask, request, session, redirect, url_for
from flask import render_template

app = Flask(__name__)
app.secret_key = "any random string"

groups = [{"hostname": "hostA","ip": "192.168.30.22", "fqdn": "hostA.localdomain"},
          {"hostname": "hostB", "ip": "192.168.30.33", "fqdn": "hostB.localdomain"},
          {"hostname": "hostC", "ip": "192.168.30.44", "fqdn": "hostC.localdomain"}]

@app.route("/")
def index():
  ## if the key "username" has a value in session
  if "username" in session:
    username = session["username"]
    return render_template("jinjahosts.html", hosts=groups)

  ## if the key "username" does not have a value in session
  return "You are not logged in <br><a href = '/login'></b>" + \
      "click here to log in</b></a>"

@app.route("/addhosts", methods = ["POST"])
def add_hosts():
    if session['username'] == "admin":
        groups.append({
            "hostname": request.form.get("hostname"),
            "fqdn": request.form.get("fqdn"),
            "ip": request.form.get("ip")
        })
        return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))

## If the user hits /login with a GET or POST
@app.route("/login", methods = ["GET", "POST"])
def login():
   ## if you sent us a POST because you clicked the login button
   if request.method == "POST":

      ## request.form["xyzkey"]: use indexing if you know the key exists
      ## request.form.get("xyzkey"): use get if the key might not exist
      session["username"] = request.form.get("username")
      return redirect(url_for("index"))

   ## return this HTML data if you send us a GET
   return """
   <form action = "" method = "post">
      <p><input type = text name = username></p>
      <p><input type = submit value = Login></p>
   </form>
  """

@app.route("/logout")
def logout():
   # remove the username from the session if it is there
   session.pop("username", None)
   return redirect(url_for("index"))

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)
