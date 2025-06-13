import threading


def process_chunk(chunk, target, lock, filter_func, **kwargs):
    filter_func(chunk, target, lock, **kwargs)


def multi_threading(chunks, grayscale_image, filter_func):
    threads = []
    lock = threading.Lock()
    for chunk in chunks:
        thread = threading.Thread(target=process_chunk, args=(chunk, grayscale_image, lock, filter_func))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
