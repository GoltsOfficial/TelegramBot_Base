# modules/admin_panel/__init__.py
from aiogram import Router

# Импорт роутеров всех разделов админки
from .analytics.handlers import router as analytics_router
from .broadcast.handlers import router as broadcast_router
from .ecommerce.handlers import router as ecommerce_router
from .media.handlers import router as media_router
from .referral.handlers import router as referral_router
from .security.handlers import router as security_router
from .users.handlers import router as users_router

admin_router = Router()

# Подключаем все подроутеры
admin_router.include_router(analytics_router)
admin_router.include_router(broadcast_router)
admin_router.include_router(ecommerce_router)
admin_router.include_router(media_router)
admin_router.include_router(referral_router)
admin_router.include_router(security_router)
admin_router.include_router(users_router)
