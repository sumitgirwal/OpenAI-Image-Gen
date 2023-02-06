from key import key
import datetime
from base64 import b64decode
import webbrowser
import openai
from openai.error import InvalidRequestError

def generate_image(prompt, num_image=1, size='512x512', output_format='url'):
    """
    params:
        prompt (str):
        num_image (int):
        size (str):
        output_format (str):
    """
    try:
        images = []
        response = openai.Image.create(
            prompt=prompt,
            n=num_image,
            size=size,
            response_format=output_format
        )
        if output_format=='url':
            for image in response['data']:
                images.append(image.url)
        elif output_format == 'b64_json':
            for image in response['data']:
                    images.append(image.b64_json)
        return {
                'created': datetime.datetime.fromtimestamp(response['created']), 
                'images': images
                }
    except InvalidRequestError as e:
        print(e)
    
# Main function
openai.api_key = key
SIZES = ('256x256', '512x512', '1024x1024')

# first image call
# get images as link
# response = generate_image('corgi with hats', num_image=2, size=SIZES[1])
# print(response['created'])
# images = response['images']
# for image in images:
#     webbrowser.open(image)


######################################################
# second image call
# Save the image in local as jpg file
gen_text = 'batman at night'
num_images = 2
size = SIZES[0]

# print(gen_text, num_images, size)
# calling functions
response = generate_image(gen_text, num_image=num_images, size=size, output_format='b64_json')

# getting result and saving in image as jpg
prefix = 'demo'
for indx, image in enumerate(response['images']):
    with open(f'{prefix}_{indx}.jpg', 'wb') as f:
        f.write(b64decode(image))

print("Succesfully Image Created!")