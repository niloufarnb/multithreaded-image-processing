# Multithreaded Image-Processing

> **Efficient, scalable image-processing CLI that applies CPU-bound filters (Sobel edge-detection, grayscale & adaptive threshold)** to large images using Python’s `concurrent.futures`.

<p align="center">
  <img src="assets/demo.png" alt="Demo: original vs. Sobel-filtered output" width="80%"/>
</p>

[![MIT license](https://img.shields.io/github/license/YOUR_USER/multithreaded-image-processing?style=flat)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/downloads/)
[![CI](https://img.shields.io/github/actions/workflow/status/YOUR_USER/multithreaded-image-processing/ci.yml?label=tests)](../../actions)

---

## ✨ Features

| Capability | Details |
|------------|---------|
| **Sobel edge-detection** | Highlights horizontal & vertical edges (configurable kernel size). |
| **Grayscale conversion** | Fast luminance transform via NumPy. |
| **Adaptive thresholding** | Converts to binary image using global or local mean. |
| **Multithreaded tiling** | Splits huge images into tiles processed in parallel via `ThreadPoolExecutor` or `ProcessPoolExecutor` to bypass the GIL for heavy NumPy ops. |
| **Batch mode** | Point it at a folder; it processes everything inside. |
| **CLI & API** | Use from the terminal **or** import as a library. |

---


### CLI flags

```
--filter {sobel,grayscale,threshold,all}   Filter(s) to apply
--workers N                                Number of worker threads/processes (default: CPU cores)
--tile-size PxP                            Split image into P×P pixel tiles (default: 512)
--threshold VAL                            Fixed threshold value (0-255) or "auto"
```

---

### 🔖 Topics
```
multithreading  image-processing  sobel  edge-detection  parallel-computing  python  cli
