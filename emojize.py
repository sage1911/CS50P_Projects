import emoji

user_input = input("Input: ").strip()   

emojized = emoji.emojize(user_input, language='alias')

print("Output: ",emojized)