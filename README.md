# AI flashcards
## About
This repo features a unique flashcards viewer, designed to efficiently aid in the memorization and comprehension of any educational material. It reads data from both .xlsx and .csv files. Additionally, the flashcard viewer also has a built-in AI assistant that can impersonate the style of anyone to provide tailored (or just plain funny) way of aiding you in your learning process. Program dynamically evaluates your responses, offering explanations to any misconceptions and reinforcing your understanding of the subject matter.

## Installation
In order to run the program, you will need to install `Python3` and `pip`.
Then install the required dependencies by typing:
```bash
$ pip install -r requirements.txt
```
or (if above command fails)
```bash
$ pip install openai
$ pip install openpyxl
$ pip install python-csv
```

Then create a file named `key.txt` and paste your unique API key from [here](https://openai.com/blog/openai-api/).  
Eventually, you can run the program by typing:
```
python3 app.py <file_name> <beginning_line> <end_line>
```
Beggining and ending lines are optional, and if not specified, the program will read the entire file.

## Usage
The program will read the file and present the flashcards one by one. All necessary instructions are going to be displayed on the screen.

## AI assistant customization
The AI assistant is capable of impersonating the style of anyone. However, the more popular the person is, the more data is available for the AI to learn from. Therefore, the more popular the person is, the more accurate the impersonation will be.  
In order to change the AI assistant's style, you will need to edit `app.py` file and change the `style` variable to the name of your liking.

## Screenshots
Correct answer:
![right](https://user-images.githubusercontent.com/93160829/230689929-2ff8afaf-a524-4030-97dd-6dfef2ec5a82.gif)
Incorrect answer:
![wrong](https://user-images.githubusercontent.com/93160829/230689947-38470cfd-7ff9-4145-b100-2ef3387d22ca.gif)
Incorrect answer && 'toxic Donald Trump' style
![trump](https://user-images.githubusercontent.com/93160829/230689994-15dbcf24-7871-44e6-99f7-a1d87623df2b.gif)
