import TextMagic
from TextMagic.rest import ApiException
import time
import app
import cam
import send_sms

configuration = TextMagic.Configuration()

# put your Username and API Key from https://my.textmagic.com/online/api/rest-api/keys page.
configuration.username = "INSERT_USERNAME"
configuration.password = "INSERT_API_KEY"

api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
def run():
    print("running...")
    print("ready to recieve text message. Check Text Magic account to find phone number")
    print()
    print("note: only text the concept you are looking for. Ex 'vehicle' or 'person' ")
    while True:
        while True:
            try:
                # Get all inbound messages
                result = api_instance.get_all_inbound_messages()

                # Check if any messages were received
                if result.resources:
                    for message in result.resources:
                        concept = message.text
                        sender = message.sender
                        print("Received message:")
                        print(f"From: {message.sender}")
                        print(f"Text: {message.text}")
                        print("\n")
                        api_instance.delete_inbound_message(message.id)
                    break  # Exit the loop once a message is received

            except ApiException as e:
                print("Exception when calling TextMagicApi->get_all_inbound_messages: %s\n" % e)

            # Wait before checking again
            time.sleep(10)  # Adjust the interval as needed

        print("Message received!")
        cam.get_image("snapshot.png")
        concepts = app.run_model(concept, "snapshot.png")
        concept_name = concept + "s."
        message = "There are currently " +  str(len(concepts)) + " " + concept_name
        send_sms.send_message(sender, message)
