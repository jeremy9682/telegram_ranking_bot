from telegram import Update
from telegram.ext import ContextTypes
import database
import config

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("欢迎使用聊天积分机器人，请私聊发送 /bind 你的钱包地址 进行绑定。")

async def bind(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return
    
    wallet = ' '.join(context.args)
    if wallet:
        database.bind_wallet(update.message.from_user.id, wallet)
        await update.message.reply_text(f"绑定钱包成功！地址为: {wallet}")
    else:
        await update.message.reply_text("绑定失败，请发送 `/bind 钱包地址`")

async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = (
        update.message.from_user.id if update.message
        else update.callback_query.from_user.id
    )
    username = (
        update.message.from_user.username if update.message
        else update.callback_query.from_user.username
    )
    reply = (
        update.message.reply_text if update.message
        else update.callback_query.message.reply_text
    )

    user = database.get_user(user_id)
    if user:
        wallet, points = user
        await reply(f"当前积分: {points}\n钱包地址: {wallet or '未绑定'}")
    else:
        await reply("你还没有积分记录，快去群里多聊天赚积分吧！")

async def withdraw(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = (
        update.message.from_user.id if update.message
        else update.callback_query.from_user.id
    )
    username = (
        update.message.from_user.username if update.message
        else update.callback_query.from_user.username
    )
    reply = (
        update.message.reply_text if update.message
        else update.callback_query.message.reply_text
    )

    user = database.get_user(user_id)
    if user:
        wallet, points = user
        if not wallet:
            await reply("你尚未绑定钱包，私聊发送 `/bind 钱包地址` 进行绑定。")
            return
        if points >= config.MIN_WITHDRAW_POINTS:
            database.reset_points(user_id)
            await reply(f"已申请提现 {points} 积分，请等待管理员发放。")
            await context.bot.send_message(
                chat_id=config.ADMIN_ID,
                text=f"用户 @{username} 提现 {points} 积分到 {wallet}"
            )
        else:
            await reply(f"积分不足 {config.MIN_WITHDRAW_POINTS}，无法提现。")
    else:
        await reply("暂无积分记录。")


async def settoken(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.from_user.id != config.ADMIN_ID:
        return
    coin = ' '.join(context.args)
    if coin:
        config.DEFAULT_COIN = coin
        await update.message.reply_text(f"奖励币种已设置为: {coin}")
    else:
        await update.message.reply_text("命令格式 `/settoken 币种名称`")


from telegram import InlineKeyboardMarkup, InlineKeyboardButton

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔗 绑定钱包", callback_data='bind')],
        [InlineKeyboardButton("📊 查看积分", callback_data='balance')],
        [InlineKeyboardButton("💰 提现", callback_data='withdraw')],
        [InlineKeyboardButton("❓ 帮助", callback_data='help')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🤖 你好，我是聊天挖矿机器人！\n\n请选择操作：",
        reply_markup=reply_markup
    )

# ✅ 添加按钮回调处理函数
async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data
    if data == 'bind':
        await query.message.reply_text("请私聊我并发送 `/bind 钱包地址` 进行绑定。")
    elif data == 'balance':
        await balance(update, context)  # 复用 balance 命令逻辑
    elif data == 'withdraw':
        await withdraw(update, context)  # 复用 withdraw 命令逻辑
    elif data == 'help':
        await query.message.reply_text(
            "我是聊天积分机器人，你只需在群里正常聊天，就能获得奖励积分。\n积分满100可通过 /withdraw 提现。"
        )
    else:
        await query.message.reply_text("未知操作")

