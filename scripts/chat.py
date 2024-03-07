from barrier import OpenAiApiHandler, AnthropicApiHandler

inp = input("Would you like to prompt GPT-4 or Claude-3? (g/c)? ~ ")
if inp == "g":
    model = "gpt-4-turbo-preview"
    api_handler = OpenAiApiHandler()
elif inp == "c":
    model = "claude-3-opus-20240229"
    api_handler = AnthropicApiHandler()
else:
    print("Invalid input. Exiting.")
    exit()

prompt = input("Type your prompt\n~ ")
print()
msg = [{"role": "user", "content": prompt}]
response = api_handler.prompt_text_model(model=model, messages=msg)
print(response)
