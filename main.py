import os
import time
from datetime import datetime
import subprocess
import cv2
from VideoRecorder import VideoRecorder
from AudioRecorder import AudioRecorder


def create_recording_directory():
    base_dir = './recordings'
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    recording_dir = os.path.join(base_dir, f'recording_{timestamp}')
    os.makedirs(recording_dir, exist_ok=True)
    return recording_dir


def record_video_with_audio(recording_dir, duration=None):
    video_path = os.path.join(recording_dir, 'temp_video.mp4')
    audio_path = os.path.join(recording_dir, 'temp_audio.wav')
    final_path = os.path.join(recording_dir, 'final_recording.mp4')
    stats_path = os.path.join(recording_dir, 'stats.txt')

    video_recorder = VideoRecorder(video_path)
    audio_recorder = AudioRecorder(audio_path)

    try:
        video_recorder.start_recording()
        audio_recorder.start_recording()

        start_time = time.time()
        frames_captured = 0

        print("Recording started... Press 'Q' in the video window to stop")

        while video_recorder.is_recording and audio_recorder.is_recording:
            elapsed_time = time.time() - start_time
            if duration and elapsed_time >= duration:
                break
            if not video_recorder.record_frame():
                break
            audio_recorder.record_chunk()
            frames_captured += 1

    finally:
        video_recorder.stop_recording()
        audio_recorder.stop_recording()
        cv2.destroyAllWindows()

    actual_duration = time.time() - start_time
    actual_fps = frames_captured / actual_duration
    print(f"\nActual FPS: {actual_fps:.2f}")

    if os.path.exists(video_path) and os.path.exists(audio_path):
        try:
            cmd = [
                'ffmpeg', '-i', video_path, '-i', audio_path,
                '-r', f"{actual_fps}", '-c:v', 'copy', '-c:a', 'aac',
                '-strict', 'experimental', '-map', '0:v:0', '-map', '1:a:0',
                '-shortest', final_path
            ]
            subprocess.run(cmd, check=True, capture_output=True)
            os.remove(video_path)
            os.remove(audio_path)

            file_size = os.path.getsize(final_path) / (1024 * 1024)
            stats = (
                f"Final video saved to: {final_path}\n"
                f"Resolution: 240p (426x240)\n"
                f"Duration: {actual_duration:.1f} seconds\n"
                f"Total frames: {frames_captured}\n"
                f"File size: {file_size:.2f} MB\n"
            )

            with open(stats_path, 'w') as stats_file:
                stats_file.write(stats)

            print(stats)
            return final_path

        except subprocess.CalledProcessError as e:
            print(f"Error combining video and audio: {e}")
            return None
    return None


def main():
    recording_dir = create_recording_directory()
    use_duration = input("Do you want to set a recording duration? (y/n): ").lower() == 'y'
    duration = None

    if use_duration:
        while True:
            try:
                duration = float(input("Enter recording duration in seconds: "))
                if duration > 0:
                    break
                print("Please enter a positive number")
            except ValueError:
                print("Please enter a valid number")

    final_video = record_video_with_audio(recording_dir, duration)
    if final_video:
        print("\nRecording saved successfully!")
    else:
        print("\nRecording failed!")


if __name__ == "__main__":
    main()