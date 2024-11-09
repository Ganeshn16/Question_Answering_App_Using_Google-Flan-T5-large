#Import Library
#Load the Model and Tokenizer
#For web interface using Streamlit


#Import Libraries
import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-large")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-large")

#Streamlit app

st.title("Question Answer Bot")

#Topic Selection
topics = ["Geography", "Health", "Sports"]
selected_topics = st.selectbox("Select a topic", topics)

#Generate question
if st.button("Generate Question"):
    prompt = f"Create a unique and thoughtful question related to {selected_topics}."
    inputs = tokenizer(prompt, return_tensors = "pt")
    output = model.generate(**inputs, temperature = 0.9, do_sample = True)
    question = tokenizer.decode(output[0], skip_special_tokens= True)
    st.session_state.question = question
    st.write("Question: ", question)

#Answer Submission
if "question" in st.session_state:
    answer = st.text_input("Your answer: ")
    if st.button("Submit Answer"):
        question = st.session_state.question
        prompt = f"{question}\nAnswer:{answer}\nEvaluate the correctness of the answer and tell us the correct answer"
        eval_input = tokenizer(prompt, return_tensors="pt")
        output = model.generate(**eval_input, temperature = 0.8, num_beams = 4, top_p = 0.9, do_sample = True)
        evaluation = tokenizer.decode(output[0], skip_special_tokens= True)
        st.write("Evaluation: ", evaluation)
