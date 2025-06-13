import numpy as np
from scipy.ndimage import convolve


def rgb_to_grayscale(image):
    grayscale_image = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])
    return grayscale_image


def apply_sobel(chunk, source_image, lock):
    start, end, _ = chunk

    sobel_x = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ])

    sobel_y = np.array([
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1]
    ])

    buffer_x = convolve(source_image[start:end, :], sobel_x, mode='reflect')
    buffer_y = convolve(source_image[start:end, :], sobel_y, mode='reflect')

    buffer = np.sqrt(buffer_x ** 2 + buffer_y ** 2)
    buffer = np.clip(buffer, 0, 255)

    lock.acquire()
    try:
        source_image[start:end, :] = buffer
    finally:
        lock.release()


def compute_gradient(image, x, y, kernel):
    kernel_size = kernel.shape[0] // 2
    sum = 0

    for i in range(-kernel_size, kernel_size + 1):
        for j in range(-kernel_size, kernel_size + 1):
            pixel_x = np.clip(x + j, 0, image.shape[1] - 1)
            pixel_y = np.clip(y + i, 0, image.shape[0] - 1)
            gray_value = image[pixel_y, pixel_x]
            sum += gray_value * kernel[i + kernel_size, j + kernel_size]

    return sum


def threshold_image(image_matrix):
    mean_value = np.mean(image_matrix)
    thresholded = np.where(image_matrix > mean_value, 0, 255).astype(np.uint8)
    return thresholded


def apply_oil_painting(chunk, source_image, lock, radius=5, intensity_levels=20):
    start, end, _ = chunk
    buffer = np.zeros_like(source_image[start:end])

    for y in range(start, end):
        for x in range(source_image.shape[1]):
            if y < radius or y >= source_image.shape[0] - radius or x < radius or x >= source_image.shape[1] - radius:
                buffer[y - start, x] = source_image[y, x]
                continue

            intensity_count = np.zeros(intensity_levels)
            average_color = np.zeros((intensity_levels, 3))

            for dy in range(-radius, radius + 1):
                for dx in range(-radius, radius + 1):
                    ny, nx = y + dy, x + dx
                    color = source_image[ny, nx]
                    intensity = int(np.sum(color) / 3 * (intensity_levels - 1) / 255)  # Fixed intensity calculation
                    intensity_count[intensity] += 1
                    average_color[intensity] += color

            most_frequent_intensity = np.argmax(intensity_count)
            buffer[y - start, x] = average_color[most_frequent_intensity] / intensity_count[most_frequent_intensity]

    lock.acquire()
    try:
        source_image[start:end, :] = buffer
    finally:
        lock.release()


def apply_warm_filter(chunk, source_image, lock):
    start, end, _ = chunk
    buffer = np.copy(source_image[start:end])

    warm_matrix = np.array([[1.1, 0.05, 0], [0, 1.1, 0], [0, 0, 0.9]])

    for y in range(start, end):
        for x in range(source_image.shape[1]):
            buffer[y - start, x] = np.clip(np.dot(warm_matrix, buffer[y - start, x]), 0, 255)

    lock.acquire()
    try:
        source_image[start:end, :] = buffer
    finally:
        lock.release()


def apply_negative(chunk, source_image, lock):
    start, end, _ = chunk
    buffer = np.copy(source_image[start:end])

    for y in range(start, end):
        for x in range(source_image.shape[1]):
            buffer[y - start, x] = 255 - source_image[y, x]

    lock.acquire()
    try:
        source_image[start:end, :] = buffer
    finally:
        lock.release()
