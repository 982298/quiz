from flask import Flask, render_template, request
import os

app = Flask(__name__)

questions = [

    {
        "question": "What is the capital of India?",
        "options": ["Delhi", "Mumbai", "Chennai", "Kolkata"],
        "answer": "Delhi"
    },

    {
        "question": "Which language is used in Flask?",
        "options": ["Java", "Python", "C++", "PHP"],
        "answer": "Python"
    },

    {
        "question": "Who developed Python?",
        "options": ["James Gosling", "Guido van Rossum", "Dennis Ritchie", "Bjarne Stroustrup"],
        "answer": "Guido van Rossum"
    },

    {
        "question": "Which company developed Windows?",
        "options": ["Apple", "Google", "Microsoft", "IBM"],
        "answer": "Microsoft"
    },

    {
        "question": "What does CPU stand for?",
        "options": ["Central Process Unit", "Central Processing Unit", "Computer Personal Unit", "Central Processor Utility"],
        "answer": "Central Processing Unit"
    },

    {
        "question": "Which HTML tag is used for inserting an image?",
        "options": ["<img>", "<image>", "<pic>", "<src>"],
        "answer": "<img>"
    },

    {
        "question": "Which protocol is used to browse websites?",
        "options": ["FTP", "SMTP", "HTTP", "SSH"],
        "answer": "HTTP"
    }

]

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':

        score = 0

        for i, q in enumerate(questions):

            selected = request.form.get(f"q{i}")

            if selected == q["answer"]:
                score += 1

        return render_template('result.html',
                               score=score,
                               total=len(questions))

    return render_template('index.html',
                           questions=questions)

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0",
            port=port,
            debug=True)