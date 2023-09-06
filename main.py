import sys
import recieve_sms
import app
import cam

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 app.py <sms/nosms>")
    if sys.argv[1] == "sms":
        recieve_sms.run()
    if sys.argv[1] == "nosms":
        concept = input("Enter concept to search for: ")
        IMAGE_PATH = input("Enter image file path (or '0' to take a picture): ")
        if IMAGE_PATH == '0':
            cam.get_image("snapshot.png")
            IMAGE_PATH = "snapshot.png"
        app.run_model(concept, IMAGE_PATH)
    else:
        print("Arg must be sms or nosms")

if __name__ == "__main__":
    main()