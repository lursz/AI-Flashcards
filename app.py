import sys
import os
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
        print("[", counter, "/", len(reader.list), "]   Question: " + reader.getQuestion(counter))
        user_answer = input(" -> ")
        
        # Ask GPT for an explanation
        temp_gpt = ai.askChatGPT(reader.getAnswer(counter), prefix="Explain:  ")
        
        # Check wheter the answer is correct
        if ai.verifyAnswer(reader.getQuestion(counter), user_answer):
            print("Correct!\n Explanation: \n")
            print(temp_gpt)
        else:
            print("Incorrect!\n The correct answer is: ", reader.getAnswer(counter), "\n Explanation: \n")
            print(temp_gpt)
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