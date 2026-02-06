import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from aiogram.filters import CommandStart

# tikai šādi:
BOT_TOKEN = "8536903164:AAFd7MZ4KpBJamcoTUajjHmdWzf1RfX-OxY"



bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Glabājam valodu
user_language = {}

texts = {
    "ru": {
        "start": "Choose language",
        "text1": """Привет!
Если ты читаешь это, значит, скорее всего, ты тоже когда-то задавался вопросом: «Как люди реально зарабатывают? Откуда берётся пассивный доход? И почему у других получается, а у меня пока нет?»

Я тоже когда-то был именно в этой точке.
Работал, пробовал разные направления в бизнесе, совершал ошибки, терял деньги и время. Бывали моменты, когда казалось, что я много делаю, но стою на месте.

Переломный момент наступил тогда, когда я понял одну важную вещь:
деньги зарабатываются не количеством часов, а правильно выстроенными системами.

Я начал развивать цифровой бизнес с автоматизированной системой продаж — цифровые продукты, онлайн-курсы и партнёрские программы, которые работают 24/7. Один раз выстраиваешь систему правильно — и она начинает приносить доход даже без постоянного участия.

Сегодня этот бизнес:

👉 приносит мне стабильный пассивный доход (2000-3500$/месяц),
👉 позволяет работать из любой точки мира,
👉 и даёт свободу, о которой раньше можно было только мечтать.

Если интересно, читай дальше""",
        "text2": """За всё это время я собрал огромное количество информации.

Я многому научился — как самостоятельно, так и у профессионалов, которые уже давно работают с системами, приносящими стабильный доход.

Я:
👉 учился у опытных предпринимателей и наставников,
👉 работал в разных компаниях и видел, как бизнес работает изнутри,
👉 тестировал различные модели на практике — что работает, а что нет.

Самое главное — я не просто изучал теорию, я проверял всё на практике. Многое, о чём говорят в интернете, на самом деле не работает. Именно этот опыт я считаю самым ценным.

Со временем мне удалось:

👉 отобрать только то, что реально даёт результат,
👉 понять, как объединить знания в одну понятную систему,
👉 и создать структуру, которую могут повторить другие.

Именно поэтому я создал этот курс.
Не как теоретическое обучение, а как практическое руководство, где я делюсь всем самым важным, что сам освоил и проверил на практике.

Этот курс для тех, кто:
👉 не хочет годами экспериментировать и допускать ошибки,
👉 хочет учиться на реальном опыте,
👉 и готов начинать строить свои доходы умнее.

Если ты здесь — это не случайно.
Всё, что я собирал годами, теперь структурировано в одном месте.""",
        "course_short": """📚 Содержание курса

Курс состоит из 6 ключевых модулей, каждый из которых даст тебе практические знания и инструменты для реального заработка:

1️⃣ Основы бизнеса
2️⃣ Виды доходов и бизнес-модели
3️⃣ Практические схемы заработка на которых ты уже сможешь зарабатывать
4️⃣ Программы и инструменты
5️⃣ Типичные ошибки и их решения
6️⃣ Как начать с нуля

Нажимай если интересно!""",
        "course_full": """Готов начать зарабатывать?

Теперь, когда ты видишь весь курс и понимаешь, какие пошаговые знания и инструменты тебя ждут, самое время действовать.

👉 Ты получаешь проверенные схемы заработка, которые реально работают.
👉 Ты знаешь, какие программы использовать, чтобы ускорить процесс.
👉 Ты избежишь типичных ошибок, которые останавливают большинство новичков.

Не откладывай успех на завтра!
Каждый день, который ты ждёшь, — это упущенные возможности и деньги, которые могли бы работать на тебя.

👉 Нажми «Получить курс» и сделай первый шаг к своему пассивному доходу и финансовой свободе уже сегодня!""",
        "buy": """Цена курса всего 15$ 
Оплата в криптовалюте:
Адрес кошелька👇 0x75eaf979db1869d875a8940f521454a8d012fba2 
ERC20
Криптовалюта: usdc
После успешной оплаты свяжитесь со мной и пришлите скриншот перевода (с подписью «курс»).
@arnisarnis"""
    },
    "en": {
        "start": "Choose language",
        "text1": """Hi!
If you’re reading this, it probably means that at some point you’ve asked yourself: “How do people really make money? Where does passive income come from? And why are others successful while I’m not… yet?”

I was in that exact position too.
I worked, tried different business directions, made mistakes, lost money and time. There were moments when it felt like I was doing a lot, but not moving forward at all.

The turning point came when I realized one important thing:
money is earned not by the number of hours you work, but by properly built systems.

I started developing a digital business with an automated sales system — digital products, online courses, and affiliate programs that work 24/7. Once you set up the system correctly, it starts generating income even without constant involvement.

Today, this business:

👉 brings me a stable passive income ($2,000–$3,500/month),
👉 allows me to work from anywhere in the world,
👉 and gives the freedom I could only dream of before.

If you’re interested, keep reading""",
        "text2": """During all this time, I have gathered a huge amount of information.

I have learned a lot — both on my own and from professionals who have long been working with systems that generate stable income.

I:

👉 studied under experienced entrepreneurs and mentors,
👉 worked in different companies and saw how business operates from the inside,
👉 tested various models in practice — what works and what doesn’t.

The most important thing — I didn’t just study theory, I verified everything in practice. Much of what is talked about online simply doesn’t work. This real experience is what I consider most valuable.

Over time, I managed to:

filter out only what truly delivers results,
understand how to combine knowledge into one clear system,
and create a structure that others can replicate.

That is exactly why I created this course.
Not as a theoretical training, but as a practical guide where I share everything crucial that I personally learned and tested in practice.

This course is for those who:

don’t want to spend years experimenting and making mistakes,
want to learn from real experience,
and are ready to start building their income smarter.

If you’re here — it’s not by chance.
Everything I have gathered over the years is now structured in one place.""",
        "course_short": """📚 Course Content

The course consists of 6 key modules, each providing you with practical knowledge and tools for real earnings:

1️⃣ Business Fundamentals
2️⃣ Types of Income and Business Models
3️⃣ Practical earning schemes you can start making money from right away
4️⃣ Programs and Tools
5️⃣ Common Mistakes and How to Fix Them
6️⃣ How to Start from Scratch

Click if you’re interested! ✅""",
        "course_full": """Ready to Start Earning?

Now that you’ve seen the entire course and understand the step-by-step knowledge and tools that await you, it’s time to take action.

👉 You’ll get proven earning methods that actually work.
👉 You’ll know which programs to use to speed up the process.
👉 You’ll avoid common mistakes that stop most beginners.

Don’t put your success off until tomorrow!
Every day you wait is a missed opportunity and money that could be working for you.

👉 Click “Get the Course” and take your first step toward passive income and financial freedom today!""",
        "buy": """The course costs only $15 
Payment in cryptocurrency:
Wallet address 👇 0x75eaf979db1869d875a8940f521454a8d012fba2 
ERC20
Coin: usdc
After successful payment, contact me and send a screenshot of the transfer (with the caption ‘Course’).
@arnisarnis"""
    }
}

