# Coder Retriever 🦮

CodeRetriever: Your loyal coding companion. Just like a Golden Retriever, we're here to fetch and provide you with the most essential pieces of code. 

## Installation

Install the latest release:

`
  pip install coder_retriever
`

or intall the up-to-date version (might be unstable):

`
  pip install git+https://github.com/GitMarco27/coder_retriever.git
`

## Examples

### AI Assistant Digit Mnist Classifier

You can find the complete example [here](https://github.com/GitMarco27/coder_retriever/blob/main/examples/notebooks/digit_mnist_0_1_2.ipynb)

```python
import coder_retriever as cr

assistant = cr.ai.assistant.AiAssistant(openai_api_key="YOUR API KEY")

query = """

- Load the digit mnist dataset from tensorflow datasets and covert it to X (images) and Y (labels) as numpy arrays

"""
assistant.run_code(query, vars=vars())

...

query = """

- Show a batch of classified images, displaying True and Predicted labels.

"""
assistant.run_code(query, vars=vars())
```

![download](https://github.com/GitMarco27/coder_retriever/assets/72693100/7a646205-9e3b-4bba-89f5-317d2a313369)
