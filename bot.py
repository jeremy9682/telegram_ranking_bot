from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, filters
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, BotCommand
import config, commands, database

async def handle_message(update, context):
    if update.message.chat.type in ['group', 'supergroup']:
        user_id = update.message.from_user.id
        username = update.message.from_user.username or update.message.from_user.full_name
        if database.update_points(user_id, username):
            print(f"积分增加：{username}")

from telegram import Update
from telegram.ext import ContextTypes

async def get_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    username = update.effective_user.username
    await update.message.reply_text(f"你的 Telegram 用户 ID 是：{user_id}\n用户名：@{username}")

async def set_commands(app):
    commands_list = [
        BotCommand("menu", "显示主菜单"),
        BotCommand("bind", "绑定钱包地址"),
        BotCommand("balance", "查看积分"),
        BotCommand("withdraw", "申请提现")
    ]
    await app.bot.set_my_commands(commands_list)


def main():
    app = ApplicationBuilder().token(config.TOKEN).build()

    app.add_handler(CommandHandler("start", commands.start))
    app.add_handler(CommandHandler("bind", commands.bind))
    app.add_handler(CommandHandler("balance", commands.balance))
    app.add_handler(CommandHandler("withdraw", commands.withdraw))
    app.add_handler(CommandHandler("settoken", commands.settoken))
    app.add_handler(CommandHandler("getid", get_id))
    app.add_handler(CommandHandler("menu", commands.menu))
    app.add_handler(CallbackQueryHandler(commands.handle_callback))
   

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot已启动...")
    app.post_init = lambda _: set_commands(app)
    app.run_polling()

if __name__ == '__main__':
    main()

