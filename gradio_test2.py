import gradio as gr

def video_identity(video):
    #  ここで video を加工する
    return video

demo = gr.Interface(video_identity,
                    gr.Video(),
                    "playable_video",
                    )

if __name__ == "__main__":
    demo.launch()