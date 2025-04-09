import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
ADMIN_ID = int(os.getenv('ADMIN_ID'))

COOLDOWN_SECONDS = 60  # 发言积分冷却60秒
MIN_WITHDRAW_POINTS = 100  # 最低提现积分
DEFAULT_COIN = "BNB"  # 默认奖励币种（管理员可改）
