from flask import Flask, render_template, request
import requests
import smtplib

MY_EMAIL = "python.gmtest@gmail.com"
PASSWORD = "japk vivn hvwk munx"

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


# @app.route("/contact")
# def contact():
#     return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


# # @app.route('/form-entry', methods=['post'])
# def receive_data():
#     username = request.form['name']
#     email_id = request.form['email']
#     phone_no = request.form['phone']
#     msg = request.form['message']
#     return f"<h1> Successfully sent your message </h1>"


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        username = request.form['name']
        email_id = request.form['email']
        phone_no = request.form['phone']
        msg = request.form['message']
        formatted_string = f"Subject:New Message\n\n Name:{username}\n Email: {email_id}\n Phone: {phone_no}, Message: {msg}"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail('python.gmtest@yahoo.com', MY_EMAIL, msg=formatted_string)

        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
