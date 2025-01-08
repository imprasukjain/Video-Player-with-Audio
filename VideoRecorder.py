import cv2


class VideoRecorder:
    def __init__(self, output_path, fps=25):
        self.output_path = output_path
        self.fps = fps
        self.width = 426
        self.height = 240
        self.cap = None
        self.out = None
        self.is_recording = False

    def start_recording(self):
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            raise RuntimeError("Could not open webcam")

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self.out = cv2.VideoWriter(
            self.output_path,
            fourcc,
            self.fps,
            (self.width, self.height)
        )
        self.is_recording = True

    def stop_recording(self):
        self.is_recording = False
        if self.cap:
            self.cap.release()
        if self.out:
            self.out.release()

    def record_frame(self):
        ret, frame = self.cap.read()
        if ret:
            resized_frame = cv2.resize(frame, (self.width, self.height), interpolation=cv2.INTER_AREA)
            self.out.write(resized_frame)
            cv2.imshow('Recording... (Press Q to stop)', resized_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                return False
            return True
        return False