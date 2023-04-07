import sys
import os
import threading
from logic.gpt import GPT
from logic.reader import Reader


def main():
    # Initialize
    ai = GPT()
    reader = Reader()

    should_quit = False

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
    while(counter < len(reader.list) and not should_quit):
        os.system('cls||clear')
        
        # Print the question
        print("[", counter, "/", len(reader.list), "]   Question: " + reader.getQuestion(counter))
        user_answer = input(" -> ")

        # Check wheter the answer is correct
        if ai.verifyAnswer(reader.getQuestion(counter), reader.getAnswer(counter), user_answer):
            print(f"Correct! Correct answer is {reader.getAnswer(counter)}\n\nExplanation:")
        else:
            print("Incorrect!\n The correct answer is: ", reader.getAnswer(counter))
            reader.list.append(reader.list[counter])

        # Base GPT question template
        chat_object = [{"role": "user", "content": f"Question was: {reader.getQuestion(counter)}\nCorrect answer given by database: {reader.getAnswer(counter)}\nMy answer: {user_answer}. Is my answer correct?"}]
        while True:
            chat_answer = ""
            
            print("(AI) -> ", end = "") # Print with flush (cause no endl)
            sys.stdout.flush()
            
            # Print answer token by token in real time
            for token in ai.askChatGPT(chat_object): # Ask GPT for an explanation
                chat_answer += token
                print(token, end = "")
                # print the buffor
                sys.stdout.flush()
            chat_object.append({"role": "assistant", "content": chat_answer})

            # Proceed
            print("\n\n -- [d] Next question, [a] Previous question, [h] [<question>] To ask question, [q] Quit --  ")
            user_input = input(" -> ")
            if user_input == "d":
                counter += 1
                break
            elif user_input == "a":
                counter -= 1
                break
            elif user_input == "q":
                should_quit = True
                break
            elif user_input[0] == "h" and len(user_input) > 2:
                chat_object.append({"role": "user", "content": user_input[2:]})
            else:
                print("Invalid input")
                break
        

    
if __name__ == "__main__":
    main()