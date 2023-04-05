import sys
import os
import keyboard



import logic


def main():
    # Initialize
    ai = logic.GPT()
    reader = logic.Reader()
        
    # Read the file
    input_file = sys.argv[1]
    if (input_file.endswith(".csv")):
        reader.readCSV(input_file)
    elif (input_file.endswith(".xlsx")):
        reader.readXlsx(input_file)
    else:
        print("Invalid file type")
    
    # Potentially cut the list
    if (len(sys.argv) == 4):
        reader.cutQuestions(int(sys.argv[2]), int(sys.argv[3]))
    # Shuffle
    reader.shuffle()
    
    counter = 0
    while(True):
        os.system('cls||clear')
        temp_gpt = ai.askChatGPT(reader.getQuestion(counter), prefix="Explain  ")
        print("Question: " + reader.getQuestion(counter))

        if keyboard.is_pressed(' '):
            print('--- \n')
            print("Answer: " + reader.getAnswer(counter))
            print("\n")
            print("Info: " + temp_gpt)
        elif keyboard.is_pressed('d'):
            counter += 1
        elif keyboard.is_pressed('a'):
            counter -= 1

        elif keyboard.is_pressed('q'):
            print('Goodbye!')
            break
        print(reader.list)
    
    
    
    
    
if __name__ == "__main__":
    main()