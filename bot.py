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