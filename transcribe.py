import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import os
import threading
from pydub import AudioSegment
from vosk import Model, KaldiRecognizer
import wave
import json

def convert_to_wav(audio_path, output_directory):
    if not audio_path.lower().endswith('.wav'):
        output_path = os.path.join(output_directory, os.path.basename(audio_path).rsplit('.', 1)[0] + '.wav')
        audio = AudioSegment.from_file(audio_path, format=audio_path.split('.')[-1])
        audio.export(output_path, format="wav")
        return output_path
    else:
        return audio_path

def transcribe_audio_vosk(audio_path, model_path, callback):
    try:
        model = Model(model_path)
        with wave.open(audio_path, "rb") as wf:
            recognizer = KaldiRecognizer(model, wf.getframerate())
            full_transcription = ""
            while True:
                data = wf.readframes(4000)
                if len(data) == 0:
                    break
                if recognizer.AcceptWaveform(data):
                    part_result = json.loads(recognizer.Result())
                    full_transcription += part_result.get('text', '') + " "
            part_result = json.loads(recognizer.FinalResult())
            full_transcription += part_result.get('text', '')
        callback(full_transcription.strip())
    except Exception as e:
        messagebox.showerror("Error", f"Failed to transcribe audio. Error: {e}")

def update_transcription_text(transcription):
    transcription_text.configure(state='normal')
    transcription_text.delete(1.0, tk.END)
    transcription_text.insert(tk.END, transcription)
    transcription_text.configure(state='disabled')

def select_model_path():
    model_path_value = filedialog.askdirectory()
    if model_path_value:
        model_path.set(model_path_value)

def select_file():
    model_path_value = model_path.get()
    if not model_path_value or not os.path.exists(model_path_value):
        messagebox.showerror("Error", "Please select a valid Vosk model directory.")
        return
    
    file_path = filedialog.askopenfilename()
    if file_path:
        output_directory = None
        if not file_path.lower().endswith('.wav'):
            output_directory = filedialog.askdirectory(title="Select Output Directory for WAV Conversion")
            if not output_directory:
                messagebox.showerror("Error", "Output directory is required for non-WAV files.")
                return
            file_path = convert_to_wav(file_path, output_directory)

        # Transcription is run on a separate thread to keep GUI responsive
        threading.Thread(target=transcribe_audio_vosk, args=(file_path, model_path_value, update_transcription_text), daemon=True).start()

root = tk.Tk()
root.title("AudioDictate")

# Model path selection
model_path_frame = tk.Frame(root)
model_path_label = tk.Label(model_path_frame, text="Vosk Model Path:")
model_path_label.pack(side=tk.LEFT, padx=(0, 10))
model_path = tk.StringVar()
model_path_entry = tk.Entry(model_path_frame, textvariable=model_path, width=50)
model_path_entry.pack(side=tk.LEFT, expand=True, fill=tk.X)
model_path_button = tk.Button(model_path_frame, text="Select", command=select_model_path)
model_path_button.pack(side=tk.LEFT)
model_path_frame.pack(pady=5, padx=5, fill=tk.X)

# Transcription display area
transcription_frame = tk.LabelFrame(root, text="Transcription")
transcription_text = scrolledtext.ScrolledText(transcription_frame, width=60, height=15, state='disabled')
transcription_text.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
transcription_frame.pack(pady=10, padx=5, fill=tk.BOTH, expand=True)

# Button to select file
select_file_button = tk.Button(root, text="Select Audio File", command=select_file)
select_file_button.pack(pady=5)

root.mainloop()
