from aiogram import F, Router, Bot
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, LabeledPrice, ContentType, PreCheckoutQuery, ChatInviteLink, InputFile
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
async def got_payment(message: Message, bot: Bot):
    payment= message.successful_payment

    try:
        # Создаем уникальную ссылку-приглашение
        invite_link = await bot.create_chat_invite_link(
            chat_id=config.CHANNEL_ID,
            name=f"Subscribe_{message.from_user.id}",
            expire_date=None,  # Без времени истечения
            member_limit=1,  # Только для одного использования
            creates_join_request=False
        )

        # Отправляем ссылку пользователю
        await message.answer(
            f"✅ Оплата прошла успешно!\n"
            f"💳 Сумма: {payment.total_amount / 100} {payment.currency}\n\n"
            f"🎉 Добро пожаловать в закрытый канал!\n"
            f"Ваша персональная ссылка:\n{invite_link.invite_link}",
            reply_markup=kb.mainMenu
        )
    except:
        await message.answer(
            "✅ Оплата прошла успешно!\n"
            "Произошла техническая ошибка при создании доступа. "
            "Свяжитесь с администратором.",
            reply_markup=kb.mainMenu
        )


@router.message(F.text == "О НАС🔎")
async def about(message: Message):
    await message.answer("Шурихин Владислав Андреевич\n644919186520\nСамозанятый почта - vlad.shurikhin@inbox.ru\nномер для обратной связи - 89297777381\nписьменная обратная связь(будет отвечать быстрее) t.me/mentalitet64")

@router.message(F.text == "Договор оферты📌")
async def about(message: Message):
    file = InputFile(path="../resources/files/oferta_644919186520.docx")
    await message.answer_document(file, caption="Файл договора оферты:")

@router.message(F.text == "СМЫСЛ МЕНТАЛИТЕТА ПОБЕДИТЕЛЯ📢")
async def about(message: Message):
    await message.answer("ФУНДАМЕНТАЛЬНОЕ ХЛАДНОКРОВИЕ — ЭТО ПРО:\n\n"
                        "Протоколы, а не лозунги. Четкие алгоритмы действий в стрессе.\n\n"
                            
                        "Деконструкцию твоих срывов до механики и пошаговый разбор.\n\n"
                            
                        "Перевод твоей ярости в тактическое преимущество на площадке.\n\n"
                            
                       "Управление внутренним диалогом, чтобы он работал на тебя, а не против.\n\n"
                            
                        "ЧТО Я ДАЮ:\n\n"
                            
                        "Я не продаю вдохновение. Оно сгорает. Я даю систему. Фундаментальное хладнокровие — это протоколы действий в стрессе. Деконструкция твоих срывов до механики. Перевод ярости в тактическое преимущество.\n\n"

                        "Полная история (https://t.me/vicmentall/3)\n\n")

@router.message(F.text == "О НАС🔎")
async def about(message: Message):
    await message.answer("Стоимость,условия,возврат и суть работы. (кнопка)\n\n"

                        "СТОИМОСТЬ:\n" 
                        "СОСТАВЛЯЕТ 1000 РОССИЙСКИЙ РУБЛЕЙ И В НЕЕ ВХОДИТ ДОСТУП К МОИМ КОНСУЛЬТАЦИЯМ,МЫСЛЯМ,ОПЫТУ,СХЕМАМ И РАЗБОРАМ ВНУТРИ ЗАКРЫТОГО РЕСУРСА\n\n"

                        "Суть работы:"
                        "После оплаты подписки бот выдает ссылку на закрытый теллеграм канал. Воспользоваться ссылкой может только ОДИН человек. Срок действия ссылки безграничный.\n\n"

                        "Условия и возвраты\n"

                        "Вернуть деньги получится ТОЛЬКО в случае технических неполадок с ботом. В случае,если вы передумали после покупки деньги вернуть не получится")
