Conversational AI with Gemini & PDF Export

This project allows users to interact with Google's Gemini model in a Q&A loop and saves the entire conversation history into a PDF file for later reference.

🚀 Features

Ask questions in a loop.
Get answers from the Gemini AI model.
Store the complete conversation history (questions + answers) into a PDF.

📦 Requirements

Install dependencies using `requirements.txt`:

```
bash
pip install -r requirements.txt
```

# Dependencies

`google-genai`
`reportlab`

⚙️ Setup

1. Clone this repository:

   ```
   bash
   git clone https://github.com/your-username/ai-conversation-keeper.git
   cd gemini-pdf-export
   ```

2. Add your Google Gemini API key in the script:

   ```
   python
   client = genai.Client(api_key="YOUR_API_KEY_HERE")
   ```

3. Run the script:

   ```
   bash
   python main.py
   ```

📝 Usage

1. Run the script.
2. Enter your question when prompted.
3. Gemini will generate an answer.
4. Type 'y' to continue asking more questions, or 'n' to end the session.
5. When you exit, the conversation history will be saved into `gemini_convo.pdf`.

📂 Output

A file named `gemini_convo.pdf` containing all questions and answers in a clean, readable format will be downloaded in your directory. You can view the conversation from there!
