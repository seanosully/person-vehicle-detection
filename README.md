# person-vehicle-detection
Python program that implements a person and vehicle detection model through Clarifai's API. It also allows for SMS requests to take a snapshot of the current environment and return a text of the number of vehicles / people using the TextMagic API
Originally built as an easy way to find out how many cars are in a driveway at any given time. For this reason the detection model only detects people and vehicles, however, Clarifai offers many other visual classifiers that can be used instead as well as a custom model.

# SMS capabilities
This program uses TextMagic API which costs money although they do offer free credits for new accounts.
A phone number will be created when you create a new account. This number will be used to request the concept and to send you back a response.

# Dependencies
TextMagic -> pip install git+https://github.com/textmagic/textmagic-rest-python-v2.git@v2.0.3361
opencv -> pip install opencv-python
clarifai -> pip install -U clarifai

# How To Run
python3 main.py <sms|nosms>
