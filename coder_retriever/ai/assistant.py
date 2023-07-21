import os
from dotenv import load_dotenv
import openai


class AiAssistant(object):
    __default_system_message = """

    You are an AI assistant.

    """

    __coder_system_message = """

    You're task is to provide python code based on the prompt you receive from the user.
    This code will be exececuted with the exec command by the user.

    Provide only code as string.

    First develop the code. After that check the import of all the necessary libraries.

    This is the provided context: {}. 

    Use the context to understand wich variables are available in the user globals() context.
    The value associated with a key in the context can be the actual value or the type of the object (or other useful informations).

    Avoid any print or plot, if not specified by the user.

    You must update globals() with the new defined variables (only the useful ones)

    """

    def __init__(self, system_message: str = None, openai_api_key: str = None,
                 model: str = None, temperature: float = 0.) -> None:
        if openai_api_key is None:
            if load_dotenv():
                openai.api_key = os.getenv("openai_api_key")
            else:
                raise openai.api_key = openai_api_key
        
        if system_message is None:
            self.system_message = self.__default_system_message
        else:
            self.system_message = system_message

        if model is None:
            self.model = "gpt-3.5-turbo"
        else:
            self.model = model

        self.temperature = temperature

    
    def reply(self, prompt: str):
        response = openai.ChatCompletion.create(
        model=self.model,
        messages=[
                {"role": "system", "content": self.system_message},
                {"role": "user", "content": prompt},
            ],
            temperature=self.temperature
            )
        
        return response.choices[0].message.content

    def run_code(self, prompt: str, context: dict = {}, vars = None):
        response = openai.ChatCompletion.create(
        model=self.model,
        messages=[
                {"role": "system", "content": self.__coder_system_message.format(context)},
                {"role": "user", "content": prompt},
            ],
            temperature=self.temperature
            )
        
        code = response.choices[0].message.content

        local_context = {}

        try:
            exec(code, globals(), local_context)

            if vars is not None:
                vars.update(local_context)

        except Exception as e:
            print("Error: ", e)
            print(code)

        return code 