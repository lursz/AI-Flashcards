import openai


# ---------------------------------------------------------------------------- #
#                                      GPT                                     #
# ---------------------------------------------------------------------------- #
class GPT:
    def __init__(self):
        self.model = "gpt-3.5-turbo"
        self.api_key = open("key.txt", "r").read().strip('\n')
        openai.api_key = self.api_key
        self.gpt_style = "" #empty string for no style
    
    
    def askChatGPT(self, chat_object: list[dict], temp: float = 0.6, max_token: int = 350) -> str:
        # Progrssively printing GPT's response token after token
        gpt_stream_explain = openai.ChatCompletion.create(
            model = self.model,
            messages = [
                {"role": "system", "content": f'You are an expert in the field of computer networking. Your purpose is to answer why the answer given by the user is wrong or correct. {self.gpt_style}'}
            ] + chat_object,
            temperature = temp,
            stream = True,
            max_tokens = max_token
        )

        current_role = ""
        for response_part in gpt_stream_explain:
            current_delta = response_part.choices[0]['delta']
            
            if "role" in current_delta:
                current_role = current_delta["role"]
            elif "content" in current_delta:
                if current_role == "assistant":
                    yield current_delta["content"]
    
    
    def verifyAnswer(self, prompt_question: str, correct_answer: str, prompt_answer: str, temp: float = 0.5, max_token: int = 1) -> bool:
        print("Answer is being verified...")

        if prompt_answer.strip() == "":
            return False
        if correct_answer.strip() == prompt_answer.strip():
            return True

        response = openai.ChatCompletion.create(
            model = self.model,
            messages = [
                {"role": "system", "content": 'You are an expert in the field of computer networking. Your purpose is to check whether the answer is correct. You can only reply "Yes" or "No"'},
                {"role": "user", "content": f"Question: {prompt_question}\nCorrect answer given by database: {correct_answer}\My answer: {prompt_answer}. Am I correct? Answer only Yes or No."},
            ],
            temperature = temp,
            max_tokens = max_token
        )
        answer = response.choices[0].message["content"]
        return answer == "Yes"

