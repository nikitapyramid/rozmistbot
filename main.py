import telebot
import sqlite3
from telebot import types
from pprint import pprint
from telegram import Update, ReplyKeyboardRemove
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, ConversationHandler
from auth_data import dogoviroferty, allsitestext,oformzakaztext,oplatatext,keyboard_nextcategorii_detskiymir,keyboard_osnownikategorii, keyboard_nextcategorii_neruhomist,keyboard_nextcategorii_transport,keyboard_nextcategorii_avtozapchasti,keyboard_nextcategorii_robota


#1876949573:AAFxfld7UTDkjnVzIAWhBg0tMP6Lkp9OxWQ
from telebot.types import InlineKeyboardMarkup, ReplyKeyboardMarkup
name = ''
zagolovok_obiavlenia_onlytext = ''
phone_client = ''
osnownaya_kategoriya_todatabase = ''
dopolnitelnaya_kategoriya_todatabase = ''
kontaktitorozmist_in_ogoloshemya_onlytext = ''
price_uslugi_onlytext = ''
text_ogoloshenya_onlytext = ''
regionrozmist_in_ogoloshemya_onlytext = ''
terminrozmist_in_ogoloshemya_onlytext = ''
photopublikatsiy_bezphoto = ''
notoclick = 0
stopclick = 0
notoclick_oformzak = 0
stopclick_oformzak = 0
startingzakaz = 0
nomer_zakaza = 0


age = 0
user_data = {}
bot = telebot.TeleBot("")

button1 = types.KeyboardButton('Сайт')
button2 = types.KeyboardButton('Оформити замовлення')
button3 = types.KeyboardButton("Зв'язатись з менеджером")
button4 = types.KeyboardButton('Оплата та реквізити')
button5 = types.KeyboardButton('Дошки розміщень')
button6 = types.KeyboardButton('Договір Оферти')
buttonotmenazakaza = types.KeyboardButton('Відмінити замовлення')





def sendtoadmin_info():
    global name
    bot.send_message(687554764, "Номер замовлення клієнта : " + nomer_zakaza + "\n\n\nім'я замовника : " + name + "\n\n\nТелефон замовника : " + phone_client + "\n\n\nКатегорія розміщень : " + osnownaya_kategoriya_todatabase + "\n\n\nЗаголовок оголошення : " + zagolovok_obiavlenia_onlytext + "\n\n\nТекст оголошення : " + text_ogoloshenya_onlytext + "\n\n\nЦіна в оголошенні : " + price_uslugi_onlytext + "\n\n\nКонтакти для оголошення : " + kontaktitorozmist_in_ogoloshemya_onlytext + "\n\n\nРегіон для оголошення : " + regionrozmist_in_ogoloshemya_onlytext + "\n\n\nТермін для оголошення : " + terminrozmist_in_ogoloshemya_onlytext + "")
    bot.send_photo(687554764, photopublikatsiy)
    name = ""



def sendtoadmin_info_bezphoto():
    global name
    bot.send_message(687554764, "Номер замовлення клієнта : " + nomer_zakaza + "\n\n\nім'я замовника : " + name + "\n\n\nТелефон замовника : " + phone_client + "\n\n\nКатегорія розміщень : " + osnownaya_kategoriya_todatabase + "\n\n\nЗаголовок оголошення : " + zagolovok_obiavlenia_onlytext + "\n\n\nТекст оголошення : " + text_ogoloshenya_onlytext + "\n\n\nЦіна в оголошенні : " + price_uslugi_onlytext + "\n\n\nКонтакти для оголошення : " + kontaktitorozmist_in_ogoloshemya_onlytext + "\n\n\nРегіон для оголошення : " + regionrozmist_in_ogoloshemya_onlytext + "\n\n\nТермін для оголошення : " + terminrozmist_in_ogoloshemya_onlytext + "")
    bot.send_message(687554764, "Текст який надіслав клієнт замість фото : " + photopublikatsiy_bezphoto + "")
    name = ""


