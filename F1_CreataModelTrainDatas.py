import cv2
import time
import pyautogui
import numpy as np
from pathlib import Path


class TrainModel:
    def __init__(self):
        self.rootpath = Path(__file__).parent
        self.frameWidth = 1920
        self.frameHeight = 1080
        self.cap = cv2.VideoCapture("train_videos/Kart_BS_n.MP4")

    def play_video(self):
        _, self.frame = self.cap.read()
        frame = cv2.resize(self.frame, (self.frameWidth, self.frameHeight), interpolation=cv2.INTER_LINEAR)
        return frame

    @staticmethod
    def video_for_train_datas():
        train_model = TrainModel()
        print("-" * 50, "Infos", "-" * 50)
        print("Drücke 'p' für screenshots wenn ein anderes Kart zusehen ist")
        print("Drücke 'n' für screenshots wenn ein KEIN anders Kart zusehen ist")
        print("je mehr screenshots gemacht werden um so besser wird das Modell trainiert")
        print("Drücke 'q' zum beenden")
        print("-" * 100)
        while True:
            screenshot = pyautogui.screenshot()
            screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
            cv2.imshow("org", train_model.play_video())
            key = cv2.waitKey(1)
            if key == ord("q"):
                break
            elif key == ord("p"):
                cv2.imwrite(rf"{train_model.rootpath}\p\positiv_{time.time()}.jpg", screenshot)
            elif key == ord("n"):
                cv2.imwrite(rf"{train_model.rootpath}\n\negative_{time.time()}.jpg", screenshot)


if __name__ == "__main__":
    TrainModel.video_for_train_datas()
