import cv2
import gradio as gr

def process_frame():
    cap = cv2.VideoCapture(0)  # カメラを開く（0 はデフォルトカメラ）

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # グレースケール変換
        yield frame  # 画像をリアルタイムで送信

    cap.release()

# Gradio インターフェース
with gr.Blocks() as demo:
    gr.Markdown("## リアルタイムカメラ処理")
    video_output = gr.Image(label="Processed Video", streaming=True)
    demo.load(process_frame, inputs=None, outputs=video_output)

demo.launch()

