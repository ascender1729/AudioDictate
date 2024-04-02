
# AudioDictate

AudioDictate is an intuitive desktop application designed to transcribe audio content with high accuracy. It offers offline functionality for the transcription of WAV audio files, including the conversion of non-WAV formats into WAV. Featuring a straightforward graphical user interface, it provides a seamless experience for users to convert spoken language into text.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup and Installation](#setup-and-installation)
- [Running the Application](#running-the-application)
- [How to Use](#how-to-use)
- [Tools and Technologies](#tools-and-technologies)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Audio File Transcription**: Converts spoken words from audio files into written text with high accuracy.
- **WAV File Conversion**: Automatically converts non-WAV files to WAV format for processing.
- **Offline Functionality**: Processes audio files offline, ensuring data privacy and security.
- **Interactive GUI**: Provides a user-friendly interface for file selection and displaying transcription results.

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

1. Start **AudioDictate**.
2. When prompted, input the directory path to the Vosk model.
3. Use the application's interface to select your audio file. The application supports browsing and selecting the file directly within the app.
4. If the selected file is not in WAV format, you'll be asked to select an output directory for the conversion process.
5. After processing, the transcribed text will be displayed within the application window.

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

## Contributing

To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add YourFeature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Create a new Pull Request.


## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Pavan Kumar - pavankumard.pg19.ma@nitp.ac.in

LinkedIn: [linkedin.com/in/im-pavankumar](https://www.linkedin.com/in/im-pavankumar/)

Project Link: [AudioDictate](https://github.com/ascender1729/AudioDictate)
