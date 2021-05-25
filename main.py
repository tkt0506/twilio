import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='lol testing',
                              from_='whatsapp:+14155238886',
                              to=''
                          )

print(message.sid)
