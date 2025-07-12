# 🤖 AI-Powered Interviewer

A command-line based AI Interviewer that conducts interactive interviews by parsing a candidate's PDF resume, generating tailored technical questions, and dynamically asking follow-up questions — all using LLMs and multi-agent orchestration.

🚀 Features
📄 PDF Resume Parsing — Automatically extracts and clusters content from uploaded resumes.

🎯 Custom Questions — Generates interview questions based on the candidate’s unique resume content.

🔁 Follow-up Logic — Dynamically adapts based on user responses using an intelligent follow-up agent.

🧠 Multi-Agent System — Built using LangGraph and LangChain for agent orchestration and memory.

📚 Modular & Extensible — Easy to add new nodes or logic for other interview formats.

🎯 Video Sample is Added for Visual Idea

🛠️ Tech Stack
Python 3.10+

LangGraph for agent flow control

LangChain for LLM integration

pdfminer.six for resume extraction

OpenAI or any LLM-backed provider (configurable)

📦 Installation
bash
Copy
Edit
# Clone the repository
git clone https://github.com/dev-Rutwik/Interview-AI.git
cd Interview-AI

# Create virtual environment
conda create -n ai_interviewer python=3.10
conda activate ai_interviewer

# Install dependencies
pip install -r requirements.txt
⚙️ Configuration
Create a .env file in the root directory to securely store your API key:

env
Copy
Edit
MISTRAL_API_KEY=your-MISTRAL_API_KEY
🧪 How to Use (CLI Version)
Place your resume PDF in the root directory.

Run the following script:

bash
Copy
Edit
python app/cli.py
You'll be prompted to enter your resume filename.

The AI interviewer will start asking questions in the terminal based on your resume content.

Respond to each question — the system will adapt and continue the interview.

🧠 How It Works
Resume Clustering: Clusters similar sections of your resume (skills, projects, experience).

Question Generation: An LLM agent creates relevant technical questions from each cluster.

Follow-Up Engine: Responds to answers with tailored follow-up questions.

State Management: All progress is tracked using a shared InterviewState.

🧩 Example Output
bash
Copy
Edit
🤖 Starting interview...

Question 1: Can you explain how your work on the 'Fraud Detection System' used machine learning models?

💬 Your Answer: I used logistic regression to classify transactions...

🤖 Follow-up: Why did you choose logistic regression over other classifiers?
🤝 Contributing
Feel free to open issues or PRs to improve the interviewer logic, support more resume formats, or integrate new LLMs.

📄 License
MIT License

Let me know if you'd like:

A shorter "Quickstart" version

GitHub Actions for deployment/testing

Custom PDF template or export logs to .json or .md format