import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from multi_threading import *
from divide import *

# original image
image = mpimg.imread('input1.jpg')
thread_num = number_of_threads(image)
original_copy = np.copy(image) # making a copy becase image is read only
chunks_originalImage = divide_image(original_copy, thread_num)

# gray-scale for applying sobel filter
gray_scale_image = rgb_to_grayscale(image)
plt.imsave('grayScale_output.jpg', gray_scale_image, cmap='gray')
chunks_grayScale = divide_image(gray_scale_image, thread_num)

menu = ['filters:',
        '1. edge detection by sobel filter',
        '2. oil painting filter',
        '3. negative filter',
        '4. exit']

for item in menu:
    print(item)

option = int(input("choose the filter:"))

if option == 1:
    multi_threading(chunks_grayScale, gray_scale_image, apply_sobel)
    result = threshold_image(gray_scale_image)
    plt.imsave('sobel_result.jpg', result, cmap='gray')
elif option == 2:
    multi_threading(chunks_originalImage, original_copy, apply_oil_painting)
    plt.imsave('oilPainting_result.jpg', original_copy)
elif option == 3:
    multi_threading(chunks_originalImage, original_copy, apply_negative)
    plt.imsave('negative_result.jpg', original_copy)
else:
    pass



