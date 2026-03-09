from dotenv import load_dotenv
load_dotenv()

import os
import gradio as gr

from brain_of_the_doctor import encode_image, analyze_image_with_query
from voice_of_the_patient import record_audio, transcribe_with_groq
from voice_of_the_doctor import text_to_speech_with_gtts, text_to_speech_with_elevenlabs

system_prompt="""You have to act as a professional doctor, i know you are not but this is for learning purpose. 
            What's in this image?. Do you find anything wrong with it medically? 
            If you make a differential, suggest some remedies for them. Donot add any numbers or special characters in 
            your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
            Donot say 'In the image I see' but say 'With what I see, I think you have ....'
            Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot, 
            Keep your answer concise (max 2 sentences). No preamble, start your answer right away please"""

custom_css = """
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

:root {
    --primary: #00f2ff;
    --primary-glow: rgba(0, 242, 255, 0.4);
    --secondary: #2dd4bf;
    --bg-dark: #020617;
    --bg-card: rgba(15, 23, 42, 0.7);
    --border: rgba(45, 212, 191, 0.2);
    --text: #f8fafc;
    --text-dim: #94a3b8;
}

body, .gradio-container {
    background: radial-gradient(circle at 50% 50%, #0f172a 0%, var(--bg-dark) 100%) !important;
    background-attachment: fixed !important;
    font-family: 'Space Grotesk', sans-serif !important;
    color: var(--text) !important;
}

/* Medical Grid Background Overlay */
.gradio-container::before {
    content: "";
    position: fixed;
    top: 0; left: 0; width: 100%; height: 100%;
    background-image: 
        linear-gradient(rgba(0, 242, 255, 0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0, 242, 255, 0.03) 1px, transparent 1px);
    background-size: 40px 40px;
    pointer-events: none;
    z-index: -1;
}

.gradio-container {
    max-width: 1100px !important;
    padding: 1rem 2rem !important;
}

.main-title {
    font-weight: 700 !important;
    font-size: 1.8rem !important;
    color: var(--primary) !important;
    text-align: center !important;
    margin: 0.5rem 0 0.5rem 0 !important;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    text-shadow: 0 0 10px var(--primary-glow);
    display: block;
    width: 100%;
}
#header-container {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
}

.block, .panel {
    background: var(--bg-card) !important;
    backdrop-filter: blur(16px) !important;
    border: 1px solid var(--border) !important;
    border-radius: 20px !important;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.8) !important;
    transition: all 0.3s ease !important;
}

.block:hover {
    border-color: var(--primary) !important;
    box-shadow: 0 0 20px rgba(0, 242, 255, 0.15) !important;
}

label span {
    color: var(--primary) !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.75rem !important;
    font-weight: 500 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.2em !important;
}

button.primary {
    background: linear-gradient(135deg, var(--bg-dark) 0%, #1e293b 100%) !important;
    color: var(--primary) !important;
    border: 1px solid var(--primary) !important;
    border-radius: 12px !important;
    font-weight: 600 !important;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    padding: 1rem 2rem !important;
    box-shadow: 0 0 15px var(--primary-glow) !important;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
}

button.primary:hover {
    background: var(--primary) !important;
    color: var(--bg-dark) !important;
    box-shadow: 0 0 30px var(--primary) !important;
    transform: translateY(-2px);
}

textarea, input[type="text"] {
    background: rgba(30, 41, 59, 0.5) !important;
    border: 1px solid var(--border) !important;
    color: var(--text) !important;
    font-family: 'JetBrains Mono', monospace !important;
    border-radius: 12px !important;
    padding: 12px !important;
}

textarea:focus, input[type="text"]:focus {
    border-color: var(--primary) !important;
    box-shadow: 0 0 10px var(--primary-glow) !important;
}

/* Dashboard UI Accents */
.futuristic-card {
    position: relative;
    overflow: hidden;
}

.futuristic-card::after {
    content: "";
    position: absolute;
    top: 0; right: 0;
    width: 40px; height: 40px;
    background: linear-gradient(225deg, var(--primary) 0%, transparent 50%);
    opacity: 0.5;
}
"""

def process_inputs(audio_filepath, image_filepath):
    try:
        # Guard: check audio is provided
        if not audio_filepath:
            return "Please record your voice first.", "No audio recorded.", None

        speech_to_text_output = transcribe_with_groq(
            GROQ_API_KEY=os.environ.get("GROQ_API_KEY"),
            audio_filepath=audio_filepath,
            stt_model="whisper-large-v3"
        )
        print(f"STT Output: {speech_to_text_output}")

        if image_filepath:
            print(f"Analyzing image at {image_filepath}...")
            doctor_response = analyze_image_with_query(
                query=system_prompt + speech_to_text_output,
                encoded_image=encode_image(image_filepath),
                model="meta-llama/llama-4-scout-17b-16e-instruct"
            )
        else:
            doctor_response = "No image provided for me to analyze"

        print(f"Doctor Response: {doctor_response}")

        voice_of_doctor = text_to_speech_with_elevenlabs(
            input_text=doctor_response,
            output_filepath="final.mp3"
        )

        return speech_to_text_output, doctor_response, voice_of_doctor
    except Exception as e:
        print(f"Error in process_inputs: {e}")
        return f"Error: {str(e)}", "An error occurred during processing.", None


with gr.Blocks(css=custom_css, title="AI Health Assistant | Neural Diagnosis") as iface:
    with gr.Row(elem_id="header-container"):
        gr.HTML("""
            <h1 class="main-title">
                <i class='fas fa-user-md'></i> 
                AI Health Voice & Vision Assistant
            </h1>
        """)

    with gr.Row():
        with gr.Column(scale=1):
            with gr.Group():
                gr.Markdown("### 🎙️ Audio Capture")
                audio_input = gr.Audio(sources=["microphone"], type="filepath", label="Patient Sync")
            
            with gr.Group():
                gr.Markdown("### 📷 Neural Scan")
                image_input = gr.Image(type="filepath", label="Diagnostic Target")
            
            submit_btn = gr.Button("INITIALIZE DIAGNOSIS", variant="primary")

        with gr.Column(scale=1):
            with gr.Group():
                gr.Markdown("### 📡 Neural Processing")
                text_output = gr.Textbox(label="Decoded Signal (STT)", interactive=False)
                response_output = gr.Textbox(label="Doctor's Analysis", interactive=False, lines=4)
            
            audio_output = gr.Audio(label="Voice Synthesis", type="filepath", autoplay=True)

    submit_btn.click(
        fn=process_inputs,
        inputs=[audio_input, image_input],
        outputs=[text_output, response_output, audio_output]
    )

iface.launch(debug=True)