def obnowclickdanni():
    global notoclick
    global stopclick
    global notoclick_oformzak
    global stopclick_oformzak
    global startingzakaz
    notoclick = 0
    stopclick = 0
    notoclick_oformzak = 0
    stopclick_oformzak = 0
    startingzakaz = 0


def obnowclickstartornozakaz():
    global startingzakaz
    startingzakaz = 1




@bot.message_handler(func=lambda m: True,  content_types=["text", "sticker", "pinned_message", "photo", "audio"])
def echo_all(message):
    global startingzakaz
    global name
    if message.text == "/start":
        if(startingzakaz == 0):
            keyboard = types.InlineKeyboardMarkup()
            see_card_rozmist = types.InlineKeyboardButton(text='Подивитись карту розміщень',callback_data='see_card_rozmist')
            keyboard.add(see_card_rozmist)
            oform_zakaz = types.InlineKeyboardButton(text='Оформити замовлення',callback_data='oform_zakaz')
            keyboard.add(oform_zakaz)
            go_to_manager = types.InlineKeyboardButton(text="Зв'язатись з менеджером",callback_data='go_to_manager')
            keyboard.add(go_to_manager)
            bot.send_message(message.from_user.id, text="Сервіс розміщення оголошень Rozmist", reply_markup=keyboard)
            markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup_reply.add(button1, button2, button3, button4, button5, button6)
            bot.send_message(message.from_user.id, text="Вітаю вас", reply_markup=markup_reply)
        else:
            markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup_reply.add(buttonotmenazakaza)
            bot.send_message(message.from_user.id, text="Вибачте я вас не розумію", reply_markup=markup_reply)
    elif message.text == "Оформити замовлення":
        startingzakaz = 1
        if(startingzakaz == 1 and name == ""):
            markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup_reply.add(buttonotmenazakaza)
            bot.send_message(message.from_user.id,"Скажіть будь ласка як мені до вас звертатись", reply_markup=markup_reply)
            bot.register_next_step_handler(message,reg_name)
        else:
            markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup_reply.add(buttonotmenazakaza)
            bot.send_message(message.from_user.id, text="Вибачте я вас не розумію", reply_markup=markup_reply)
    elif message.text == "Відмінити замовлення":
        if(startingzakaz == 0):
            markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup_reply.add(button1, button2, button3, button4, button5, button6)
            bot.send_message(message.from_user.id, text="Вибачте я вас не розумію")
        else:
            keyboardotmenazakaza = types.InlineKeyboardMarkup()
            key_yes_bez_photo = types.InlineKeyboardButton(text='Так', callback_data='yesotmenazakaza')
            keyboardotmenazakaza.add(key_yes_bez_photo)
            key_bez_photo = types.InlineKeyboardButton(text='Ні', callback_data='nootmenazakaza')
            keyboardotmenazakaza.add(key_bez_photo)
            question = 'Відмінити оформлення замовлення'
            bot.send_message(message.from_user.id, text=question, reply_markup=keyboardotmenazakaza)
            try:
                bot.delete_message(message.chat.id, to_deletekeyboard.message_id)
            except:
                question = 'Відмінити оформлення замовлення'
    elif message.text == "Оплата та реквізити":
        bot.send_message(message.from_user.id, oplatatext)
    elif message.text == "Договір Оферти":
        bot.send_message(message.from_user.id, dogoviroferty)
    elif message.text == "Зв'язатись з менеджером":
        bot.send_message(message.from_user.id,"@rozmist_com_ua")
    elif message.text == "Сайт":
        bot.send_message(message.from_user.id,"https://www.rozmist.com.ua/")
    elif message.text == "Дошки розміщень":
        bot.send_message(message.from_user.id,allsitestext)
    #elif message.content_type == 'photo':
    #    user_id = message.photo[-1].file_id
    #    bot.send_photo(message.from_user.id, user_id)
    else:
        if(startingzakaz == 1):
            bot.send_message(message.from_user.id, text="Вибачте я вас не розумію")
        else:
            markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup_reply.add(button1, button2, button3, button4, button5, button6)
            bot.send_message(message.from_user.id, text="Вибачте я вас не розумію", reply_markup=markup_reply)

   # bot.reply_to(message, message.text)


