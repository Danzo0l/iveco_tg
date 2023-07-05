import re
from aiogram.types import ReplyKeyboardRemove
from aiogram import types
from create_bot import dp
from dp import push, check_user_existence, push_only
from q import questions


@dp.message_handler(commands=['start'], state='*')
async def start(message: types.Message):
    if check_user_existence(message.from_user.username):
        await message.answer("Вы уже проходили тестирование, попробуйте пройти позже")
    else:
        await message.answer("Добро пожаловать! Готовы пройти опрос?", reply_markup=types.ReplyKeyboardMarkup(
            keyboard=[[types.KeyboardButton('Готов')]],
            resize_keyboard=True,
            one_time_keyboard=True
        ))
        await dp.current_state().set_state('ready')


@dp.message_handler(state='ready', content_types=types.ContentTypes.TEXT)
async def answer_ready(message: types.Message, state: dict):
    if message.text == 'Готов':
        await message.answer('Отлично! Давайте начнем. Ваше ФИО:', reply_markup=ReplyKeyboardRemove())
        await state.update_data(question1=message.text)
        await dp.current_state().set_state('question1')


@dp.message_handler(state='question1', content_types=types.ContentTypes.TEXT)
async def answer_question1(message: types.Message, state: dict):
    answer1 = message.text
    await state.update_data(question1=answer1)
    await message.answer('1. Ваш контактный номер телефона')
    await dp.current_state().set_state('question_phone')


@dp.message_handler(state='question_phone', content_types=types.ContentTypes.TEXT)
async def answer_question1(message: types.Message, state: dict):
    answer_19 = message.text
    if not re.match(r"^(?:\+7|8)\d{10}$", answer_19):
        await message.answer("Некорректный номер телефона")
        return
    await state.update_data(question19=answer_19)
    user_answers_only = await state.get_data()
    push_only(message.from_user.username, user_answers_only)
    await message.answer('2. Ваш возраст:')
    await dp.current_state().set_state('question2')


@dp.message_handler(state='question2', content_types=types.ContentTypes.TEXT)
async def answer_question2(message: types.Message, state: dict):
    answer2 = message.text

    if not answer2.isdigit() or int(answer2) < 0:
        await message.answer("Некорректный возраст")
        return

    await state.update_data(question2=answer2)
    await message.answer('3. Ваш опыт в продажах:', reply_markup=types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton('нет')],
            [types.KeyboardButton('до 1 года')],
            [types.KeyboardButton('1-3 года')],
            [types.KeyboardButton('более 3-х лет')],
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    ))
    await dp.current_state().set_state('question3')


@dp.message_handler(state='question3', content_types=types.ContentTypes.TEXT)
async def answer_question3(message: types.Message, state: dict):
    answer3 = message.text

    # Валидатор: проверяем, что ответ является одним из вариантов на кнопках
    valid_answers = ['нет', 'до 1 года', '1-3 года', 'более 3-х лет']
    if answer3 not in valid_answers:
        await message.answer("Пожалуйста, выберите ответ с помощью клавиатуры.")
        return

    await state.update_data(question3=answer3)
    await message.answer('4. С какими сегментами клиентов работали?', reply_markup=types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton('В2В')],
            [types.KeyboardButton('В2С')],
            [types.KeyboardButton('все вышеперечисленное')],
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    ))
    await dp.current_state().set_state('question4')


@dp.message_handler(state='question4', content_types=types.ContentTypes.TEXT)
async def answer_question4(message: types.Message, state: dict):
    answer4 = message.text

    valid_answers = ['В2В', 'В2С', 'все вышеперечисленное']
    if answer4 not in valid_answers:
        await message.answer("Пожалуйста, выберите ответ с помощью клавиатуры.")
        return

    await state.update_data(question4=answer4)
    await message.answer('5. Какие были лиды?', reply_markup=types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton('входящие')],
            [types.KeyboardButton('холодные')],
            [types.KeyboardButton('все вышеперечисленное')],
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    ))
    await dp.current_state().set_state('question5')


@dp.message_handler(state='question5', content_types=types.ContentTypes.TEXT)
async def answer_question5(message: types.Message, state: dict):
    answer5 = message.text
    valid_answers = ['входящие', 'холодные', 'все вышеперечисленное', 'более 3-х лет']
    if answer5 not in valid_answers:
        await message.answer("Пожалуйста, выберите ответ с помощью клавиатуры.")
        return
    await state.update_data(question5=answer5)
    await message.answer('6. Перечислите этапы продаж:', reply_markup=ReplyKeyboardRemove())
    await dp.current_state().set_state('question6')


@dp.message_handler(state='question6', content_types=types.ContentTypes.TEXT)
async def answer_question6(message: types.Message, state: dict):
    answer6 = message.text
    await state.update_data(question6=answer6)
    await message.answer('7. Через что формируется ценность продукта у клиента при презентации?',
                         reply_markup=ReplyKeyboardRemove())
    await dp.current_state().set_state('question7')


