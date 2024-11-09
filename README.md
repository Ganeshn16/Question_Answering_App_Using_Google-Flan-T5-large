# Question_Answering_App_Using_Google-Flan-T5-large

Question Answer Bot with Streamlit and Hugging Face Transformers
This repository contains a Question Answer Bot built with Streamlit and Hugging Face’s transformers library, utilizing the flan-t5-large model. The app allows users to select a topic, generate a question, submit an answer, and receive instant feedback on correctness and relevance.


Features
Topic Selection: Choose from Geography, Health, or Sports.
Dynamic Question Generation: Generates unique, contextually relevant questions based on the selected topic.
Answer Evaluation: Evaluates the correctness and relevance of submitted answers and provides feedback, including the correct answer.

Tech Stack
Streamlit: For creating an interactive web interface.
Hugging Face Transformers: For loading flan-t5-large to generate and evaluate questions.
PyTorch: To support the model backend.

Getting Started

Install Requirements
Ensure that Python 3.7+ is installed, then install the required libraries:
pip install streamlit torch transformers

Run the Application
Launch the Streamlit app with the following command:
  streamlit run app.py

Use the Bot
Select a topic.
  Click "Generate Question" to receive a question on the chosen topic.
  Submit an answer and receive feedback on the correctness and relevance of your response.
