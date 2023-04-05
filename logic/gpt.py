import random
import openai


# ---------------------------------------------------------------------------- #
#                                      GPT                                     #
# ---------------------------------------------------------------------------- #
class GPT:
    def __init__(self):
        self.model = "gpt-3.5-turbo"
        self.api_key = open("key.txt","r").read().strip('\n')
        openai.api_key = self.api_key
    
    def askChatGPT(self, prompt: str, prefix:str = '', temp: float = 0.8, max_token: int = 350) -> str:
        # openai.api_key = self.api_key
        response = openai.ChatCompletion.create(
            model = self.model,
            messages = [{"role": "user", "content": prefix + prompt}],
            temperature = temp,
            max_tokens = max_token
        )
        answer = response.choices[0].message["content"]
        print(answer)
        return answer
    
    def verifyAnswer(self, prompt_question: str, prompt_answer: str, temp: float = 0.4, max_token: int = 50) -> bool:
        response = openai.ChatCompletion.create(
            model = self.model,
            messages = [{"role": "user", "content": 'You are an expret in the field of computer networking. Your purpose is to check whether the answer is correct. You can only reply "True" or "False" \nQuestion:  ' + prompt_question + '\nAnswer: ' + prompt_answer}],
            temperature = temp,
            max_tokens = max_token
        )
        answer = response.choices[0].message["content"]
        answer_bool = bool(answer)
        return answer_bool