def reg_name(message):
    if message.text == 'Відмінити замовлення':
        keyboardotmenazakaza = types.InlineKeyboardMarkup()
        key_yes_bez_photo = types.InlineKeyboardButton(text='Так', callback_data='yesotmenazakaza')
        keyboardotmenazakaza.add(key_yes_bez_photo)
        key_bez_photo = types.InlineKeyboardButton(text='Ні', callback_data='nootmenazakaza')
        keyboardotmenazakaza.add(key_bez_photo)
        question = 'Відмінити оформлення замовлення'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboardotmenazakaza)
    else:
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_reply.add(buttonotmenazakaza)
        if message.content_type == 'text':
            global name
            name = message.text
            bot.send_message(message.from_user.id, "Вкажіть будь ласка ваш телефон для зв'язку з вами та подальшого оговорення замовлення, а також відправки звітності про виконане замовлення. Ви можете вказати ваші додаткові контактні дані(Email, telegram, viber і тд)", reply_markup=markup_reply)
            bot.register_next_step_handler(message, reg_phone)
        else:
            bot.send_message(message.from_user.id, text="Це не схоже на текст. Введіть будь ласка текст", reply_markup=markup_reply)
            bot.register_next_step_handler(message, reg_name)

def reg_phone(message):
    if message.text == 'Відмінити замовлення':
        keyboardotmenazakaza = types.InlineKeyboardMarkup()
        key_yes_bez_photo = types.InlineKeyboardButton(text='Так', callback_data='yesotmenazakaza')
        keyboardotmenazakaza.add(key_yes_bez_photo)
        key_bez_photo = types.InlineKeyboardButton(text='Ні', callback_data='nootmenazakaza')
        keyboardotmenazakaza.add(key_bez_photo)
        question = 'Відмінити оформлення замовлення'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboardotmenazakaza)
    else:
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_reply.add(buttonotmenazakaza)
        if message.content_type == 'text':
            global phone_client
            global to_deletekeyboard
            phone_client = message.text
            to_deletekeyboard = bot.send_message(message.from_user.id, text="Виберіть категорію розміщень", reply_markup=keyboard_osnownikategorii)
        else:
            bot.send_message(message.from_user.id, text="Це не схоже на текст. Введіть будь ласка текст", reply_markup=markup_reply)
            bot.register_next_step_handler(message, reg_phone)


def zagolovok_obiavlenia(message):
    if message.text == 'Відмінити замовлення':
        keyboardotmenazakaza = types.InlineKeyboardMarkup()
        key_yes_bez_photo = types.InlineKeyboardButton(text='Так', callback_data='yesotmenazakaza')
        keyboardotmenazakaza.add(key_yes_bez_photo)
        key_bez_photo = types.InlineKeyboardButton(text='Ні', callback_data='nootmenazakaza')
        keyboardotmenazakaza.add(key_bez_photo)
        question = 'Відмінити оформлення замовлення'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboardotmenazakaza)
    else:
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_reply.add(buttonotmenazakaza)
        if message.content_type == 'text':
            global zagolovok_obiavlenia_onlytext
            zagolovok_obiavlenia_onlytext = message.text
            bot.send_message(message.from_user.id, "Напишіть будь ласка текст оголошення", reply_markup=markup_reply)
            bot.register_next_step_handler(message, text_ogoloshenya)
        else:
            bot.send_message(message.from_user.id, text="Це не схоже на текст. Введіть будь ласка текст", reply_markup=markup_reply)
            bot.register_next_step_handler(message, zagolovok_obiavlenia)