@dp.message_handler(state='question7', content_types=types.ContentTypes.TEXT)
async def answer_question7(message: types.Message, state: dict):
    answer7 = message.text
    await state.update_data(question7=answer7)
    await message.answer('8. Что такое "дожим"? Перечислите инструменты дожима', reply_markup=ReplyKeyboardRemove())
    await dp.current_state().set_state('question8')


@dp.message_handler(state='question8', content_types=types.ContentTypes.TEXT)
async def answer_question8(message: types.Message, state: dict):
    answer8 = message.text
    await state.update_data(question8=answer8)
    await message.answer('9. Что такое "ключевой этап продаж"?', reply_markup=ReplyKeyboardRemove())
    await dp.current_state().set_state('question9')


@dp.message_handler(state='question9', content_types=types.ContentTypes.TEXT)
async def answer_question9(message: types.Message, state: dict):
    answer9 = message.text
    await state.update_data(question9=answer9)
    await message.answer(
        '10. Какой итоговый продукт генерирует Менеджер по поиску и привлечению новых клиентов?',
        reply_markup=ReplyKeyboardRemove()
    )
    await dp.current_state().set_state('question10')


@dp.message_handler(state='question10', content_types=types.ContentTypes.TEXT)
async def answer_question10(message: types.Message, state: dict):
    answer10 = message.text
    await state.update_data(question10=answer10)
    await message.answer(
        '11. Какими инструментами/ресурсами Вы пользуетесь для поиска потенциальных клиентов?',
        reply_markup=ReplyKeyboardRemove()
    )
    await dp.current_state().set_state('question11')


