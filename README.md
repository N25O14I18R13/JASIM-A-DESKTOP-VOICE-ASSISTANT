# JASIM-A-DESKTOP-VOICE-ASSISTANT

# JASIM - Just A Simple Intelligent Machine

![JASIM Logo](https://img.shields.io/badge/JASIM-Desktop%20Assistant-25D366?style=for-the-badge)

## Overview

JASIM (Just A Simple Intelligent Machine) is a powerful desktop voice assistant built in Python. It offers a seamless voice-controlled interface for everyday computer tasks, web searches, communications, and more. With an elegant chat-based UI, JASIM makes interacting with your computer as simple as having a conversation.

## Features

### System Control
- **App Management**: Open and close applications with voice commands
- **Web Navigation**: Launch websites and perform web searches
- **Screenshot Capture**: Take and save screenshots instantly
- **Volume Control**: Adjust system volume using voice commands
- **Media Controls**: Pause, play, mute/unmute media content

### Communication
- **WhatsApp Integration**: Send WhatsApp messages directly through voice commands
- **Email Management**: Compose and send emails through voice interaction
- **Camera Control**: Launch camera and take photos with voice commands

### Information Services
- **Wikipedia Access**: Get concise information from Wikipedia
- **Weather Updates**: Retrieve current weather conditions for any city
- **Time & Date**: Quick access to current time and date information
- **YouTube Search**: Search and play YouTube videos through voice

### Personal Assistant Features
- **Memory Function**: Store and recall information between sessions
- **Jokes**: Get random jokes to lighten your mood
- **Music Player**: Play random music from your collection

## Technology Stack

- **Core**: Python 3.x
- **Voice Recognition**: SpeechRecognition, PyAudio
- **Text-to-Speech**: pyttsx3
- **GUI**: Tkinter with custom chat bubble interface
- **Database**: SQLite for persistent memory
- **APIs Integration**:
  - OpenWeatherMap API for weather data
  - Gmail SMTP for email functionality
  - Wikipedia API for information retrieval
  - YouTube/WhatsApp integration via pywhatkit

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/JASIM.git
cd JASIM
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Run JASIM:
```bash
python jasim.py
```

## Dependencies

```
pyttsx3
SpeechRecognition
pywin32
wikipedia
pywhatkit
pyautogui
requests
pyjokes
keyboard
Pillow
```

## Usage

1. Launch JASIM application
2. Click the microphone button to activate listening mode
3. Speak your command clearly (examples below)
4. View JASIM's response in the chat interface

### Example Commands

- "What time is it?"
- "Open Chrome"
- "Search on YouTube for Python tutorials"
- "Send a WhatsApp message"
- "Tell me the weather in New York"
- "Remember that I have a meeting tomorrow at 3 PM"
- "Take a screenshot"
- "Tell me a joke"
- "Volume up"

## Project Structure

```
JASIM/
├── jasim.py           # Main application file
├── jasim.db           # SQLite database for memory storage
├── requirements.txt   # Required packages
├── mic_icon.png       # Microphone icon for UI
└── README.md
```

## Future Enhancements

- Natural Language Processing integration for more conversational interactions
- Custom wake word implementation
- Calendar integration for scheduling
- Multi-language support
- Machine learning integration for personalized responses
- Cross-platform compatibility (macOS, Linux)

## Contributors

- Yuvraj
- Vishnu

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

*JASIM was developed as a part of a semester project.*
