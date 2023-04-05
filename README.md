# AI assisted flashcards
## About
This repo contains a flashcards viewer. It reads from .xlsx or .csv files, loads and shuffles the data, and then displays it in the terminal. As the more unique features go, it also has a built-in AI that can help you learn the cards. Every time you answer an inquiry, the AI will inteligently check whether you were correct or not, and then will provide you with a simple explanation of the issue. Whole process is intended to help you memorise and understand content of the cards faster and more efficiently.

## Installation
In order to run type in the following command:
```
$ pip install -r requirements.txt
```
Then create a file named `key.txt` and paste your unique API key from [here](https://openai.com/blog/openai-api/).  
Eventually, you can run the program by typing:
```
python3 app.py <file_name> <beginning_line_to_read_from> <end_line_to_read_from>
```

## Screenshots