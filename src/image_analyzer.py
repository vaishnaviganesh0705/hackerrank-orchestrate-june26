from PIL import Image
import pillow_avif

def analyze_image(image_path):

    img = Image.open(image_path)

    width, height = img.size

    valid_image = True

    if width < 200 or height < 200:
        valid_image = False

    return {
        "valid_image": valid_image,
        "width": width,
        "height": height
    }