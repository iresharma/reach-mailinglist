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
    send_mail(template, plaintext, email, "Thank you for supporting Reach at early stages")
    return "Thank you for supporting Reach", 200

@app.route("/verify/mail")
def verify_mail():
    args = dict(request.args)
    token = args.get("token", "")
    mail = args.get("email", "")
    subject = args.get("subject", "")
    template = compile_mail("verify.html", args)
    plaintext = ""
    with open("static/text/verify.txt", "r") as f:
        plaintext = f.read().replace("[token]", token)
    send_mail(template, plaintext, mail, subject)
    return "Thank you for supporting Reach", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
