from filters import *


def number_of_threads(image):
    height, width, _ = image.shape
    image_size = height * width

    if image_size < 1e6:
        return 9
    elif image_size < 5e6:
        return 16
    else:
        return 25


def divide_image(image, num_chunks):
    height = image.shape[0]
    part_size = int(np.ceil(height / num_chunks))
    chunks = []

    for i in range(num_chunks):
        start = i * part_size
        end = min((i + 1) * part_size, height)
        chunks.append((start, end, image))

    return chunks
