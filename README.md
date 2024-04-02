
# AudioDictate

AudioDictate is an intuitive desktop application designed to transcribe audio content with high accuracy. It offers offline functionality for the transcription of WAV audio files, including the conversion of non-WAV formats into WAV. Featuring a straightforward graphical user interface, it provides a seamless experience for users to convert spoken language into text.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup and Installation](#setup-and-installation)
- [Running the Application](#running-the-application)
- [How to Use](#how-to-use)
- [Tools and Technologies](#tools-and-technologies)
- [License](#license)
- [Contact](#contact)

## Features

- **Audio File Transcription**: Converts spoken words from audio files into written text.
- **WAV File Conversion**: Automatically converts non-WAV files to WAV format for processing.
- **Offline Functionality**: No internet connection required, ensuring data privacy and security.
- **Drag-and-Drop Interface**: Simple drag-and-drop feature for easy file submission.
- **Interactive GUI**: Provides a user-friendly interface for all interactions with the application.

## Prerequisites

- Python 3.x
- Tkinter
- PyDub
- Vosk Speech Recognition Toolkit

## Setup and Installation

### Clone the Repository

```bash
git clone https://github.com/ascender1729/AudioDictate.git
cd AudioDictate
```

### Environment Setup

Create and activate a virtual environment:

```bash
python -m venv myenv
.\myenv\Scripts\Activate.ps1  # On Windows
source myenv/bin/activate  # On Unix or MacOS
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Download Vosk Model

Download the Vosk model appropriate for your language and note the directory path where it is saved.

## Running the Application

```bash
python transcribe.py
```

### Shutting Down

When you are finished using AudioDictate, you can deactivate the virtual environment:

```bash
deactivate
```

## How to Use

1. Start AudioDictate.
2. Input the Vosk model directory when prompted.
3. Use the file dialog to select your audio file or drag and drop it into the application window.
4. If the file is not a WAV file, choose an output directory for the conversion.
5. The transcribed text will be displayed within the application window.

## Tools and Technologies

<table>
  <tr>
    <th>Area</th>
    <th>Tool/Technology</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Audio Processing</td>
    <td>PyDub</td>
    <td>Handles the audio file format conversion.</td>
  </tr>
  <tr>
    <td>Speech Recognition</td>
    <td>Vosk</td>
    <td>Performs the speech-to-text transcription.</td>
  </tr>
  <tr>
    <td>GUI</td>
    <td>Tkinter</td>
    <td>Provides the graphical user interface for the application.</td>
  </tr>
  <tr>
    <td>Programming Language</td>
    <td>Python</td>
    <td>The core language used for developing the application.</td>
  </tr>
</table>

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Pavan Kumar - pavankumard.pg19.ma@nitp.ac.in

LinkedIn: [linkedin.com/in/im-pavankumar](https://www.linkedin.com/in/im-pavankumar/)

Project Link: [AudioDictate](https://github.com/ascender1729/AudioDictate)