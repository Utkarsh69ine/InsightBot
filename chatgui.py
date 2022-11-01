#https://github.com/tridibsamanta/Chatbot-using-Python

from tkinter import font
from turtle import color
import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np

from keras.models import load_model
model = load_model('chatbot_model.h5')
import json
import random
intents = json.loads(open('intents.json', encoding='utf8').read())
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))


def clean_up_sentence(sentence):
    # tokenize the pattern - split words into array
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word - create short form for word
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence

def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))

def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = bow(sentence, words,show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            break
    return result

def chatbot_response(msg):
    ints = predict_class(msg, model)
    res = getResponse(ints, intents)
    return res


#Creating GUI with tkinter
# import tkinter
# from tkinter import *


# def send():
#     msg = EntryBox.get("1.0",'end-1c').strip()
#     EntryBox.delete("0.0",END)

#     if msg != '':
#         ChatLog.config(state=NORMAL)
#         ChatLog.insert(END, "You: " + msg + '\n\n')
#         ChatLog.config(foreground="#FFD553", font=("Verdana", 30 ))
    
#         res = chatbot_response(msg)
#         ChatLog.insert(END, "Bot: " + res + '\n\n')
            
#         ChatLog.config(state=DISABLED)
#         ChatLog.yview(END)
 

# base = Tk()
# base.title("Hello")
# base.geometry("1920x1080")
# base.resizable(width=FALSE, height=FALSE)

# #Create Chat window
# ChatLog = Text(base, bd=0, bg="#1c2020", height="780", width="1920", font="Arial",fg='#FFD553',borderwidth=5, relief="solid")

# ChatLog.config(state=DISABLED)

# #Bind scrollbar to Chat window
# scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart",borderwidth=2, relief="solid")
# ChatLog['yscrollcommand'] = scrollbar.set

# #Create Button to send message
# SendButton = Button(base, font=("Verdana",20,'bold'), text="Send", width="1920", height=100,
#                     bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#FFFFFF',
#                     command= send ,borderwidth=5, relief="solid")

# #Create the box to enter message
# EntryBox = Text(base, bd=0, bg="#FFD553",width="1920", height="200", font="Arial",borderwidth=5, relief="solid")
# #EntryBox.bind("<Return>", send)


# #Place all components on the screen
# scrollbar.place(x=1900,y=0, height=780)
# ChatLog.place(x=0,y=0, height=780, width=1920)
# EntryBox.place(x=0, y=780, height=200, width=1920)
# SendButton.place(x=0, y=980, height=100, width=1920)

# base.mainloop()
