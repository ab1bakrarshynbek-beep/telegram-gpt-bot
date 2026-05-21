import telebot
from openai import OpenAI

BOT_TOKEN = "8958336623:AAG88z3da1mqsd3_T4tSVbzNflLTSVXI3xs"
OPENAI_API_KEY = "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"

bot = telebot.TeleBot(BOT_TOKEN)

client = OpenAI(
    api_key=OPENAI_API_KEY
)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "Привет! Я GPT бот 😎"
    )

@bot.message_handler(func=lambda message: True)
def chat(message):
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "user",
                    "content": message.text
                }
            ]
        )

        answer = response.choices[0].message.content

        bot.reply_to(message, answer)

    except Exception as e:
        bot.reply_to(message, f"Ошибка: {e}")

print("GPT бот запущен!")

bot.infinity_polling()
