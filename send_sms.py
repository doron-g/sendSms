from twilio.rest import Client

client = Client()
message = client.messages \
                .create(
                     body="אני לא מרגיש תפה שלי",
                     from_='+12058430768',
                     to='+972546735285'
                 )

print(message.sid)