@dp.message_handler(state='question11', content_types=types.ContentTypes.TEXT)
async def answer_question11(message: types.Message, state: dict):
    answer11 = message.text
    await state.update_data(question11=answer11)
    await message.answer(
        '12. Цель первого телефонного разговора с потенциальным клиентом:\n\n'
        '1. <i>Продажа</i>\n'
        '2. <i>Создание благоприятного впечатления о себе и своей компании</i>\n'
        '3. <i>Достижение договоренности о дальнейшем взаимодействии</i>\n'
        '4. <i>Все перечисленные</i>\n'
        '5. <i>Ни одно из перечисленных</i>',
        parse_mode=types.ParseMode.HTML,
        reply_markup=types.ReplyKeyboardMarkup(
            keyboard=[
                [
                    types.KeyboardButton('1'),
                    types.KeyboardButton('2'),
                    types.KeyboardButton('3'),
                    types.KeyboardButton('4'),
                    types.KeyboardButton('5'),
                ],
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )
    await dp.current_state().set_state('question12')


@dp.message_handler(state='question12', content_types=types.ContentTypes.TEXT)
async def answer_question12(message: types.Message, state: dict):
    answer12 = message.text
    valid_answers = ['1', '2', '3', '4', '5']
    if answer12 not in valid_answers:
        await message.answer("Пожалуйста, выберите ответ с помощью клавиатуры.")
        return
    await state.update_data(question12=answer12)
    await message.answer(
        '13. Цель первого телефонного разговора с потенциальным клиентом:\n\n'
        '1. <i>Можно преподнести свое предложение в наиболее выгодном свете</i>\n'
        '2. <i>Можно познакомиться с девушкой</i>\n'
        '3. <i>Можно собрать дополнительную информацию о потенциальном клиенте</i>\n'
        '4. <i>Все перечисленные</i>\n'
        '5. <i>Никаких</i>',
        parse_mode=types.ParseMode.HTML,
        reply_markup=types.ReplyKeyboardMarkup(
            keyboard=[
                [
                    types.KeyboardButton('1'),
                    types.KeyboardButton('2'),
                    types.KeyboardButton('3'),
                    types.KeyboardButton('4'),
                    types.KeyboardButton('5'),
                ],
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )
    await dp.current_state().set_state('question13')


@dp.message_handler(state='question13', content_types=types.ContentTypes.TEXT)
async def answer_question13(message: types.Message, state: dict):
    answer13 = message.text
    valid_answers = ['1', '2', '3', '4', '5']
    if answer13 not in valid_answers:
        await message.answer("Пожалуйста, выберите ответ с помощью клавиатуры.")
        return
    await state.update_data(question13=answer13)
    await message.answer(
        '14. Цель первого телефонного разговора с потенциальным клиентом:\n\n'
        '1. <i>Уточняющие вопросы</i>\n'
        '2. <i>Ситуационные вопросы</i>\n'
        '3. <i>Метод SPIN</i>\n'
        '4. <i>Личный дар убеждения</i>\n'
        '5. <i>Все перечисленное</i>',
        parse_mode=types.ParseMode.HTML,
        reply_markup=types.ReplyKeyboardMarkup(
            keyboard=[
                [
                    types.KeyboardButton('1'),
                    types.KeyboardButton('2'),
                    types.KeyboardButton('3'),
                    types.KeyboardButton('4'),
                    types.KeyboardButton('5'),
                ],
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )
    await dp.current_state().set_state('question14')


@dp.message_handler(state='question14', content_types=types.ContentTypes.TEXT)
async def answer_question14(message: types.Message, state: dict):
    answer14 = message.text

    valid_answers = ['1', '2', '3', '4', '5']
    if answer14 not in valid_answers:
        await message.answer("Пожалуйста, выберите ответ с помощью клавиатуры.")
        return

    await state.update_data(question14=answer14)
    await message.answer(
        '15. На этапе заключения сделки с покупателем, необходимы:\n\n'
        '1. <i>Твердость и решительность</i>\n'
        '2. <i>Лояльность и гибкость</i>\n'
        '3. <i>Понимание потребностей клиента</i>\n'
        '4. <i>Презентационные навыки</i>\n'
        '5. <i>Грамотная работа с возражениями</i>',
        parse_mode=types.ParseMode.HTML,
        reply_markup=types.ReplyKeyboardMarkup(
            keyboard=[
                [
                    types.KeyboardButton('1'),
                    types.KeyboardButton('2'),
                    types.KeyboardButton('3'),
                    types.KeyboardButton('4'),
                    types.KeyboardButton('5'),
                ],
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )
    await dp.current_state().set_state('question15')


@dp.message_handler(state='question15', content_types=types.ContentTypes.TEXT)
async def answer_question15(message: types.Message, state: dict):
    answer15 = message.text

    valid_answers = ['1', '2', '3', '4', '5']
    if answer15 not in valid_answers:
        await message.answer("Пожалуйста, выберите ответ с помощью клавиатуры.")
        return

    await state.update_data(question15=answer15)
    await message.answer(
        '16. На этапе заключения сделки с покупателем, необходимы:\n\n'
        '1. <i>Знание продукта, владение техникой продаж, уверенность в себе, энтузиазм</i>\n'
        '2. <i>Компетентность, знание основ маркетинга, владение техникой продаж</i>\n'
        '3. <i>Понимание специфики бизнеса,умение руководить,умение совершать сделки Первое и второе</i>\n'
        '4. <i>Ни одно из них</i>\n',
        parse_mode=types.ParseMode.HTML,
        reply_markup=types.ReplyKeyboardMarkup(
            keyboard=[
                [
                    types.KeyboardButton('1'),
                    types.KeyboardButton('2'),
                    types.KeyboardButton('3'),
                    types.KeyboardButton('4'),
                ],
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )
    await dp.current_state().set_state('question16')


@dp.message_handler(state='question16', content_types=types.ContentTypes.TEXT)
async def answer_question16(message: types.Message, state: dict):
    answer16 = message.text

    valid_answers = ['1', '2', '3', '4']
    if answer16 not in valid_answers:
        await message.answer("Пожалуйста, выберите ответ с помощью клавиатуры.")
        return

    await state.update_data(question16=answer16)
    await message.answer(
        '17. Был ли у Вас опыт ведения собственного бизнеса?\n\n',
        parse_mode=types.ParseMode.HTML,
        reply_markup=types.ReplyKeyboardMarkup(
            keyboard=[
                [
                    types.KeyboardButton('нет'),
                    types.KeyboardButton('ИП'),
                    types.KeyboardButton('ООО'),
                ],
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )
    await dp.current_state().set_state('question17')


@dp.message_handler(state='question17', content_types=types.ContentTypes.TEXT)
async def answer_question17(message: types.Message, state: dict):
    answer17 = message.text

    valid_answers = ['нет', 'ИП', 'ООО']
    if answer17 not in valid_answers:
        await message.answer("Пожалуйста, выберите ответ с помощью клавиатуры.")
        return

    await state.update_data(question17=answer17)
    await message.answer(
        '18. Есть ли опыт работы с СРМ системой?',
        parse_mode=types.ParseMode.HTML,
        reply_markup=types.ReplyKeyboardMarkup(
            keyboard=[
                [
                    types.KeyboardButton('да'),
                    types.KeyboardButton('нет'),
                ],
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )
    await dp.current_state().set_state('question18')


@dp.message_handler(state='question18', content_types=types.ContentTypes.TEXT)
async def answer_question18(message: types.Message, state: dict):
    answer18 = message.text

    valid_answers = ['да', 'нет']
    if answer18 not in valid_answers:
        await message.answer("Пожалуйста, выберите ответ с помощью клавиатуры.")
        return

    await state.update_data(question18=answer18)
    user_answers = await state.get_data()

    push(message.from_user.username, user_answers)
    await message.answer("Опрос завершен!  👍 \nCпасибо что оставили заявку.\n"
                         "☎️  Мы получили ответы и свяжемся с Вами в ближайшее время")

    await state.finish()


def f():
    pass
