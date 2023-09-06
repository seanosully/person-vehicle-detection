# How to install SDK see here https://docs.textmagic.com/#section/Python
import TextMagic
from TextMagic.rest import ApiException

def send_message(number, message):
    configuration = TextMagic.Configuration()
    # put your Username and API Key from https://my.textmagic.com/online/api/rest-api/keys page.
    configuration.username = "INSERT_USERNAME"
    configuration.password = "INSERT_API_KEY"

    # create an instance of the API class
    api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))

    input = TextMagic.SendMessageInputObject()

    # Required parameters
    input.text = message
    input.phones = number
    # Optional parameters, you can skip them


    try:
        # SendMessageResponse object
        result = api_instance.send_message(send_message_input_object=input)
        print("message sent successfully to ", number)
        # ...
    except ApiException as e:
        print("Exception when calling TextMagicApi->send_message: %s\n" % e)
