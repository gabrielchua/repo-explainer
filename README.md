# Repo Explainer 📦


This Streamlit application leverages the power of Google's Generative AI and the Gemini-1.5-pro-latest model to provide insights and explanations about GitHub repositories. Simply input a GitHub URL, and the app will analyze the repository's structure and content, generating a comprehensive summary.

## Features

* **Repository Analysis:** Analyzes the directory structure, README, and relevant code files (Python, HTML, CSS, JavaScript, etc.).
* **AI-Powered Explanations:** Employs the Gemini-1.5-pro-latest model to provide clear and informative explanations about the repository's purpose, functionality, and code structure. 
* **Interactive Chat Interface:** Engage in a conversation with the AI to ask specific questions and delve deeper into the repository's details.

## Usage

1. **Clone the repository:** `git clone https://github.com/your-username/repo-explainer.git`
2. **Install dependencies:** `pip install -r requirements.txt` 
3. **Set up API keys:**
    * **Google API Key:** Obtain a Google API key with access to the Generative AI API and set it as the `GOOGLE_API_KEY` environment variable. 
    * **GitHub Token (Optional):** For private repositories or to avoid rate limiting, set your GitHub personal access token as the `GH_API_KEY` environment variable.
4. **Run the application:** `streamlit run app.py`
5. **Access the app:** Open the provided URL in your web browser.
6. **Enter a GitHub URL:** Input the URL of the repository you want to analyze. 
7. **Explore the results:** Review the generated summary and use the chat interface to ask further questions.

## Disclaimer

This project is for educational and experimental purposes.  API usage may incur costs.

_PS: This README was written by Gemini 1.5 Pro, using this demo_
