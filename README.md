# Python Video Player with Audio

## Motivation
While searching the internet, I couldn't find any implementation of a video player in Python that includes audio. This motivated me to develop this project. If you wish to contribute, feel free to email me at: **p.jain161202@gmail.com**.

## Features
- Record video and audio simultaneously.
- Combine video and audio into a synchronized output file.
- Save the final recording in 240p resolution by default.
- Adjustable `rate` and `chunk` settings in audio recording to handle synchronization issues.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure that `ffmpeg` is installed on your system. You can download it from [FFmpeg's official website](https://ffmpeg.org/).

## Usage

1. Run the main script:
   ```bash
   python main.py
   ```

2. Follow the prompts to:
   - Set a custom recording duration (optional).
   - Start and stop the recording manually using the video window (press 'Q' to stop).

3. The output video will be saved in the `recordings` folder with the following details:
   - Final video file in 240p resolution.
   - Statistics file (`stats.txt`) containing:
     - Duration of the recording.
     - Frame rate (FPS).
     - File size.

## Configuration
- **Video Resolution**: The video is saved at 240p (426x240) by default.
- **Audio Synchronization**: If the video and audio are not synchronized properly, experiment with the `rate` and `chunk` parameters in `AudioRecorder.py`.
  - `rate`: Sampling rate of the audio.
  - `chunk`: Number of audio frames per buffer.

## Code Structure

### main.py
Handles the overall recording process, including:
- Creating the recording directory.
- Managing video and audio recording.
- Combining video and audio using `ffmpeg`.

### AudioRecorder.py
Manages audio recording using the `pyaudio` library. Key parameters include:
- `rate`: Audio sampling rate (default: 25000).
- `chunk`: Buffer size for audio frames (default: 1024).

### VideoRecorder.py
Manages video recording using the `cv2` library. Key parameters include:
- `fps`: Frames per second (default: 25).
- `width` and `height`: Video resolution (default: 426x240).

## Contribution
Contributions are welcome! If you have ideas or improvements, please email me at **p.jain161202@gmail.com**.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
