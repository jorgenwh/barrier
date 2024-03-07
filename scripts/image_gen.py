from barrier import OpenAiApiHandler

model = "dall-e-3"
size = "1024x1024"
quality = "hd"

ah = OpenAiApiHandler()

prompt = input("~ ")
print()
response = ah.prompt_image_model(
        model=model, 
        prompt=prompt, 
        size=size, 
        quality=quality,
)
print(response)