def text_ogoloshenya(message):
    if message.text == 'Відмінити замовлення':
        keyboardotmenazakaza = types.InlineKeyboardMarkup()
        key_yes_bez_photo = types.InlineKeyboardButton(text='Так', callback_data='yesotmenazakaza')
        keyboardotmenazakaza.add(key_yes_bez_photo)
        key_bez_photo = types.InlineKeyboardButton(text='Ні', callback_data='nootmenazakaza')
        keyboardotmenazakaza.add(key_bez_photo)
        question = 'Відмінити оформлення замовлення'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboardotmenazakaza)
    else:
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_reply.add(buttonotmenazakaza)
        if message.content_type == 'text':
            global text_ogoloshenya_onlytext
            text_ogoloshenya_onlytext = message.text
            bot.send_message(message.from_user.id, "Напишіть будь ласка ціну яка буде вказана в оглошенні. Наприклад:100грн або 250$", reply_markup=markup_reply)
            bot.register_next_step_handler(message, price_uslugi)
        else:
            bot.send_message(message.from_user.id, text="Це не схоже на текст. Введіть будь ласка текст", reply_markup=markup_reply)
            bot.register_next_step_handler(message, text_ogoloshenya)


def price_uslugi(message):
    if message.text == 'Відмінити замовлення':
        keyboardotmenazakaza = types.InlineKeyboardMarkup()
        key_yes_bez_photo = types.InlineKeyboardButton(text='Так', callback_data='yesotmenazakaza')
        keyboardotmenazakaza.add(key_yes_bez_photo)
        key_bez_photo = types.InlineKeyboardButton(text='Ні', callback_data='nootmenazakaza')
        keyboardotmenazakaza.add(key_bez_photo)
        question = 'Відмінити оформлення замовлення'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboardotmenazakaza)
    else:
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_reply.add(buttonotmenazakaza)
        if message.content_type == 'text':
            global price_uslugi_onlytext
            price_uslugi_onlytext = message.text
            bot.send_message(message.from_user.id, "Вкажіть контакти для розміщення в оголошенні (ПІБ , тел, сайт, email)", reply_markup=markup_reply)
            bot.register_next_step_handler(message, kontaktitorozmist_in_ogoloshemya)
        else:
            bot.send_message(message.from_user.id, text="Це не схоже на текст. Введіть будь ласка текст", reply_markup=markup_reply)
            bot.register_next_step_handler(message, price_uslugi)

def kontaktitorozmist_in_ogoloshemya(message):
    if message.text == 'Відмінити замовлення':
        keyboardotmenazakaza = types.InlineKeyboardMarkup()
        key_yes_bez_photo = types.InlineKeyboardButton(text='Так', callback_data='yesotmenazakaza')
        keyboardotmenazakaza.add(key_yes_bez_photo)
        key_bez_photo = types.InlineKeyboardButton(text='Ні', callback_data='nootmenazakaza')
        keyboardotmenazakaza.add(key_bez_photo)
        question = 'Відмінити оформлення замовлення'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboardotmenazakaza)
    else:
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_reply.add(buttonotmenazakaza)
        if message.content_type == 'text':
            global kontaktitorozmist_in_ogoloshemya_onlytext
            kontaktitorozmist_in_ogoloshemya_onlytext = message.text
            bot.send_message(message.from_user.id, "Вкажіть будь ласка регіон розміщення (Наприклад:Київ, Умань, Вся Україна)", reply_markup=markup_reply)
            bot.register_next_step_handler(message, regionrozmist_in_ogoloshemya)
        else:
            bot.send_message(message.from_user.id, text="Це не схоже на текст. Введіть будь ласка текст", reply_markup=markup_reply)
            bot.register_next_step_handler(message, kontaktitorozmist_in_ogoloshemya)


