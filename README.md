# rpi4-voice-assistant
> Streamlit based webapp for voice based interaction with Gemini 1.5 Flash model.

### Libraries Used
- `google.generativeai` - LLM for prompt-response
- `sounddevice`, `wavio` - Manipulating voice recording
- `streamlit` - UI

## Setup for Local Development

- Install/Check for Python v3.11+.
  ```bash
  python -V
  Python 3.12.3
  ```
- Clone the repository and change directory.
  ```bash
  git clone https://github.com/SourasishBasu/rpi4-voice-assistant.git
  cd rpi4-voice-assistant
  ```
- Create a virtual environment and install the necessary packages.
  ```bash
  python -m venv venv
  ./venv/Scripts/activate
  pip install requirements.txt
  ```
- Make changes in `main.py` and launch the webapp UI
  ```bash
  streamlit run main.py
  ```
- Visit http://localhost:8501.

## Usage (with Docker)

- Install Docker.
- Pull the app image and run with Docker.
  ```bash
  docker pull sasquatch06/vink_project:latest
  docker run -p 8501:8501 -e GEMINI_API_KEY=<insert-api-key-here> --device /dev/snd -d sasquatch06/vink_project:latest
  ```
- Visit http://localhost:8501 to view the Streamlit Dashboard for interacting with the webapp.