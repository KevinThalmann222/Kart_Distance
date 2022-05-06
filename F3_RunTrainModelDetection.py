import cv2
import cvzone
from pathlib import Path


class Kart_detection:
    def __init__(self, video):
        self.rootpath = Path(__file__).parent
        self.video = video
        self.cap = cv2.VideoCapture(self.video)
        self.frameWidth = 1920
        self.frameHeight = 1080
        self.kart_detection = cv2.CascadeClassifier("cascade/cascade.xml")
        self.playing = True

    def play(self):
        while self.playing:
            self.playing, self.frame = self.cap.read()
            if not self.playing:
                break
            frame = cv2.resize(self.frame, (self.frameWidth, self.frameHeight), interpolation=cv2.INTER_LINEAR)
            detected_kart = self.kart_detection.detectMultiScale(frame)

            for (x, y, w, h) in detected_kart:
                cvzone.cornerRect(frame, (x, y, w, h), rt=1, l=30, t=5, colorR=(255, 0, 255), colorC=(0, 255, 0))
                cv2.putText(frame, "ENEMY", (x + 10, y + 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)
                w = (x + w) - x
                W = 1.2  # Kartbreite ca.1.2
                f = 320  # Appikationswert
                d = round((W * f) / w, 2)  # Formel

                cv2.putText(frame, f"DISTANCE: {d}m", (x + h - 220, y + w - 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)
                cv2.imshow("org", frame)

            if cv2.waitKey(1) == ord("q"):
                break


if __name__ == "__main__":
    kart = Kart_detection(video="train_videos/Kart_BS_p.mp4")
    kart.play()
