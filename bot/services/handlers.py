from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, LabeledPrice, ContentType, PreCheckoutQuery
import services.keyboard as kb
import config


router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}!\nДобро пожаловать в сообщество МЕНТАЛИТЕТ ПОБЕДИТЕЛЯ!', reply_markup=kb.mainMenu)

@router.message(F.text == 'Подписка🔔')
async def mainMenu_subscribe(message: Message):
    await message.answer(f'Ты можешь купить подписку за {config.PRICE_SUBSCRIBE}{config.CURRENCY}', reply_markup=kb.btnBuy)

@router.callback_query(F.data == 'buySubscribe')
async def callback_buySubscribe(callback: CallbackQuery):
    await callback.answer()
    #await callback.message.answer('Вы купили подписку ✅')
    prices = [LabeledPrice(label="Подписка", amount=config.PRICE_SUBSCRIBE*100)]  # сумма в копейках (100.00 RUB)
    await callback.message.bot.send_invoice(
        chat_id=callback.message.chat.id,
        title="Оформление подписки",
        description="Вам станет доступен весь контент закрытого канала!",
        payload="order_12345",  # уникальный идентификатор заказа
        provider_token=config.PAYMENT_TEST_TOKEN,
        currency=config.CURRENCY,  # обязательно в верхнем регистре ISO-4217
        prices=prices,
        start_parameter="example-payment",
        #photo_url="https://opt.24poligon.ru/upload/cssinliner_webp/medialibrary/952/7itcdesrb6aab04ishl26r702ay54mrr.webp",
    )

# ПРАВИЛЬНЫЙ СИНТАКСИС для pre_checkout_query
@router.pre_checkout_query()
async def checkout(pre_checkout_query: PreCheckoutQuery):
    # Получаем bot из контекста
    await pre_checkout_query.bot.answer_pre_checkout_query(
        pre_checkout_query.id,
        ok=True
    )

# ПРАВИЛЬНЫЙ СИНТАКСИС для successful_payment
@router.message(F.content_type == ContentType.SUCCESSFUL_PAYMENT)
async def got_payment(message: Message):
    payment_info = message.successful_payment.to_python()
    await message.answer(f"✅ Оплата прошла успешно!\nДетали: {payment_info}")