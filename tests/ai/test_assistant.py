import sys
import os

sys.path.append(os.getcwd())

import coder_retriever as cr


def test_assistant_reply():
    system_message = "You are a ai assistant talking like a dog"

    assistant = cr.ai.assistant.AiAssistant(system_message=system_message)

    query = "How are you doing?"

    print(assistant.reply(query))

def test_assistant_run_code():
    assistant = cr.ai.assistant.AiAssistant()
    query = "Create two numpy array, x and y. They must have shape (100, 1). Print their shapes. \
         X must be linearly between 0 and 1. Y is x**2 - 3."
    assistant.run_code(query, vars=vars())

    assert "x" in vars() and "y" in vars()


if __name__ == "__main__":
    test_assistant_reply()