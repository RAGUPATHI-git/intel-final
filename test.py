# import requests

# API_URL = "https://api-inference.huggingface.co/models/renderartist/simplevectorflux"
# headers = {"Authorization": "Bearer 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"}

# def query(payload):
# 	response = requests.post(API_URL, headers=headers, json=payload)
# 	return response.content
# image_bytes = query({
# 	"inputs": "Astronaut riding a horse",
# })
# # You can access the image with PIL.Image for example
# import io
# from PIL import Image
# image = Image.open(io.BytesIO(image_bytes))
# image.save('./static/images/saved/img.png')
# print("img saved")



import datetime

print(datetime.datetime.today())

id = str(datetime.datetime.today()).replace(":", '').replace(' ','').replace('-','').replace('.','')
print(id)