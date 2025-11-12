from aiogram.filters import BaseFilter
from aiogram.types import Message
from tgbot.config import Config


class AdminFilter(BaseFilter):
    is_admin: bool = True  # Default: True → checks for admin users

    async def __call__(self, obj: Message, config: Config) -> bool:
        """Return True if the user's admin status matches self.is_admin"""
        user_id = obj.from_user.id if obj.from_user else None
        return (user_id in config.tg_bot.admin_ids) == self.is_admin


# ✅ Reusable alias (so you can write IsAdmin() in handlers)
IsAdmin = AdminFilter