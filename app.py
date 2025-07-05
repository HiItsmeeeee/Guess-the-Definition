from random import randint
from flask import Flask, render_template
from words import word_list
from definition import definitions
from cs50 import SQL
from phrases import phrase_list
from ShowNOTTell import ShowNT


app = Flask(__name__)

@app.route("/")
def word_generator_page():
    no_of_words = -1
    for i in word_list:
        no_of_words += 1
    randomise = randint(0, no_of_words)
    word = word_list[randomise]
    definition = definitions[randomise]
    return render_template("home.html", word=word, index=randomise, definition=definition)

@app.route("/phrases")
def phrases():
    no_of_phrases = -1
    for i in phrase_list:
        no_of_phrases += 1
    randomise = randint(0, no_of_phrases)
    phrase = phrase_list[randomise]
    return render_template("phrases.html", phrase=phrase)

@app.route("/timer")
def timer():
    return render_template("timer.html")

@app.route("/Shownottell")
def show_not_TELL():
    show_not_tell = -1
    for i in ShowNT:
        show_not_tell += 1
    randomise = randint(0, show_not_tell)
    show = ShowNT[randomise]
    return render_template("shownottell.html", show=show, index=randomise)

print(app.url_map)

