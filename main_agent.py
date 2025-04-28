import streamlit as st
from groq_client import Groq_Client
import os
from voice_interface import VoiceInterface
import time

class VoiceAgent:
    def __init__(self):
        self.groq_client = Groq_Client()
        self.voice_interface = VoiceInterface()
        self.conversation_history = []

    def run_interaction(self, duration=5):
        try:
            # Record User audio
            audio_file = self.voice_interface.record_audio(duration=duration)

            # Convert Speech to Text
            user_input = self.voice_interface.speech_to_text(audio_file)

            if user_input:
                # Add to conversation history
                self.conversation_history.append({"role": "user", "content": user_input})
                
                # Get AI response
                ai_response = self.groq_client.generate_response(self.conversation_history)
                
                # Add AI response to history
                self.conversation_history.append({"role": "assistant", "content": ai_response})
                
                # Clean up
                os.remove(audio_file)
                
                return user_input, ai_response
            
        except Exception as e:
            st.error(f"Error: {e}")
            return None, None

def main():
    # Custom CSS for styling
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&family=Poppins:wght@300;600&family=Roboto+Mono&display=swap');
        
        /* Main background */
        .stApp {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            font-family: 'Poppins', sans-serif;
        }
        
        /* Titles */
        h1 {
            font-family: 'Montserrat', sans-serif;
            color: #2c3e50 !important;
        }
        
        /* Buttons */
        .stButton>button {
            background: linear-gradient(45deg, #6a11cb 0%, #2575fc 100%) !important;
            color: white !important;
            border: none !important;
            font-family: 'Montserrat', sans-serif;
            font-weight: bold;
            border-radius: 8px !important;
            padding: 10px 24px !important;
        }
        
        .stButton>button:hover {
            box-shadow: 0 4px 15px rgba(106, 17, 203, 0.4);
            transform: translateY(-2px);
            transition: all 0.3s ease;
        }
        
        /* Chat bubbles */
        .user-bubble {
            background-color: #2575fc;
            color: white;
            border-radius: 18px 18px 0 18px;
            padding: 12px 16px;
            margin: 8px 0;
            max-width: 80%;
            margin-left: auto;
            font-family: 'Poppins', sans-serif;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        
        .ai-bubble {
            background-color: #ffffff;
            color: #2c3e50;
            border-radius: 18px 18px 18px 0;
            padding: 12px 16px;
            margin: 8px 0;
            max-width: 80%;
            margin-right: auto;
            font-family: 'Poppins', sans-serif;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        
        /* Sidebar */
        .css-1d391kg {
            background: linear-gradient(180deg, #2c3e50 0%, #1a2530 100%) !important;
        }
        
        /* Code blocks */
        .stCodeBlock {
            font-family: 'Roboto Mono', monospace !important;
        }
    </style>
    """, unsafe_allow_html=True)

    # Initialize session state
    if 'agent' not in st.session_state:
        st.session_state.agent = VoiceAgent()
    if 'conversation' not in st.session_state:
        st.session_state.conversation = []
    if 'recording' not in st.session_state:
        st.session_state.recording = False

    # App header
    st.markdown("""
    <h1 style='text-align: center; margin-bottom: 30px;'>
        🎙️ Voice AI Assistant
    </h1>
    <p style='text-align: center; color: #666; margin-bottom: 40px;'>
        Speak with an AI assistant powered by Groq
    </p>
    """, unsafe_allow_html=True)

    # Sidebar controls
    with st.sidebar:
        st.markdown("## ⚙️ Settings")
        recording_duration = st.slider("Recording duration (seconds)", 2, 10, 5)
        
        st.markdown("## 📚 About")
        st.info("""
        This interactive Voice AI Assistant allows you to:
        - Speak naturally to an AI
        - Get intelligent responses
        - Have a flowing conversation
        """)

    # Main chat area
    chat_container = st.container()

    # Recording button
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("🎤 Hold to Speak", key="record_button"):
            with st.spinner("Listening..."):
                user_input, ai_response = st.session_state.agent.run_interaction(duration=recording_duration)
                
                if user_input and ai_response:
                    st.session_state.conversation.append(("user", user_input))
                    st.session_state.conversation.append(("ai", ai_response))
                    
                    # Rerun to update the chat display
                    st.rerun()

    # Display conversation
    with chat_container:
        for speaker, text in st.session_state.conversation:
            if speaker == "user":
                st.markdown(f"""
                <div class="user-bubble">
                    <strong>You</strong>: {text}
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="ai-bubble">
                    <strong>AI Assistant</strong>: {text}
                </div>
                """, unsafe_allow_html=True)

    # Add some space at the bottom
    st.markdown("<br><br>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()