## 🎙️ **Voice AI Assistant**

A real-time voice-controlled AI assistant that allows natural language conversations through speech recognition and text-to-speech capabilities, powered by Groq's ultra-fast LLM inference.

![image](https://github.com/user-attachments/assets/ba49290a-20be-43f5-b131-da3c134ad7bd)

*Fig 1: AI VOICE ASSISTANT STREAMLIT UI*

## 🌟 **Features**

- Voice Interaction: Speak naturally to the AI assistant
- Real-time Processing: Fast response times using Groq's LPU inference engine
- Conversation History: Maintains context across multiple turns
- Customizable UI: Beautiful Streamlit interface with responsive design
- Offline Speech Recognition: Uses Google's speech recognition API
- Easy Configuration: Environment variables for API keys and model selection

## 🛠️ **Technologies Used**

- **Groq API:** For ultra-fast LLM inference
- Streamlit: For the web interface
- SpeechRecognition: For speech-to-text conversion
- SoundDevice/SoundFile: For audio recording
- PyDub: For audio playback
- Python-dotenv: For environment management

## ⚙️ **Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/voice-ai-assistant.git
   cd voice-ai-assistant
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
5. Create a .env file in the root directory with your API keys:
   ```bash
   GROQ_API_KEY=your_groq_api_key_here
   MODEL_NAME=mixtral-8x7b-32768  # or other Groq-supported model

## 🚀 **Usage**

1. Run the Streamlit application:
   ```bash
   streamlit run app.py
2. The application will open in your default browser.
3. Click the "Hold to Speak" button and speak to the assistant.
4. The AI will process your speech and respond.

## 📝 **Configuration Options**

You can customize the application through:

1. Environment Variables (in .env file):
   - GROQ_API_KEY: Your Groq API key
   - MODEL_NAME: The LLM model to use (default: mixtral-8x7b-32768)

2. UI Settings (in the sidebar):
   - Recording duration (2-10 seconds)

3. Code Customization:
   - Adjust temperature and other LLM parameters in groq_client.py
   - Modify the UI styling in app.py

## 🤝 **Contributing**
Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (git checkout -b feature/your-feature)
3. Commit your changes (git commit -am 'Add some feature')
4. Push to the branch (git push origin feature/your-feature)
5. Create a new Pull Request

## 📜 **License**

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 **Acknowledgments**

- Groq for their amazing inference technology
- Streamlit for the easy-to-use web framework
- All open-source libraries used in this project

## 📧 **Contact**
For questions or feedback, please open an issue on GitHub or contact the maintainer directly.