def regionrozmist_in_ogoloshemya(message):
    if message.text == 'Відмінити замовлення':
        keyboardotmenazakaza = types.InlineKeyboardMarkup()
        key_yes_bez_photo = types.InlineKeyboardButton(text='Так', callback_data='yesotmenazakaza')
        keyboardotmenazakaza.add(key_yes_bez_photo)
        key_bez_photo = types.InlineKeyboardButton(text='Ні', callback_data='nootmenazakaza')
        keyboardotmenazakaza.add(key_bez_photo)
        question = 'Відмінити оформлення замовлення'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboardotmenazakaza)
    else:
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_reply.add(buttonotmenazakaza)
        if message.content_type == 'text':
            global regionrozmist_in_ogoloshemya_onlytext
            regionrozmist_in_ogoloshemya_onlytext = message.text
            bot.send_message(message.from_user.id, "Вкажіть будь ласка термін розміщення (тиждень, місяць, пів-року, рік)", reply_markup=markup_reply)
            bot.register_next_step_handler(message, termin_rozmist_in_ogoloshemya)
        else:
            bot.send_message(message.from_user.id, text="Це не схоже на текст. Введіть будь ласка текст", reply_markup=markup_reply)
            bot.register_next_step_handler(message, regionrozmist_in_ogoloshemya)


def termin_rozmist_in_ogoloshemya(message):
    if message.text == 'Відмінити замовлення':
        keyboardotmenazakaza = types.InlineKeyboardMarkup()
        key_yes_bez_photo = types.InlineKeyboardButton(text='Так', callback_data='yesotmenazakaza')
        keyboardotmenazakaza.add(key_yes_bez_photo)
        key_bez_photo = types.InlineKeyboardButton(text='Ні', callback_data='nootmenazakaza')
        keyboardotmenazakaza.add(key_bez_photo)
        question = 'Відмінити оформлення замовлення'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboardotmenazakaza)
    else:
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_reply.add(buttonotmenazakaza)
        if message.content_type == 'text':
            global terminrozmist_in_ogoloshemya_onlytext
            terminrozmist_in_ogoloshemya_onlytext = message.text
            bot.send_message(message.from_user.id, "Додайте фото публікації", reply_markup=markup_reply)
            bot.register_next_step_handler(message, dobavtephotopublikatsiy)
        else:
            bot.send_message(message.from_user.id, text="Це не схоже на текст. Введіть будь ласка текст", reply_markup=markup_reply)
            bot.register_next_step_handler(message, termin_rozmist_in_ogoloshemya)



def dobavtephotopublikatsiy(message):
    markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup_reply.add(button1, button2, button3, button4, button5, button6)
    try:
        global photopublikatsiy
        photopublikatsiy = message.photo[-1].file_id
        bot.send_photo(message.from_user.id, photopublikatsiy)
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Так', callback_data='yes')
        keyboard.add(key_yes)
        key_no = types.InlineKeyboardButton(text='Ні', callback_data='no')
        keyboard.add(key_no)
        question = 'Підтвердити замовлення ?'
        bot.send_message(message.from_user.id, text="Ваше замовлення прийнято системою.", reply_markup=markup_reply)
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

    except:
        global photopublikatsiy_bezphoto
        photopublikatsiy_bezphoto = message.text
        bot.send_message(message.from_user.id, 'Це не схоже на фото але я запишу це. Потім фото ви зможете відправити менеджеру @rozmist_com_ua')
        keyboard_bez_photo = types.InlineKeyboardMarkup()
        key_yes_bez_photo = types.InlineKeyboardButton(text='Так', callback_data='yesbezphoto')
        keyboard_bez_photo.add(key_yes_bez_photo)
        key_bez_photo = types.InlineKeyboardButton(text='Ні', callback_data='nobezphoto')
        keyboard_bez_photo.add(key_bez_photo)
        question = 'Підтвердити замовлення ?'
        bot.send_message(message.from_user.id, text="Ваше замовлення прийнято системою.", reply_markup=markup_reply)
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard_bez_photo)









