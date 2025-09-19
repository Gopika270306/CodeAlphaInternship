

def bot():

    print("Bot: Hi! I'm just a small chatbot made for fun 😄")
    print("Say something (or type 'bye' to quit):")

    while True:

        a = input("You: ").lower()

        match a:

            case "hi" | "hello" | "hey":
                print("Bot: Hey there! 👋")

            case "how are you" | "how you doing":
                print("Bot: I'm doing okay... just chilling inside your code. 😊")

            case "What your name" | "your name" | "who are you":
                print("Bot: I'm Gopika's chatbot 😎 Just here to talk!")

            case "what your age" | "your age":
                print("Bot: I'm Created in last month !")

            case "bye":
                print("Bot: Alright, Good bye! Take care ! Have a nice day! 👋")
                break
            case _:
                print("Bot: Umm... I don't really know how to reply to that 🤷‍♀️")

# Run the bot
bot()



