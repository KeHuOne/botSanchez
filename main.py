import config
import logging
import time


from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

bad_words = ["ебать", "мудак", "бля", "хуй", "xуй", "хyй", "xyй", "пизда",
             "хуя", "ебались", "ебать", "пидор", "ахуенно", "пиздюк", "долбоеб", "долбоёб", "ебучая", "ебаная", "ёбаная"]

#other_lang = ["x x x"] - словарь умных\редких слов



# remove new user join messages
#@dp.message_handler(content_types=["new_chat_members"])
#async def on_user_joined(message: types.Message):
#    await message.delete()

#@dp.message_handler(commands=['help'])
#async def process_help(message: types.Message):
#    await bot.send_message(message.chat.id, "Нужна помощь?")

#@dp.message_handler()
#async def process_reply(message: types.Message):
#    await message.reply("Ваш текст!")

@dp.message_handler(content_types=['text'])
async def filter_messages(message: types.Message):
    for i in range(0, len(bad_words)):
        if bad_words[i] in message.text.lower():
            try:
                mes = message.text.lower().replace(bad_words[i], 'пендехо')
                await message.reply(f"{message.from_user.first_name}, ваше сообщение содержало матные слова и было отредактированно на : {mes}")
                await message.delete()
            except OSError:
                print("BadWordsError - Sending again after 3 seconds!!!")
                time.sleep(3)
                mes = message.text.lower().replace(bad_words[i], 'пендехо')
                await message.reply(f"{message.from_user.first_name}, ваше сообщение содержало матные слова и было отредактированно на : {mes}")
                await message.delete()
# Сделать функцию тролящую умников =)
#    for l in range(0, len(other_lang)):
#        if other_lang[l] in message.text.lower():
#            await message.reply





if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)