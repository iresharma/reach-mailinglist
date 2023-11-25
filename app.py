from flask import Flask, request
from database import create_email
from email_renderer import compile_mail
from mailing import send_mail

app = Flask(__name__)


@app.route('/')
def email_list():  # put application's code here
    email = request.args.get('email')
    if email is None or email == '':
        return "Email is a required field", 400
    try:
        out = create_email(email)
        if not out:
            return "Already exists", 200
    except Exception as _:
        return "Error", 503
    dictionary = {
        "email": email.split("@")[0]
    }
    template = compile_mail("email-list.html", dictionary)
    plaintext = ""
    with open("static/text/email-list.txt", "r") as f:
        plaintext = f.read().replace("[email]", email)
    send_mail(template, plaintext, email)
    return "Thank you for supporting Reach", 200


if __name__ == '__main__':
    app.run(debug=True)
