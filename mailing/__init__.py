import resend


def send_mail(template: str, plaintext: str, email_id: str, subject: str):
    """
    Takes compiled template and plain text to send a mail
    :param template: compiled template
    :param plaintext: plaintext with email
    :param email_id: email id
    :param subject: subject of the email
    :return:
    """
    r = resend.Emails.send({
        "from": "Team Reach <me@iresharma.com>",
        "to": email_id,
        "subject": subject,
        "html": template,
        "text": plaintext
    })
