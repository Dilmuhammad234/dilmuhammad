from aiogram.types import KeyboardButton,ReplyKeyboardMarkup


main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🍽 Menyu")
        ],
        [
            KeyboardButton("📖 Buyurtmalar tarixi"),
            KeyboardButton("✍️ Fikr bildirish")
        ],
        [
            KeyboardButton("ℹ️ Ma'lumot"),
            KeyboardButton("☎️ Biz bilan aloqa")
        ],
        [
            KeyboardButton("⚙️Sozlamalar")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

delivery_type = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🚙 Yetkazib berish"),
            KeyboardButton("🏃 Olib ketish")
        ],
        [
            KeyboardButton("⬅️ Ortga")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)


yetkazish = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("📍 Eng yaqin filialni aniqlash")
        ],
        [
            KeyboardButton("🗺 Mening manzillarim")
        ],
        [
            KeyboardButton("⬅️ Ortga")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

olib_ketish = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("📍 Eng yaqin filialni aniqlash")
        ],
        [
            KeyboardButton("Wok & STREET77 Беруни")
        ],
        [
            KeyboardButton("⬅️ Ortga")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)