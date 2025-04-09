# 🪙 Telegram Chat Mining Bot

A minimalist Telegram chat mining bot that rewards users with points for participating in group conversations. Once they reach a certain threshold, users can bind their wallet address and request a payout in any crypto token (e.g. BNB, MATIC, TON) preconfigured by the admin.

Built with Python using `python-telegram-bot`, this bot is ideal for community engagement or airdrop-style reward programs.

---

## ✨ Features

- ✅ Listens to group messages and tracks user activity
- ✅ Implements cooldown logic (1 point every 60 seconds max per user)
- ✅ Users can bind a wallet address via `/bind`
- ✅ Users can check their balance via `/balance`
- ✅ Users can request a withdrawal via `/withdraw`
- ✅ Admin can set the reward token via `/settoken`
- ✅ Supports button-based UI via `/menu` with inline buttons

---

## 🧱 Project Structure

```bash
telegram_bot/
├── bot.py              # Bot launcher
├── commands.py         # Command and button handlers
├── config.py           # Global settings (Token, cooldown, thresholds)
├── database.py         # SQLite-based point and wallet storage
├── requirements.txt    # Required Python libraries
├── .env                # Telegram token and admin ID (private)
└── data.db             # SQLite DB file (auto-generated)
⚙️ Setup Instructions
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/yourname/telegram-chat-mining-bot.git
cd telegram-chat-mining-bot
2. (Optional) Create a virtual environment
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Create a .env file
In the root folder, create a .env file:

ini
Copy
Edit
TOKEN=YourTelegramBotToken
ADMIN_ID=YourNumericTelegramUserID
To get your numeric Telegram ID, use @userinfobot

🚀 Run the bot
bash
Copy
Edit
python bot.py
✅ Group Setup Guide (Important)
Disable Privacy Mode (required!)

Chat with @BotFather

/mybots → select your bot → Bot Settings

Group Privacy → select Turn Off

Add the bot to your group

Group settings → Add member → Search your bot → Add

Type /menu or simply start chatting to earn points!

💬 Available Commands
Command	Description
/bind <addr>	Bind your crypto wallet via private chat
/balance	Check your point balance & wallet
/withdraw	Request a token payout
/menu	Show interactive button menu
/settoken	Admin-only: set the reward token
🧠 Mining Logic
Every user gets 1 point per 60 seconds max (cooldown-based)

Meaningless spam is ignored (basic cooldown control)

Once a user reaches the minimum threshold (default 100 points), they can request a payout

Withdrawals are sent to the bound wallet address, processed by admin manually or via script

🛠 Data Storage
All user activity and wallet bindings are stored in data.db (SQLite)

You can inspect or export data using sqlite3 CLI or any SQLite browser

🔐 Security Tips
Keep your .env file private – never commit your token or admin ID

If you later automate token transfers, protect any private keys used to send tokens!

💡 Future Ideas (Pull Requests Welcome!)
Group leaderboard /leaderboard

Blockchain auto-transfer integration (via Web3)

Admin dashboard with web UI

Multi-token and multi-group support

NFT or gamified reward extensions

📄 License
MIT License

🤝 Contact & Contribution
Feel free to submit issues or PRs. You’re welcome to use this bot as a base for your own community reward project!

# telegram_ranking_bot# 🪙 Telegram Chat Mining Bot

一个极简版本的 Telegram 聊天挖矿机器人，用户只需在群中正常发言，即可自动获得积分奖励，积分累计到一定数额后可绑定钱包地址进行提现，管理员可提前设置奖励币种（如 BNB、MATIC、TON 等）。

本项目采用 Python 开发，使用 `python-telegram-bot` 实现群聊监听和用户交互，适合用于社区活跃度激励或空投工具。

---

## ✨ 功能特性

- ✅ 群聊消息监听，自动记录活跃用户积分
- ✅ 冷却时间机制（防刷屏）每人每60秒最多记1次积分
- ✅ 用户私聊绑定钱包地址 `/bind`
- ✅ 用户随时查看余额 `/balance`
- ✅ 用户可申请提现 `/withdraw`，后台人工或脚本发币
- ✅ 管理员可配置奖励币种 `/settoken`
- ✅ 支持按钮菜单操作 `/menu`，点击按钮即执行操作

---

## 🧱 项目结构

```bash
telegram_bot/
├── bot.py              # 启动主程序
├── commands.py         # 所有命令和按钮逻辑处理
├── config.py           # 配置参数，如Token、冷却时间、最低提现额度等
├── database.py         # 积分与钱包信息的本地数据库（SQLite）
├── requirements.txt    # 所需依赖库
├── .env                # Telegram Bot Token & 管理员ID（私密）
└── data.db             # 自动生成的SQLite数据库文件


⚙️ 安装步骤
1. 克隆项目并进入目录
bash
git clone https://github.com/yourname/telegram-chat-mining-bot.git
cd telegram-chat-mining-bot
2. 创建虚拟环境（可选但推荐）
bash
python3 -m venv venv
source venv/bin/activate
3. 安装依赖
bash
pip install -r requirements.txt
4. 创建 .env 文件
在项目根目录创建 .env 文件：

ini
TOKEN=你的TelegramBotToken
ADMIN_ID=你的Telegram账号数字ID（不是@用户名）
如何获取数字 ID？私聊 @userinfobot

🚀 启动机器人
bash
python bot.py
✅ 群组部署说明（重要）
关闭机器人隐私模式（必须）

私聊 @BotFather

/mybots → 选中你的Bot → Bot Settings

Group Privacy → 选择 Turn Off

将机器人添加进群

群设置 → 添加成员 → 搜索Bot名 → 添加

输入 /menu 或直接发消息开始挖矿！

💬 常用命令一览
命令	说明
/bind <地址>	私聊机器人绑定钱包地址
/balance	查看当前积分与绑定钱包
/withdraw	提现（需满一定积分）
/menu	打开交互按钮菜单
/settoken <币种>	管理员设置当前奖励币种
🧠 挖矿逻辑说明
每位用户每 60 秒 内最多获得一次积分

聊天内容需为正常消息，重复刷屏无效

达到最低积分（默认100）后，用户可申请提现

提现记录由机器人通知管理员，由后台人工或脚本发放奖励代币

🛠 数据存储
所有积分、钱包绑定信息存储于 data.db（SQLite）

如需导出积分数据，可使用 sqlite3 或 DB 浏览器

🔐 安全提示
Bot 使用的 Token 和管理员 ID 请保存在 .env 文件中，不要上传到公开仓库

后续如集成自动发币功能，请妥善保管链上钱包私钥！

💡 后续可拓展功能（欢迎PR）
群排行榜 /leaderboard

自动链上发币（结合 Web3.py / Web3.js）

Web 管理面板

不同群支持不同币种与规则

活跃度排行榜 / 积分NFT等创意玩法

📄 License
MIT License

🤝 联系 & 贡献
欢迎提交 PR 或 issue，也欢迎用于你自己的社群积分项目中！
