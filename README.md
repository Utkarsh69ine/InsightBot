# Chatbot-using-Python
Build a chatbot using deep learning techniques. The chatbot will be trained on the dataset which contains categories (intents), pattern and responses. We use a special recurrent neural network (LSTM) to classify which category the user’s message belongs to and then we will give a random response from the list of responses.

:white_check_mark:  Getting Started 

- [x] Download all the files

- [x] Open Command Prompt

- [x] Get the control to the folder where your files are present

- [x] Make sure your system has the following modules installed - 
tensorflow, keras, nltk, pickle. If not, then install the modules using the command - {pip install module_name}. If your system already has the module, it will show "Requirement already satisfied".

- [x] Now we have to train and create the model. Hence execute the "train_chatbot.py" file using the following command - {python train_chatbot.py}. If the training is successful it will show model created. 

- [x] To start conversation with the chatbot execute the "app.py" file using the following command - {python app.py}. It will open the web window. 

- [x] Write your text in the section on the right to the send button and click on "Send". Enjoy the responses !  


!!! ERROR GUIDE !!!

While executing the file "train_chatbot.py" if you get some error like - "ImportError: cannot import name 'tf_utils'", uninstall keras using the command - {pip uninstall keras}, then reinstall keras using the command - {pip install keras==2.2.0}. Try executing the file, i hope it works properly ! 

## [Open report file for project explanation](https://www.notion.so/InsightBot-using-Python-b6138ffca81241e685978dc4050bd109?pvs=4)

Our objective is to create a personal chatbot that can communicate and perform human-like actions for portfolio websites.

With the help of a database containing categories, patterns, and responses, InsightBot will be trained to understand the user's intent and provide relevant responses. Our retrieval-based chatbot uses pre-defined input patterns and responses to select the correct answer using a specific selection method.

To achieve this, we will be using natural language processing (NLP) to map user input to an intent, which will classify the message and generate an appropriate predefined response. By leveraging deep learning techniques such as LSTM, we aim to create a smart piece of software that can communicate and perform human-like actions.

Join us on this exciting journey as we develop InsightBot using Python, NLTK, and Keras to build a cutting-edge chatbot that revolutionizes customer communication, marketing on social networking sites, and instant messaging with clients.

![](https://pbs.twimg.com/media/FsKSu67aMAEvGs9?format=png&name=large)
