from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from keyboards.reply.menu import main_menu,delivery_type,yetkazish,olib_ketish
from states.main import Example
from aiogram.dispatcher import FSMContext


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await Example.menu.set()
    await message.answer(f"Salom, {message.from_user.full_name}!\n\n<b>Bosh Menyu</b>",
                    reply_markup=main_menu)
    
    
@dp.message_handler(state=Example.menu)
async def menu_handler(message: types.Message, state: FSMContext):
    if message.text == "🍽 Menyu":
        await Example.delivery_type.set()
        await message.answer("Buyurtmani o'zingiz olib keting yoki Yetkazib berishni tanlang",
                        reply_markup=delivery_type)
    elif message.text == "☎️ Biz bilan aloqa":
        await message.answer("Agar sizda Savollar/Shikoyatlar/Takliflar bo'lsa bizga yozishingiz mumkin: <b>@Street77tech_bot</b>\n☎️ Telefon raqam: <b>+99871-200-73-73 / +99871 200-86-86</b>")
        
    
@dp.message_handler(state=Example.delivery_type)
async def delivery_type_handler(message: types.Message, state: FSMContext):
    if message.text == "🚙 Yetkazib berish":
        await Example.yetkazish.set()
        await message.answer("Buyurtmangizni qayerga yetkazib berish kerak 🚙? Agar lokatsiyangizni📍 yuborsangiz, sizga eng yaqin filialni va yetkazib berish xarajatlarini aniqlaymiz 💵",
                        reply_markup=yetkazish)
    elif message.text == "🏃 Olib ketish":
        await Example.olib_ketish.set()
        await message.answer("Qayerdasiz 👀? Agar lokatsiyangizni📍 yuborsangiz, sizga eng yaqin filialni aniqlaymiz"
                            ,reply_markup=olib_ketish)
    elif message.text == "⬅️ Ortga":
        await Example.menu.set()
        await message.answer(f"Salom, {message.from_user.full_name}!\n\n<b>Bosh Menyu</b>",
                    reply_markup=main_menu)
   
@dp.message_handler(state=Example.yetkazish)
async def delivery_type_handler(message: types.Message, state: FSMContext):
    if message.text == "⬅️ Ortga":
        await Example.delivery_type.set()
        await message.answer("Buyurtmani o'zingiz olib keting yoki Yetkazib berishni tanlang",
                        reply_markup=delivery_type)
        
       
