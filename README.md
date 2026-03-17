# AI Interview Practice System

A Streamlit-based AI-powered interview practice platform that uses Google's Gemini API to conduct realistic technical interviews and provide real-time feedback.

## Features

✨ **User Authentication**
- Secure user registration and login
- Password hashing with SHA-256
- Session management

🤖 **AI Interview Practice**
- Generate realistic technical interview questions
- AI-powered feedback and scoring
- Support for multiple job roles

📊 **Interview Analysis**
- Performance scoring (1-10)
- Detailed improvement suggestions
- Real-time AI feedback

## Setup

### Prerequisites
- Python 3.8+
- Streamlit
- Google Generative AI SDK
- Google API Key

### Installation

1. Clone the repository:
```bash
git clone https://github.com/sumayasayeed/ai-interview-practise-system.git
cd ai-interview-practise-system
```

2. Install dependencies:
```bash
pip install streamlit google-generativeai
```

3. Set up your Google API key:
   - Get your API key from [Google AI Studio](https://aistudio.google.com)
   - Add it to `app.py` (replace `YOUR_API_KEY`)

4. Run the application:
```bash
streamlit run app.py
```

5. Open your browser and go to `http://localhost:8501`

## Project Structure

```
.
├── app.py              # Main Streamlit application
├── auth.py             # Authentication module
├── users.json          # User database
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## Usage

1. **Register** - Create a new account
2. **Login** - Sign in with your credentials
3. **Select Job Role** - Choose your target position (e.g., Java Developer)
4. **Generate Question** - Get an AI-generated interview question
5. **Answer** - Provide your response
6. **Get Feedback** - Receive AI-powered analysis and improvement tips

## Technology Stack

- **Frontend**: Streamlit
- **AI/ML**: Google Generative AI (Gemini)
- **Authentication**: SHA-256 password hashing
- **Database**: JSON (users.json)

## Security Notes

⚠️ **Important**: This is a demo application. For production use:
- Move API keys to environment variables (not hardcoded)
- Use a proper database instead of JSON
- Implement stronger password hashing (bcrypt)
- Add rate limiting and input validation
- Use HTTPS and proper session management

## Future Enhancements

- [ ] Interview history and analytics
- [ ] Mock interview recordings
- [ ] Performance tracking dashboard
- [ ] Multiple question difficulty levels
- [ ] Database integration (PostgreSQL/MongoDB)
- [ ] User profile customization

## License

MIT License - feel free to use this project for learning and personal projects.

## Support

For issues or questions, please open an issue on GitHub.
