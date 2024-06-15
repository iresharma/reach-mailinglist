# Reach waiting service

Microservice for recording and handling mailing list.

## Archived in favor of a self host of listmonk

### TODO:

GET: /
- [x] Create database connection
- [x] Design a model
```json
{
  "email": "string",
  "created_at": "string" // automatically created by ORM 
}          
  ```
- [x] Store email address filled by user
- [x] compile html template, using jinja
- [x] Send mail to address (using resend, great pricing)

### Send mail to address

1. [resend](https://resend.com/) ---- 3000 -> $0
2. [Gmail API](https://developers.google.com/gmail/api/reference/quota) ---- 3000 -> $0 (but more than 3 mails/s == 429)
3. [AWS SES](https://aws.amazon.com/ses/pricing/) ---- 3000 -> $0.3

> railway bailed on me commit so that i can deploy
