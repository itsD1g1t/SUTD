
import os
from openai import OpenAI

client = OpenAI(api_key="")
    # Insert the API key between the "" above. Make sure to remove the key before uploading this file to GitHub


def call(sent):
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[{"role": "system", "content": 'SPECIFY HOW THE AI ASSISTANT SHOULD BEHAVE'}, # input promt engeinrgin stuff here ,examples etc.
            {"role": "user", "content": 'SPECIFY WANT YOU WANT THE AI ASSISTANT TO SAY'}
    ])

    # Create a scenario and add context for ChatGPT. Can also include sample examples.
    system_msg = 'You are a native Singaporean and an expert in Singlish. \
                    Your English speaking friend is planning to visit Singapore. \
                    They have sent you phrases that they want translated into Singlish. \
                    When translating them, please provide two authentic variations of the phrase. \
                    our response should have the translations labelled as 1 and 2. Here is an example. \
                    English input: How much is this? Singlish translation: 1. How much is this ah? \
                    2. Eh, how much ah?. Another example would be English input: How long does it take \
                    to get to the mall? Singlish translation: 1. How long need to reach the mall? 2. \
                    Eh, how long take to reach the mall ah? Using these examples as a reference. \
                    Here is the phrase your friend wants to be translated: ' 
    user_msg = sent
    response = client.chat.completions.create(model="gpt-3.5-turbo",
                                    messages=[{"role": "system", "content": system_msg},
                                    {"role": "user", "content": user_msg}])
    
    return(response.choices[0].message.content)
