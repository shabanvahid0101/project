from rembg import remove
from PIL import Image
# image address
image_file=''
# remove background image adress
image_converted=''
inserted_image=Image.open(image_file)
output=remove(inserted_image)
output.save(image_converted)