# START
@dp.message(CommandStart())
async def start(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru"),
            InlineKeyboardButton(text="🇬🇧 English", callback_data="lang_en")
        ]
    ])
    await message.answer(texts["en"]["start"], reply_markup=keyboard)

# LANGUAGE SELECT
@dp.callback_query(lambda c: c.data.startswith("lang_"))
async def choose_language(callback: CallbackQuery):
    lang = callback.data.split("_")[1]
    user_language[callback.from_user.id] = lang
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Нажимай" if lang=="ru" else "Continuation 👉", callback_data="read_more")]
    ])
    await callback.message.edit_text(texts[lang]["text1"], reply_markup=keyboard)

# READ MORE
@dp.callback_query(lambda c: c.data == "read_more")
async def read_more(callback: CallbackQuery):
    lang = user_language.get(callback.from_user.id, "en")
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬇️ Узнать больше о курсе ⬇️" if lang=="ru" else "Learn More About the Course", callback_data="course_short")]
    ])
    await callback.message.edit_text(texts[lang]["text2"], reply_markup=keyboard)

# COURSE SHORT
@dp.callback_query(lambda c: c.data == "course_short")
async def course_short(callback: CallbackQuery):
    lang = user_language.get(callback.from_user.id, "en")
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Хочу курс" if lang=="ru" else "I want the course", callback_data="course_full")]
    ])
    await callback.message.edit_text(texts[lang]["course_short"], reply_markup=keyboard)

# COURSE FULL
@dp.callback_query(lambda c: c.data == "course_full")
async def course_full(callback: CallbackQuery):
    lang = user_language.get(callback.from_user.id, "en")
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Получить курс 📚" if lang=="ru" else "Get the Course 📚", callback_data="buy")]
    ])
    await callback.message.edit_text(texts[lang]["course_full"], reply_markup=keyboard)

# BUY
@dp.callback_query(lambda c: c.data == "buy")
async def buy(callback: CallbackQuery):
    lang = user_language.get(callback.from_user.id, "en")
    await callback.message.edit_text(texts[lang]["buy"])

# RUN
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
