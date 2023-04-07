import random
import openai


# ---------------------------------------------------------------------------- #
#                                      GPT                                     #
# ---------------------------------------------------------------------------- #
class GPT:
    def __init__(self):
        self.model = "gpt-3.5-turbo"
        self.api_key = open("key.txt", "r").read().strip('\n')
        openai.api_key = self.api_key
    
    def askChatGPT(self, prompt: str, prefix:str = '', temp: float = 0.8, max_token: int = 350) -> str:
        # openai.api_key = self.api_key
        response = openai.ChatCompletion.create(
            model = self.model,
            messages = [{"role": "user", "content": prefix + prompt}],
            temperature = temp,
            stream = True,
            max_tokens = max_token
        )
        current_role = ""
        for response_part in response:
            current_delta = response_part.choices[0]['delta']
            if "role" in current_delta:
                current_role = current_delta["role"]
            elif "content" in current_delta:
                print(current_delta["content"])
            #response_part.choices[0].message["content"]
    
    def verifyAnswer(self, prompt_question: str, correct_answer: str, prompt_answer: str, temp: float = 0.5, max_token: int = 1) -> bool:
        if prompt_answer.strip() == "":
            return False
        
        if correct_answer.strip() == prompt_answer.strip():
            return True

        response = openai.ChatCompletion.create(
            model = self.model,
            messages = [{"role": "system", "content": 'You are an expert in the field of computer networking. Your purpose is to check whether the answer is correct. You can only reply "Yes" or "No"'},
                        {"role": "user", "content": f"Question: {prompt_question}\nCorrect answer: {correct_answer}\nUser answer: {prompt_answer}"},
                        ],
            temperature = temp,
            max_tokens = max_token
        )
        answer = response.choices[0].message["content"]
        
        return answer == "Yes"

