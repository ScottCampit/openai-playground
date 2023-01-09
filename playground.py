# %%
import os
import sys
import argparse
import openai
import typing

# %%
openai.api_key = os.environ["OPENAI_API_KEY"]

# %%
# Create an image using DALLE
def dalleImgGen(prompt:str, n_img:int=4, size:str='1024x1024'):
    response = openai.Image.create(
        prompt=prompt,
        n=n_img,
        size=size
    )
    for obj in response['data']:
        print(obj['url'])
    
    return response

# %%
# Use GPT-3 to generate text from a prompt

def textGenGPT(prompt:str, temperature:float=0.5, max_tokens:int=1500, engine='davinci'):
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=1,
        frequency_penalty=0.3,
        presence_penalty=0.3
    )
    generated_text = response["choices"][0]["text"]
    print(generated_text)

    return generated_text

# %%
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='GPT-3 engine')
    parser.add_argument('--prompt', type=str, 
                    help='Prompt to feed into GPT-3 to generate text.')
    parser.add_argument('--engine', type=str, default='davinci',
                    help='GPT-3 engine')
    parser.add_argument('--temperature', type=float, 
                    help='Parameter that controls the randomness of the generator.')
    parser.add_argument('--max_tokens', type=int, default=1500,
                    help='The maximum number of tokens the model can input is 2049.')
    args = parser.parse_args()

    textGenGPT(prompt=args.prompt, temperature=args.temperature, max_tokens=args.max_tokens, engine=args.engine)
