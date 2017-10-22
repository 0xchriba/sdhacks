import os
from twilio.rest import Client

account_sid = "ACdef508d68369a117ef857740bf362603"
auth_token = "96e589688a8b066654d718a105170a44"
client = Client(account_sid, auth_token)
message = client.messages.create(
    "+14158230463",
    # "+14155199133",
    body='hello',
    from_="+14159004260",
)
