import tkinter as tk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

faqs = {
    "what is artificial intelligence": "Artificial Intelligence is the ability of machines to think and learn like humans.",
    "what is machine learning": "Machine Learning is a part of AI where computers learn from data.",
    "what is python": "Python is a popular programming language used in AI, web development, and automation.",
    "what is chatbot": "A chatbot is a program that can interact with users and answer questions.",
    "what is cloud computing": "Cloud computing means storing and accessing data and services over the internet.",
    "what is data science": "Data Science is the process of analyzing data to find useful information.",
    "what is deep learning": "Deep Learning is a type of machine learning that uses neural networks.",
    "what is nlp": "NLP stands for Natural Language Processing. It helps computers understand human language."
}

questions = list(faqs.keys())
answers = list(faqs.values())

vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(questions)

def get_answer():
    user_question = entry.get().lower()

    if user_question.strip() == "":
        output_label.config(text="Please enter a question.")
        return

    user_vector = vectorizer.transform([user_question])
    similarity = cosine_similarity(user_vector, question_vectors)

    best_match = similarity.argmax()
    score = similarity[0][best_match]

    if score > 0.3:
        output_label.config(text=answers[best_match])
    else:
        output_label.config(text="Sorry, I don't know the answer. Please ask another question.")

root = tk.Tk()
root.title("FAQ Chatbot")
root.geometry("500x400")

title = tk.Label(root, text="AI FAQ Chatbot", font=("Arial", 18))
title.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

button = tk.Button(root, text="Ask", command=get_answer)
button.pack(pady=10)

output_label = tk.Label(root, text="", wraplength=450, font=("Arial", 12))
output_label.pack(pady=20)

root.mainloop()