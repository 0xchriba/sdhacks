import os
from twilio.rest import Client

account_sid = None
auth_token = None
client = Client(account_sid, auth_token)
message = client.messages.create(
    "to",
    body='hello',
    from_="+14159004260",
    media_url="http://firstdescents.org/wp-content/uploads/2014/01/inspirational-photo.jpg"
)
