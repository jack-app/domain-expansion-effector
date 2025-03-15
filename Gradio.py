import gradio as gr
import cv2
from gradio_webrtc import WebRTC
from app import main

def detection(image):
    image = cv2.resize(image)
    debug_image = main((True, image))
    return cv2.resize(debug_image, (500, 500))

css = """.my-group {max-width: 600px !important; max-height: 600 !important;}
                      .my-column {display: flex !important; justify-content: center !important; align-items: center !important};"""

with gr.Blocks(css=css) as demo:
   
    with gr.Column(elem_classes=["my-column"]):
        with gr.Group(elem_classes=["my-group"]):
            image = WebRTC(label="Stream")
            conf_threshold = gr.Slider(
                label="Confidence Threshold",
                minimum=0.0,
                maximum=1.0,
                step=0.05,
                value=0.30,
            )

        image.stream(
            fn=detection, inputs=[image, conf_threshold], outputs=[image], time_limit=20
        )

if __name__ == "__main__":
    demo.launch()

