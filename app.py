import sys
import os
import threading
from logic.gpt import GPT
from logic.reader import Reader


def main():
    # Initialize
    ai = GPT()
    reader = Reader()
        
    # ------------------------------- Read the file ------------------------------ #
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
    # print(reader.list)
    
    # ------------------------------- Program loop ------------------------------- #
    counter = 0
    while(counter < len(reader.list)):
        os.system('cls||clear')
        
        # Ask GPT for an explanation
        thread = threading.Thread(target=ai.askChatGPT, args=(reader.getAnswer(counter), "Explain:  "))
        thread.start()
        # temp_gpt = ai.askChatGPT(reader.getAnswer(counter), prefix="Explain:  ")
        
        # Print the question
        print("[", counter, "/", len(reader.list), "]   Question: " + reader.getQuestion(counter))
        user_answer = input(" -> ")
        
        # Check wheter the answer is correct
        if ai.verifyAnswer(reader.getQuestion(counter), reader.getAnswer(counter), user_answer):
            print("Correct!\n Explanation: \n")
            thread.join()
        else:
            print("Incorrect!\n The correct answer is: ", reader.getAnswer(counter), "\nExplanation: \n")
            thread.join()
            reader.list.append(reader.list[counter])
        
        # Proceed
        print(" -- [d] Next question, [a] Previous question, [q] Quit --  ")
        user_input = input(" -> ")
        if user_input == "d":
            counter += 1
        elif user_input == "a":
            counter -= 1
        elif user_input == "q":
            break
        else:
            print("Invalid input")
        
    
    
    
    
    
if __name__ == "__main__":
    main()