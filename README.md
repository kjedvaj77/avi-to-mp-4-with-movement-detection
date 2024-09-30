# avi_to_mp4

This project contains two Python programs that help you work with `.avi` and `.mp4` video files. The first program converts multiple `.avi` files into one `.mp4` video, while the second detects movement in a video and saves the movement segments as separate clips.

### `converter.py`
This script takes multiple `.avi` files from the folder `avivideos` (or a folder path you specify in the script), concatenates them, and outputs a single `.mp4` in the root directory.

### `extractmovement.py`
This script takes the `output.mp4` file from the root directory, detects movement, and saves each detected movement segment as a separate `.mp4` file in the `movement_clips` folder.

## Prerequisites

Before running these programs, make sure you have the following installed:

1. **Python 3.x**
2. **MoviePy** (for video manipulation)
3. **OpenCV** (for movement detection)
4. **FFmpeg** (for encoding `.mp4` files, which is required by MoviePy)

You can install the necessary Python packages using pip and the provided `requirements.txt` file.

### Setting Up

1. **Clone the repository**:
    ```bash
    git clone https://github.com/kjedvaj77/avi-to-mp-4-with-movement-detection.git
    cd avi-to-mp-4-with-movement-detection
    ```

2. **(Optional) Create a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    # or
    venv\Scripts\activate  # On Windows
    ```

3. **Install dependencies**:
    ```bash
    pip3 install -r requirements.txt
    ```

### Running the Programs

1. **Convert `.avi` files to `.mp4`**:
   - Place your `.avi` files in the `avivideos` folder (or specify another folder path in the script).
   - Run the `converter.py` script:
     ```bash
     python3 converter.py
     ```

   The output will be saved as `output.mp4` in the root directory.

2. **Extract movement segments**:
   - Run the `extractmovement.py` script to detect movement in the `output.mp4` file and save clips to the `movement_clips` folder:
     ```bash
     python3 extractmovement.py
     ```