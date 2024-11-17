from flask import Flask, render_template, request, jsonify
import random
import json
import pickle
import numpy as np
from tensorflow.keras.models import load_model
from nltk.stem import WordNetLemmatizer
import nltk

# Inisialisasi NLTK dan Lemmatizer
lemmatizer = WordNetLemmatizer()

# Load model dan data pendukung
model = load_model("dataset/chatbot_model.h5")
words = pickle.load(open("dataset/words.pkl", "rb"))
classes = pickle.load(open("dataset/classes.pkl", "rb"))

# Load intents data dengan encoding utf-8
with open("dataset/data.json", "r", encoding="utf-8") as json_file:
    intents = json.load(json_file)

# Preprocessing Input User
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bow(sentence, words):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
    return np.array(bag)

# Prediksi Kelas Intent
def predict_class(sentence):
    bow_vector = bow(sentence, words)
    res = model.predict(np.array([bow_vector]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

# Ambil Respon Sesuai Intent
def get_response(intents_list, intents_json):
    if not intents_list:
        return "Maaf, saya tidak mengerti. Bisa dijelaskan lebih detail?"
    tag = intents_list[0]["intent"]
    for intent in intents_json["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])

# Inisialisasi Flask
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_input = request.json.get("message")  # Ambil input dari frontend
    intents_list = predict_class(user_input)
    response = get_response(intents_list, intents)
    return jsonify({"response": response})

@app.route("/welcome", methods=["GET"])
def welcome_message():
    for intent in intents["intents"]:
        if intent["tag"] == "welcome":
            response = random.choice(intent["responses"])
            return jsonify({"response": response})
    return jsonify({"response": "Selamat datang! Ada yang bisa saya bantu?"})


if __name__ == "__main__":
    app.run(debug=True)
