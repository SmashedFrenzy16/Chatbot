from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from data_cleaner import clean_corp

CORP_FILE = "chat.txt"

initial_bot = ChatBot("CoffeeBot")

exit_words = ("quit", "exit", "see you later", "talk to you later")

bot_trainer = ListTrainer(initial_bot)

cleaned_corp = clean_corp(CORP_FILE)

bot_trainer.train(cleaned_corp)

bot_trainer.train([
    "Hello",
    "Hello there, what's up?",
])
bot_trainer.train([
    "How do you make coffee?",
    "You add coffee powder to the hot water, and let it brew!",
])

while True:

    prompt = input(":-$ ")

    if prompt in exit_words:
        break
    
    else:

        print(f"☕ {initial_bot.get_response(prompt)}")
