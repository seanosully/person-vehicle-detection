
import sys
from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_code_pb2

# Your PAT (Personal Access Token) can be found in the portal under Authentification
PAT = 'INSERT PAT HERE'

# Specify the correct user_id/app_id pairings
USER_ID = 'clarifai'
APP_ID = 'main'

# Change these to the model details you want to use
MODEL_ID = 'person-vehicle-detection-yolov5'
MODEL_VERSION_ID = '05845a4f7c534cd78243224a93e4178c'


def run_model(desired_concept, IMAGE_PATH):

    # Read the image data from the file
    with open(IMAGE_PATH, 'rb') as image_file:
        image_data = image_file.read()

    # Set up the connection to the Clarifai API
    channel = ClarifaiChannel.get_grpc_channel()
    stub = service_pb2_grpc.V2Stub(channel)

    metadata = (('authorization', 'Key ' + PAT),)

    userDataObject = resources_pb2.UserAppIDSet(user_id=USER_ID, app_id=APP_ID)

    # Prepare and send the request to the Clarifai API
    post_model_outputs_response = stub.PostModelOutputs(
        service_pb2.PostModelOutputsRequest(
            user_app_id=userDataObject,
            model_id=MODEL_ID,
            version_id=MODEL_VERSION_ID,
            inputs=[
                resources_pb2.Input(
                    data=resources_pb2.Data(
                        image=resources_pb2.Image(
                            base64=image_data
                        )
                    )
                )
            ]
        ),
        metadata=metadata
    )

    # Handle the response
    if post_model_outputs_response.status.code != status_code_pb2.SUCCESS:
        print(post_model_outputs_response.status)
        raise Exception("Post model outputs failed, status: " + post_model_outputs_response.status.description)

    # Since we have one input, one output will exist here
    output = post_model_outputs_response.outputs[0]

    vehicles = list()
    for region in output.data.regions:
        concepts = region.data.concepts
        for concept in concepts:
            if concept.name == desired_concept and concept.value > 0.8:
                vehicles.append(concept)

    #print(vehicles)
    print("There are currently", len(vehicles), str(desired_concept+ "s."))
    return vehicles

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python app.py concept image_path")
    else:
        run_model(sys.argv[1], sys.argv[2])
