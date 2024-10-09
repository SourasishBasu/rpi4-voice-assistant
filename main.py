import streamlit as st
import sounddevice as sd
import wavio
import os
import google.generativeai as palm
import pathlib

# Constants
RECORDING_FILE = "test.mp3"
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

# Initialize Palm (Gemini 1.5) client
palm.configure(api_key=GEMINI_API_KEY)
model = palm.GenerativeModel(model_name="gemini-1.5-flash")


def record_audio(duration=5, sample_rate=44100):
    """Record audio for a fixed duration and save it to a .mp3 file"""
    st.write(f"Recording for {duration} seconds...")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
    sd.wait()  # Wait for the recording to finish
    wavio.write(RECORDING_FILE, recording, sample_rate, sampwidth=2)
    st.success("Recording complete!")


def transcribe_with_gemini(audio):
    """Send the audio file to Gemini 1.5 model to transcribe it"""
    st.write("Transcribing the audio file with Gemini...")

    response = model.generate_content([
        "Please transcribe this recording:",
        {
            "mime_type": "audio/mp3",
            "data": pathlib.Path('test.mp3').read_bytes()
        }
    ])
    if response:
        return response.text
    return None


def get_gemini_answer(transcript):
    """Send the transcription to Gemini to get an answer"""
    st.write("Sending transcription to Gemini for response...")
    response = model.generate_content(transcript)
    if response:
        return response.text
    return "Sorry, no answer was generated."


# Streamlit UI
st.title("Voice Input App")

# Buttons to start and stop recording
if st.button("Start Recording"):
    record_audio()

if st.button("Stop Recording"):
    if os.path.exists(RECORDING_FILE):
        # Send the recording to Gemini for transcription
        transcription = transcribe_with_gemini(RECORDING_FILE)
        if transcription:
            st.write(f"Transcription: {transcription}")

            # Send transcription to Gemini as a question
            answer = get_gemini_answer(transcription)
            st.write(f"Answer: {answer}")
        else:
            st.error("Could not transcribe the audio.")
    else:
        st.error("No audio file found. Please record again.")
