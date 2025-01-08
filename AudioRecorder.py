import pyaudio
import wave


class AudioRecorder:
    def __init__(self, output_path, channels=1, rate=25000, chunk=1024):
        self.output_path = output_path
        self.channels = channels
        self.rate = rate
        self.chunk = chunk
        self.frames = []
        self.is_recording = False

    def start_recording(self):
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(
            format=pyaudio.paInt16,
            channels=self.channels,
            rate=self.rate,
            input=True,
            frames_per_buffer=self.chunk
        )
        self.is_recording = True

    def stop_recording(self):
        self.is_recording = False
        if hasattr(self, 'stream'):
            self.stream.stop_stream()
            self.stream.close()
        if hasattr(self, 'audio'):
            self.audio.terminate()

        with wave.open(self.output_path, 'wb') as wf:
            wf.setnchannels(self.channels)
            wf.setsampwidth(self.audio.get_sample_size(pyaudio.paInt16))
            wf.setframerate(self.rate)
            wf.writeframes(b''.join(self.frames))

    def record_chunk(self):
        if self.is_recording:
            data = self.stream.read(self.chunk)
            self.frames.append(data)