@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global notoclick
    global stopclick
    global notoclick_oformzak
    global stopclick_oformzak
    global name
    global nomer_zakaza
    if call.data == "yes":
        notoclick_oformzak = 1
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_reply.add(button1, button2, button3, button4,button5,button6)
        if stopclick_oformzak == 0 and notoclick_oformzak == 1:
            stopclick_oformzak = 1
            bot.send_message(call.message.chat.id, "Теперь будь ласка проведіть оплату.", reply_markup=markup_reply)
            bot.send_message(call.message.chat.id, oplatatext)
            connect = sqlite3.connect('users.db')
            cursor = connect.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS zakazy(
                userID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                chatID INT(10)
            )""")
            connect.commit()
            # add values in fields
            cursor.execute("INSERT INTO zakazy(chatID) VALUES('lol');")
            connect.commit()
            nomer_zakaza = cursor.execute("SELECT userID FROM zakazy ORDER BY userID DESC LIMIT 1;").fetchall()
            nomer_zakaza = nomer_zakaza[0][0]
            nomer_zakaza = str(nomer_zakaza)
            print(nomer_zakaza)
            sendtoadmin_info()
            connect.commit()
            obnowclickdanni()
            bot.send_message(call.message.chat.id, "Номер вашого замовлення : " + nomer_zakaza + " Будь ласка збережіть його")
            bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == "yesotmenazakaza":
        name = ""
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_reply.add(button1, button2, button3, button4,button5,button6)
        notoclick_oformzak = 1
        if stopclick_oformzak == 0 and notoclick_oformzak == 1:
            stopclick_oformzak = 1
            bot.send_message(call.message.chat.id, "Ви відхилили ваше замовлення.")
            bot.send_message(call.message.chat.id, "Ви можете повторно оформити замовлення або запитати в мене щось інше)))", reply_markup=markup_reply)
            obnowclickdanni()
            bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == "nootmenazakaza":
        name = ""
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_reply.add(buttonotmenazakaza)
        notoclick_oformzak = 1
        if stopclick_oformzak == 0 and notoclick_oformzak == 1:
            stopclick_oformzak = 1
            bot.send_message(call.message.chat.id, "Добре, тоді починаємо оформляти замовлення з самого початку", reply_markup=markup_reply)
            bot.send_message(call.message.chat.id, "Скажіть будь ласка як мені до вас звертатись")
            obnowclickdanni()
            obnowclickstartornozakaz()
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.register_next_step_handler(call.message, reg_name)
    elif call.data == "yesbezphoto":
        notoclick_oformzak = 1
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_reply.add(button1, button2, button3, button4,button5,button6)
        if stopclick_oformzak == 0 and notoclick_oformzak == 1:
            stopclick_oformzak = 1
            bot.send_message(call.message.chat.id, "Теперь будь ласка проведіть оплату.", reply_markup=markup_reply)
            bot.send_message(call.message.chat.id, oplatatext)
            connect = sqlite3.connect('users.db')
            cursor = connect.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS zakazy(
                userID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                chatID INT(10)
            )""")
            connect.commit()
            # add values in fields
            cursor.execute("INSERT INTO zakazy(chatID) VALUES('lol');")
            connect.commit()
            nomer_zakaza = cursor.execute("SELECT userID FROM zakazy ORDER BY userID DESC LIMIT 1;").fetchall()
            nomer_zakaza = nomer_zakaza[0][0]
            nomer_zakaza = str(nomer_zakaza)
            print(nomer_zakaza)
            sendtoadmin_info_bezphoto()
            connect.commit()
            obnowclickdanni()
            bot.send_message(call.message.chat.id, "Номер вашого замовлення : " + nomer_zakaza + " Будь ласка збережіть його")
            bot.delete_message(call.message.chat.id, call.message.message_id)
    elif call.data == "no":
        name = ""
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_reply.add(button1, button2, button3, button4,button5,button6)
        notoclick_oformzak = 1
        if stopclick_oformzak == 0 and notoclick_oformzak == 1:
            stopclick_oformzak = 1
            bot.send_message(call.message.chat.id, "Ви відхилили ваше замовлення.", reply_markup=markup_reply)
            bot.send_message(call.message.chat.id, "Ви можете повторно оформити замовлення або запитати в мене щось інше)))")
            obnowclickdanni()
            bot.delete_message(call.message.chat.id, call.message.message_id)
            #bot.register_next_step_handler(call.message,reg_name)
    elif call.data == "nobezphoto":
        name = ""
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_reply.add(button1, button2, button3, button4,button5,button6)
        notoclick_oformzak = 1
        if stopclick_oformzak == 0 and notoclick_oformzak == 1:
            stopclick_oformzak = 1
            bot.send_message(call.message.chat.id, "Ви відхилили ваше замовлення.", reply_markup=markup_reply)
            bot.send_message(call.message.chat.id, "Ви можете повторно оформити замовлення або запитати в мене щось інше)))")
            obnowclickdanni()
            bot.delete_message(call.message.chat.id, call.message.message_id)
            #bot.register_next_step_handler(call.message,reg_name)
    elif call.data == "go_to_manager":
        bot.send_message(call.message.chat.id,"@rozmist_com_ua")
    elif call.data == "oform_zakaz":
        global startingzakaz
        startingzakaz = 1
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_reply.add(buttonotmenazakaza)
        bot.send_message(call.message.chat.id,"Скажіть будь ласка як мені до вас звертатись", reply_markup=markup_reply)
        bot.register_next_step_handler(call.message,reg_name)
    elif call.data == "see_card_rozmist":
        bot.send_message(call.message.chat.id, allsitestext)
    elif call.data == "key1_detskiymir":
        notoclick = 1
        if stopclick == 0 and notoclick == 1:
            global osnownaya_kategoriya_todatabase
            osnownaya_kategoriya_todatabase = "Дитячий світ"
            bot.send_message(call.message.chat.id, "Ваша категорія дитячий світ")
            bot.send_message(call.message.chat.id, "Введіть заголовок оголошення")
            stopclick = 1
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.register_next_step_handler(call.message,zagolovok_obiavlenia)
    elif call.data == "key2_neruhomist":
        notoclick = 1
        if stopclick == 0 and notoclick == 1:
            osnownaya_kategoriya_todatabase = "Нерухомість"
            bot.send_message(call.message.chat.id, "Ваша категорія Нерухомість")
            bot.send_message(call.message.chat.id, "Введіть заголовок оголошення")
            stopclick = 1
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.register_next_step_handler(call.message,zagolovok_obiavlenia)
    elif call.data == "key3_transport":
        notoclick = 1
        if stopclick == 0 and notoclick == 1:
            osnownaya_kategoriya_todatabase = "Транспорт"
            bot.send_message(call.message.chat.id, "Ваша категорія Транспорт")
            bot.send_message(call.message.chat.id, "Введіть заголовок оголошення")
            stopclick = 1
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.register_next_step_handler(call.message,zagolovok_obiavlenia)
    elif call.data == "key4_avtozapchasti":
        notoclick = 1
        if stopclick == 0 and notoclick == 1:
            osnownaya_kategoriya_todatabase = "Авто-Запчастини"
            bot.send_message(call.message.chat.id, "Ваша категорія Авто-Запчастини")
            bot.send_message(call.message.chat.id, "Введіть заголовок оголошення")
            stopclick = 1
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.register_next_step_handler(call.message,zagolovok_obiavlenia)
    elif call.data == "key5_work":
        notoclick = 1
        if stopclick == 0 and notoclick == 1:
            osnownaya_kategoriya_todatabase = "Робота"
            bot.send_message(call.message.chat.id, "Ваша категорія Робота")
            bot.send_message(call.message.chat.id, "Введіть заголовок оголошення")
            stopclick = 1
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.register_next_step_handler(call.message,zagolovok_obiavlenia)
    elif call.data == "key6_tvarini":
        notoclick = 1
        if stopclick == 0 and notoclick == 1:
            osnownaya_kategoriya_todatabase = "Тварини"
            bot.send_message(call.message.chat.id, "Ваша категорія Тварини")
            bot.send_message(call.message.chat.id, "Введіть заголовок оголошення")
            stopclick = 1
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.register_next_step_handler(call.message,zagolovok_obiavlenia)
    elif call.data == "key7_domisad":
        notoclick = 1
        if stopclick == 0 and notoclick == 1:
            osnownaya_kategoriya_todatabase = "Дом і сад"
            bot.send_message(call.message.chat.id, "Ваша категорія Дом і сад")
            bot.send_message(call.message.chat.id, "Введіть заголовок оголошення")
            stopclick = 1
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.register_next_step_handler(call.message,zagolovok_obiavlenia)
    elif call.data == "key8_elektronica":
        notoclick = 1
        if stopclick == 0 and notoclick == 1:
            osnownaya_kategoriya_todatabase = "Електроніка"
            bot.send_message(call.message.chat.id, "Ваша категорія Електроніка")
            bot.send_message(call.message.chat.id, "Введіть заголовок оголошення")
            stopclick = 1
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.register_next_step_handler(call.message,zagolovok_obiavlenia)
    elif call.data == "key9_biznestaposlugi":
        notoclick = 1
        if stopclick == 0 and notoclick == 1:
            osnownaya_kategoriya_todatabase = "Бізнес та послуги"
            bot.send_message(call.message.chat.id, "Ваша категорія Бізнес та послуги")
            bot.send_message(call.message.chat.id, "Введіть заголовок оголошення")
            stopclick = 1
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.register_next_step_handler(call.message,zagolovok_obiavlenia)
    elif call.data == "key10_modaistil":
        notoclick = 1
        if stopclick == 0 and notoclick == 1:
            osnownaya_kategoriya_todatabase = "Мода та стиль"
            bot.send_message(call.message.chat.id, "Ваша категорія Мода та стиль")
            bot.send_message(call.message.chat.id, "Введіть заголовок оголошення")
            stopclick = 1
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.register_next_step_handler(call.message,zagolovok_obiavlenia)
    elif call.data == "key11_hobbiotdihisport":
        notoclick = 1
        if stopclick == 0 and notoclick == 1:
            osnownaya_kategoriya_todatabase = "Хоббі відпочинок та спорт"
            bot.send_message(call.message.chat.id, "Ваша категорія Хоббі відпочинок та спорт")
            bot.send_message(call.message.chat.id, "Введіть заголовок оголошення")
            stopclick = 1
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.register_next_step_handler(call.message,zagolovok_obiavlenia)
    elif call.data == "key12_otdamdarom":
        notoclick = 1
        if stopclick == 0 and notoclick == 1:
            osnownaya_kategoriya_todatabase = "Віддам даром"
            bot.send_message(call.message.chat.id, "Ваша категорія Віддам даром")
            bot.send_message(call.message.chat.id, "Введіть заголовок оголошення")
            stopclick = 1
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.register_next_step_handler(call.message,zagolovok_obiavlenia)
    elif call.data == "key13_obminiay":
        notoclick = 1
        if stopclick == 0 and notoclick == 1:
            osnownaya_kategoriya_todatabase = "Обміняю"
            bot.send_message(call.message.chat.id, "Ваша категорія Обміняю")
            bot.send_message(call.message.chat.id, "Введіть заголовок оголошення")
            stopclick = 1
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.register_next_step_handler(call.message,zagolovok_obiavlenia)




bot.polling()
