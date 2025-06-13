# Multithreaded Image‑Processing

## Overview
The goal of this project is to develop a multithreaded image‑processing application that can apply filters to large images efficiently. The application divides an image into sub‑matrices, processes each part in parallel using multiple threads, and then reassembles the processed sub‑matrices into the final image. This approach leverages multithreading to improve the performance of image‑processing tasks.

### Objectives
1. **Load an image** – Read a single copy of the image into memory in the main thread; worker threads treat it as a shared resource.
2. **Divide the image** – Split the image into smaller, manageable sub‑matrices (chunks) and assign a specific range of the main matrix to each worker thread.
3. **Apply filters** – Implement various filters; each thread writes its results into its own matrix for its pixel range.
4. **Multithreading** – Process chunks in parallel using at least nine threads, chosen dynamically based on image size.
5. **Synchronization** – Without cloning the whole matrix, threads modify the shared image safely, ensuring neighbouring chunks don’t overwrite each other’s border pixels.
6. **Reassemble and save** – Merge all processed chunks back into a single image and write it to disk.

<p align="center">
  <img src="assets/demo.jpg" alt="Demo: original vs. filtered output" width="80%"/>
</p>

## Features
- **Sobel edge‑detection** – 3 × 3 Sobel kernels highlight horizontal and vertical edges (`apply_sobel`).
- **Grayscale conversion** – luminance transform via `rgb_to_grayscale` for downstream filters.
- **Mean thresholding** – converts to high‑contrast black‑and‑white using the global mean (`threshold_image`).
- **Oil‑painting effect** – radius / intensity‑based stylisation that mimics brush strokes (`apply_oil_painting`).
- **Warm tone filter** – boosts reds and greens for a cosy film vibe (`apply_warm_filter`).
- **Negative filter** – inverts colours to produce an x‑ray look (`apply_negative`).
- **Automatic chunking & thread pooling** – `divide_image` splits the frame; `number_of_threads` scales from 9 → 25 threads depending on resolution.
- **Thread‑safe in‑place writes** – a shared `threading.Lock` ensures each worker writes its stripe without data races or extra memory.
- **Pluggable architecture** – add new effects by writing a `filter_func(chunk, source_image, lock, **kwargs)` and passing it to `multi_threading`.
