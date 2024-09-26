from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters

# ID канала, куда будут отправляться сообщения
CHANNEL_ID = '-1002388187883'

# Токен бота
TOKEN = '8048926473:AAGU0gD1iV0VZzVs_xn83Tpx9wILe4pEMAQ'

# Функция для обработки сообщений от пользователей
async def forward_message(update: Update, context):
    message = update.message
    if message and message.text:
        await context.bot.send_message(chat_id=CHANNEL_ID, text=message.text)

# Основная функция для запуска бота
async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Добавляем обработчик текстовых сообщений
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_message))

    await app.start_polling()
    await app.idle()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())

