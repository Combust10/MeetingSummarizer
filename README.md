# Meeting Summarizer

This Meeting Summarizer is a Python-based application that allows users to record meetings, transcribe the audio, and generate a summary of the conversation. The application provides a user-friendly GUI for easy interaction and supports both audio and text file inputs.

## Features

- **Real-Time Audio Recording**: Record audio directly from your microphone.
- **Speech-to-Text Transcription**: Convert recorded audio into text using AssemblyAI's transcription service.
- **Text Summarization**: Generate concise summaries of the transcribed text using a pre-trained NLP model.
- **File Upload**: Upload existing audio or text files for transcription and summarization.
- **User-Friendly GUI**: Built with `customtkinter` for a modern and intuitive user interface.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.7 or higher
- `pyaudio` (for audio recording)
- `customtkinter` (for the GUI)
- `transformers` (for text summarization)
- `nltk` (for text tokenization)
- `PIL` (for image handling)
- `requests` (for API calls)

You can install the required Python packages using pip:

```bash
pip install pyaudio customtkinter transformers nltk pillow requests
```
## Setup
### Clone the Repository:
```bash
git clone https://github.com/Combust10/MeetingSummarizer.git
cd MeetingSummarizer
```

### Obtain an AssemblyAI API Key:

- Sign up for an account at AssemblyAI.
- Obtain your API key from the dashboard.
- Set the API key as an environment variable or pass it as a command-line argument when running the application.
```bash
export AAI_API_KEY="your-api-key-here"
```
### Run the Application:
Start the application by running the main.py script:

```bash
python main.py
```

## Usage

1. **Start a Meeting**:
   - Click the microphone button to start recording the meeting.
   - Click the button again to stop recording and begin the transcription process.

2. **Upload a File**:
   - Use the "Upload File" option to upload an existing audio or text file.
   - Select the file type (audio or text) using the radio buttons.

3. **Generate Summary**:
   - After transcription, click the "Summarize" button to generate a summary of the transcribed text.

## Project Structure

- `gui.py`: Contains the GUI implementation using `customtkinter`.
- `main.py`: The main script that launches the GUI.
- `Rec.py`: Handles audio recording and transcription.
- `sumpart.py`: Implements text summarization using a pre-trained model.
- `transcribe.py`: Manages the transcription process using AssemblyAI's API.
- `utils.py`: Contains helper functions for API requests and file handling.
