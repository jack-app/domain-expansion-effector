import gradio as gr
from gradio_webrtc import WebRTC
import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False,
                       max_num_hands=2,
                       min_detection_confidence=0.5,
                       min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

def video_identity(video):
    print(video)
    # #  ここで video を加工する
    # cap = cv2.VideoCapture(video)
    # while cap.isOpened():
    #     ret, frame = cap.read()
    #     if not ret:
    #         print("カメラから映像を取得できませんでした。")
    #         break

    #     image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #     results = hands.process(image)
    #     image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    #     if results.multi_hand_landmarks:
    #         for hand_landmarks in results.multi_hand_landmarks:
    #             # ランドマークを描画
    #             mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    #     return image

demo = gr.Interface(video_identity,
                    gr.Video(),
                    "playable_video",
                    )

if __name__ == "__main__":
    demo.launch()