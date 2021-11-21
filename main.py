import telebot
import sqlite3
from telebot import types
from pprint import pprint
from telegram import Update, ReplyKeyboardRemove
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, ConversationHandler
from auth_data import dogoviroferty, allsitestext,oformzakaztext,oplatatext,keyboard_nextcategorii_detskiymir,keyboard_osnownikategorii, keyboard_nextcategorii_neruhomist,keyboard_nextcategorii_transport,keyboard_nextcategorii_avtozapchasti,keyboard_nextcategorii_robota
from telebot.types import InlineKeyboardMarkup, ReplyKeyboardMarkup


#Массивы что бы хранить введенную информацию пользователем, а также кликеры.
#Они нужны для того что бы пользоваться ботом могло одновременно много человек
#и данные не путались и не пересекались

Aname = []
Azagolovok_obiavlenia_onlytext = []
Aphone_client = []
Aosnownaya_kategoriya_todatabase = []
Adopolnitelnaya_kategoriya_todatabase = []
Akontaktitorozmist_in_ogoloshemya_onlytext = []
Aprice_uslugi_onlytext = []
Atext_ogoloshenya_onlytext = []
Aregionrozmist_in_ogoloshemya_onlytext = []
Aterminrozmist_in_ogoloshemya_onlytext = []
Aphotopublikatsiy_bezphoto = []
Anotoclick = []
Astopclick = []
Anotoclick_oformzak = []
Astopclick_oformzak = []
Astartingzakaz = []
Anomer_zakaza = []
Aphotopublikatsiy = []




bot = telebot.TeleBot("1797750128:AAFlT0gB2tautHdS7swhajuYvk4BPKyFpis")

button1 = types.KeyboardButton('Сайт')
button2 = types.KeyboardButton('Оформити замовлення')
button3 = types.KeyboardButton("Зв'язатись з менеджером")
button4 = types.KeyboardButton('Оплата та реквізити')
button5 = types.KeyboardButton('Дошки розміщень')
button6 = types.KeyboardButton('Договір Оферти')
buttonotmenazakaza = types.KeyboardButton('Відмінити замовлення ❌')





def sendtoadmin_info(iduser):
    for i in range(len(Anomer_zakaza)):
        for j in range(len(Anomer_zakaza[i])):
            if Anomer_zakaza[i][j] == iduser:
                nomer_zakaza = Anomer_zakaza[i][j + 1]
    for i in range(len(Aname)):
        for j in range(len(Aname[i])):
            if Aname[i][j] == iduser:
                name = Aname[i][j + 1]
    for i in range(len(Aphone_client)):
        for j in range(len(Aphone_client[i])):
            if Aphone_client[i][j] == iduser:
                phone_client = Aphone_client[i][j + 1]
    for i in range(len(Aosnownaya_kategoriya_todatabase)):
        for j in range(len(Aosnownaya_kategoriya_todatabase[i])):
            if Aosnownaya_kategoriya_todatabase[i][j] == iduser:
                osnownaya_kategoriya_todatabase = Aosnownaya_kategoriya_todatabase[i][j + 1]
    for i in range(len(Azagolovok_obiavlenia_onlytext)):
        for j in range(len(Azagolovok_obiavlenia_onlytext[i])):
            if Azagolovok_obiavlenia_onlytext[i][j] == iduser:
                zagolovok_obiavlenia_onlytext = Azagolovok_obiavlenia_onlytext[i][j + 1]
    for i in range(len(Atext_ogoloshenya_onlytext)):
        for j in range(len(Atext_ogoloshenya_onlytext[i])):
            if Atext_ogoloshenya_onlytext[i][j] == iduser:
                text_ogoloshenya_onlytext = Atext_ogoloshenya_onlytext[i][j + 1]
    for i in range(len(Aprice_uslugi_onlytext)):
        for j in range(len(Aprice_uslugi_onlytext[i])):
            if Aprice_uslugi_onlytext[i][j] == iduser:
                price_uslugi_onlytext = Aprice_uslugi_onlytext[i][j + 1]
    for i in range(len(Akontaktitorozmist_in_ogoloshemya_onlytext)):
        for j in range(len(Akontaktitorozmist_in_ogoloshemya_onlytext[i])):
            if Akontaktitorozmist_in_ogoloshemya_onlytext[i][j] == iduser:
                kontaktitorozmist_in_ogoloshemya_onlytext = Akontaktitorozmist_in_ogoloshemya_onlytext[i][j + 1]
    for i in range(len(Aregionrozmist_in_ogoloshemya_onlytext)):
        for j in range(len(Aregionrozmist_in_ogoloshemya_onlytext[i])):
            if Aregionrozmist_in_ogoloshemya_onlytext[i][j] == iduser:
                regionrozmist_in_ogoloshemya_onlytext = Aregionrozmist_in_ogoloshemya_onlytext[i][j + 1]
    for i in range(len(Aterminrozmist_in_ogoloshemya_onlytext)):
        for j in range(len(Aterminrozmist_in_ogoloshemya_onlytext[i])):
            if Aterminrozmist_in_ogoloshemya_onlytext[i][j] == iduser:
                terminrozmist_in_ogoloshemya_onlytext = Aterminrozmist_in_ogoloshemya_onlytext[i][j + 1]
    for i in range(len(Aphotopublikatsiy)):
        for j in range(len(Aphotopublikatsiy[i])):
            if Aphotopublikatsiy[i][j] == iduser:
                photopublikatsiy = Aphotopublikatsiy[i][j + 1]
    bot.send_message(687554764, "Номер замовлення клієнта : " + nomer_zakaza + "\n\n\nім'я замовника : " + name + "\n\n\nТелефон замовника : " + phone_client + "\n\n\nКатегорія розміщень : " + osnownaya_kategoriya_todatabase + "\n\n\nЗаголовок оголошення : " + zagolovok_obiavlenia_onlytext + "\n\n\nТекст оголошення : " + text_ogoloshenya_onlytext + "\n\n\nЦіна в оголошенні : " + price_uslugi_onlytext + "\n\n\nКонтакти для оголошення : " + kontaktitorozmist_in_ogoloshemya_onlytext + "\n\n\nРегіон для оголошення : " + regionrozmist_in_ogoloshemya_onlytext + "\n\n\nТермін для оголошення : " + terminrozmist_in_ogoloshemya_onlytext + "")
    bot.send_photo(687554764, photopublikatsiy)



def sendtoadmin_info_bezphoto(iduser):
    for i in range(len(Anomer_zakaza)):
        for j in range(len(Anomer_zakaza[i])):
            if Anomer_zakaza[i][j] == iduser:
                nomer_zakaza = Anomer_zakaza[i][j + 1]
    for i in range(len(Aname)):
        for j in range(len(Aname[i])):
            if Aname[i][j] == iduser:
                name = Aname[i][j + 1]
    for i in range(len(Aphone_client)):
        for j in range(len(Aphone_client[i])):
            if Aphone_client[i][j] == iduser:
                phone_client = Aphone_client[i][j + 1]
    for i in range(len(Aosnownaya_kategoriya_todatabase)):
        for j in range(len(Aosnownaya_kategoriya_todatabase[i])):
            if Aosnownaya_kategoriya_todatabase[i][j] == iduser:
                osnownaya_kategoriya_todatabase = Aosnownaya_kategoriya_todatabase[i][j + 1]
    for i in range(len(Azagolovok_obiavlenia_onlytext)):
        for j in range(len(Azagolovok_obiavlenia_onlytext[i])):
            if Azagolovok_obiavlenia_onlytext[i][j] == iduser:
                zagolovok_obiavlenia_onlytext = Azagolovok_obiavlenia_onlytext[i][j + 1]
    for i in range(len(Atext_ogoloshenya_onlytext)):
        for j in range(len(Atext_ogoloshenya_onlytext[i])):
            if Atext_ogoloshenya_onlytext[i][j] == iduser:
                text_ogoloshenya_onlytext = Atext_ogoloshenya_onlytext[i][j + 1]
    for i in range(len(Aprice_uslugi_onlytext)):
        for j in range(len(Aprice_uslugi_onlytext[i])):
            if Aprice_uslugi_onlytext[i][j] == iduser:
                price_uslugi_onlytext = Aprice_uslugi_onlytext[i][j + 1]
    for i in range(len(Akontaktitorozmist_in_ogoloshemya_onlytext)):
        for j in range(len(Akontaktitorozmist_in_ogoloshemya_onlytext[i])):
            if Akontaktitorozmist_in_ogoloshemya_onlytext[i][j] == iduser:
                kontaktitorozmist_in_ogoloshemya_onlytext = Akontaktitorozmist_in_ogoloshemya_onlytext[i][j + 1]
    for i in range(len(Aregionrozmist_in_ogoloshemya_onlytext)):
        for j in range(len(Aregionrozmist_in_ogoloshemya_onlytext[i])):
            if Aregionrozmist_in_ogoloshemya_onlytext[i][j] == iduser:
                regionrozmist_in_ogoloshemya_onlytext = Aregionrozmist_in_ogoloshemya_onlytext[i][j + 1]
    for i in range(len(Aterminrozmist_in_ogoloshemya_onlytext)):
        for j in range(len(Aterminrozmist_in_ogoloshemya_onlytext[i])):
            if Aterminrozmist_in_ogoloshemya_onlytext[i][j] == iduser:
                terminrozmist_in_ogoloshemya_onlytext = Aterminrozmist_in_ogoloshemya_onlytext[i][j + 1]
    for i in range(len(Aphotopublikatsiy_bezphoto)):
        for j in range(len(Aphotopublikatsiy_bezphoto[i])):
            if Aphotopublikatsiy_bezphoto[i][j] == iduser:
                photopublikatsiy_bezphoto = Aphotopublikatsiy_bezphoto[i][j + 1]
    bot.send_message(687554764, "Номер замовлення клієнта : " + nomer_zakaza + "\n\n\nім'я замовника : " + name + "\n\n\nТелефон замовника : " + phone_client + "\n\n\nКатегорія розміщень : " + osnownaya_kategoriya_todatabase + "\n\n\nЗаголовок оголошення : " + zagolovok_obiavlenia_onlytext + "\n\n\nТекст оголошення : " + text_ogoloshenya_onlytext + "\n\n\nЦіна в оголошенні : " + price_uslugi_onlytext + "\n\n\nКонтакти для оголошення : " + kontaktitorozmist_in_ogoloshemya_onlytext + "\n\n\nРегіон для оголошення : " + regionrozmist_in_ogoloshemya_onlytext + "\n\n\nТермін для оголошення : " + terminrozmist_in_ogoloshemya_onlytext + "")
    bot.send_message(687554764, "Текст який надіслав клієнт замість фото : " + photopublikatsiy_bezphoto + "")


def obnowclickdanni(iduser):
    for i in range(len(Aname)):
        for j in range(len(Aname[i])):
            if Aname[i][j] == iduser:
                Aname[i][j + 1] = 0
    for i in range(len(Azagolovok_obiavlenia_onlytext)):
        for j in range(len(Azagolovok_obiavlenia_onlytext[i])):
            if Azagolovok_obiavlenia_onlytext[i][j] == iduser:
                Azagolovok_obiavlenia_onlytext[i][j + 1] = ""
    for i in range(len(Aphone_client)):
        for j in range(len(Aphone_client[i])):
            if Aphone_client[i][j] == iduser:
                Aphone_client[i][j + 1] = ""
    for i in range(len(Aosnownaya_kategoriya_todatabase)):
        for j in range(len(Aosnownaya_kategoriya_todatabase[i])):
            if Aosnownaya_kategoriya_todatabase[i][j] == iduser:
                Aosnownaya_kategoriya_todatabase[i][j + 1] = ""
    for i in range(len(Adopolnitelnaya_kategoriya_todatabase)):
        for j in range(len(Adopolnitelnaya_kategoriya_todatabase[i])):
            if Adopolnitelnaya_kategoriya_todatabase[i][j] == iduser:
                Adopolnitelnaya_kategoriya_todatabase[i][j + 1] = ""
    for i in range(len(Akontaktitorozmist_in_ogoloshemya_onlytext)):
        for j in range(len(Akontaktitorozmist_in_ogoloshemya_onlytext[i])):
            if Akontaktitorozmist_in_ogoloshemya_onlytext[i][j] == iduser:
                Akontaktitorozmist_in_ogoloshemya_onlytext[i][j + 1] = ""
    for i in range(len(Aprice_uslugi_onlytext)):
        for j in range(len(Aprice_uslugi_onlytext[i])):
            if Aprice_uslugi_onlytext[i][j] == iduser:
                Aprice_uslugi_onlytext[i][j + 1] = ""
    for i in range(len(Atext_ogoloshenya_onlytext)):
        for j in range(len(Atext_ogoloshenya_onlytext[i])):
            if Atext_ogoloshenya_onlytext[i][j] == iduser:
                Atext_ogoloshenya_onlytext[i][j + 1] = 0
    for i in range(len(Aregionrozmist_in_ogoloshemya_onlytext)):
        for j in range(len(Aregionrozmist_in_ogoloshemya_onlytext[i])):
            if Aregionrozmist_in_ogoloshemya_onlytext[i][j] == iduser:
                Aregionrozmist_in_ogoloshemya_onlytext[i][j + 1] = 0
    for i in range(len(Aterminrozmist_in_ogoloshemya_onlytext)):
        for j in range(len(Aterminrozmist_in_ogoloshemya_onlytext[i])):
            if Aterminrozmist_in_ogoloshemya_onlytext[i][j] == iduser:
                Aterminrozmist_in_ogoloshemya_onlytext[i][j + 1] = 0
    for i in range(len(Aphotopublikatsiy_bezphoto)):
        for j in range(len(Aphotopublikatsiy_bezphoto[i])):
            if Aphotopublikatsiy_bezphoto[i][j] == iduser:
                Aphotopublikatsiy_bezphoto[i][j + 1] = 0
    for i in range(len(Anotoclick)):
        for j in range(len(Anotoclick[i])):
            if Anotoclick[i][j] == iduser:
                Anotoclick[i][j + 1] = 0
    for i in range(len(Astopclick)):
        for j in range(len(Astopclick[i])):
            if Astopclick[i][j] == iduser:
                Astopclick[i][j + 1] = 0
    for i in range(len(Anotoclick_oformzak)):
        for j in range(len(Anotoclick_oformzak[i])):
            if Anotoclick_oformzak[i][j] == iduser:
                Anotoclick_oformzak[i][j + 1] = 0
    for i in range(len(Astopclick_oformzak)):
        for j in range(len(Astopclick_oformzak[i])):
            if Astopclick_oformzak[i][j] == iduser:
                Astopclick_oformzak[i][j + 1] = 0
    for i in range(len(Astartingzakaz)):
        for j in range(len(Astartingzakaz[i])):
            if Astartingzakaz[i][j] == iduser:
                Astartingzakaz[i][j + 1] = 0
    for i in range(len(Anomer_zakaza)):
        for j in range(len(Anomer_zakaza[i])):
            if Anomer_zakaza[i][j] == iduser:
                Anomer_zakaza[i][j + 1] = 0


def obnowclickstartornozakaz(iduser):
    for i in range(len(Astartingzakaz)):
        for j in range(len(Astartingzakaz[i])):
            if Astartingzakaz[i][j] == iduser:
                Astartingzakaz[i][j + 1] = 1





@bot.message_handler(func=lambda m: True,  content_types=["text", "sticker", "pinned_message", "photo", "audio"])
def echo_all(message):
    foundinlist = 0
    startingzakaz = 0
    if message.text == "/start":
        for i in range(len(Astartingzakaz)):
            for j in range(len(Astartingzakaz[i])):
                if Astartingzakaz[i][j] == message.from_user.id:
                    startingzakaz = Astartingzakaz[i][j + 1]
                    foundinlist = 1
        if foundinlist == 0:
            Astartingzakaz.append([message.from_user.id, 0])
            startingzakaz = 0
        foundinlist = 0
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
        for i in range(len(Astartingzakaz)):
            for j in range(len(Astartingzakaz[i])):
                if Astartingzakaz[i][j] == message.from_user.id:
                    if Astartingzakaz[i][j + 1] == 0:
                        Astartingzakaz[i][j + 1] = 1
                        foundinlist = 1
                        startingzakaz = 1
                    elif Astartingzakaz[i][j + 1] == 1:
                        foundinlist = 1
                        startingzakaz = 0
        if foundinlist == 0:
            Astartingzakaz.append([message.from_user.id, 1])
            startingzakaz = 1
        foundinlist = 0
        if startingzakaz == 1:
            markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup_reply.add(buttonotmenazakaza)
            bot.send_message(message.from_user.id, "Скажіть будь ласка як мені до вас звертатись", reply_markup=markup_reply)
            bot.register_next_step_handler(message, reg_name)
        else:
            markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup_reply.add(buttonotmenazakaza)
            bot.send_message(message.from_user.id, text="Вибачте я вас не розумію", reply_markup=markup_reply)
    elif message.text == "Відмінити замовлення ❌":
        for i in range(len(Astartingzakaz)):
            for j in range(len(Astartingzakaz[i])):
                if Astartingzakaz[i][j] == message.from_user.id:
                    if Astartingzakaz[i][j + 1] == 0:
                        startingzakaz = 0
                        foundinlist = 1
                    elif Astartingzakaz[i][j + 1] == 1:
                        startingzakaz = 1
                        foundinlist = 1
        if foundinlist == 0:
            Astartingzakaz.append([message.from_user.id, 0])
            startingzakaz = 0
        foundinlist = 0
        if startingzakaz == 0:
            markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup_reply.add(button1, button2, button3, button4, button5, button6)
            bot.send_message(message.from_user.id, text="Вибачте я вас не розумію")
        else:
            keyboardotmenazakaza = types.InlineKeyboardMarkup()
            key_yes_bez_photo = types.InlineKeyboardButton(text='Так', callback_data='yesotmenazakaza')
            keyboardotmenazakaza.add(key_yes_bez_photo)
            key_bez_photo = types.InlineKeyboardButton(text='Ні', callback_data='nootmenazakaza')
            keyboardotmenazakaza.add(key_bez_photo)
            question = 'Відмінити оформлення замовлення ❌'
            bot.send_message(message.from_user.id, text=question, reply_markup=keyboardotmenazakaza)
            try:
                bot.delete_message(message.chat.id, to_deletekeyboard.message_id)
            except:
                question = 'Відмінити оформлення замовлення ❌'
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
        for i in range(len(Astartingzakaz)):
            for j in range(len(Astartingzakaz[i])):
                if Astartingzakaz[i][j] == message.from_user.id:
                    if Astartingzakaz[i][j + 1] == 1:
                        startingzakaz = 1
        if(startingzakaz == 1):
            bot.send_message(message.from_user.id, text="Вибачте я вас не розумію")
        else:
            markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup_reply.add(button1, button2, button3, button4, button5, button6)
            bot.send_message(message.from_user.id, text="Вибачте я вас не розумію", reply_markup=markup_reply)

   # bot.reply_to(message, message.text)


def reg_name(message):
    if message.text == 'Відмінити замовлення ❌':
        keyboardotmenazakaza = types.InlineKeyboardMarkup()
        key_yes_bez_photo = types.InlineKeyboardButton(text='Так', callback_data='yesotmenazakaza')
        keyboardotmenazakaza.add(key_yes_bez_photo)
        key_bez_photo = types.InlineKeyboardButton(text='Ні', callback_data='nootmenazakaza')
        keyboardotmenazakaza.add(key_bez_photo)
        question = 'Відмінити оформлення замовлення ❌'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboardotmenazakaza)
    else:
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_reply.add(buttonotmenazakaza)
        foundinlist = 0
        if message.content_type == 'text':
            for i in range(len(Aname)):
                for j in range(len(Aname[i])):
                    if Aname[i][j] == message.from_user.id:
                        Aname[i][j + 1] = message.text
                        foundinlist = 1
            if foundinlist == 0:
                Aname.append([message.from_user.id, message.text])
            bot.send_message(message.from_user.id, "Вкажіть будь ласка ваш телефон для зв'язку з вами та подальшого оговорення замовлення, а також відправки звітності про виконане замовлення. Ви можете вказати ваші додаткові контактні дані(Email, telegram, viber і тд)", reply_markup=markup_reply)
            bot.register_next_step_handler(message, reg_phone)
        else:
            bot.send_message(message.from_user.id, text="Це не схоже на текст. Введіть будь ласка текст", reply_markup=markup_reply)
            bot.register_next_step_handler(message, reg_name)

def reg_phone(message):
    if message.text == 'Відмінити замовлення ❌':
        keyboardotmenazakaza = types.InlineKeyboardMarkup()
        key_yes_bez_photo = types.InlineKeyboardButton(text='Так', callback_data='yesotmenazakaza')
        keyboardotmenazakaza.add(key_yes_bez_photo)
        key_bez_photo = types.InlineKeyboardButton(text='Ні', callback_data='nootmenazakaza')
        keyboardotmenazakaza.add(key_bez_photo)
        question = 'Відмінити оформлення замовлення ❌'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboardotmenazakaza)
    else:
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_reply.add(buttonotmenazakaza)
        foundinlist = 0
        if message.content_type == 'text':
            for i in range(len(Aphone_client)):
                for j in range(len(Aphone_client[i])):
                    if Aphone_client[i][j] == message.from_user.id:
                        Aphone_client[i][j + 1] = message.text
                        foundinlist = 1
            if foundinlist == 0:
                Aphone_client.append([message.from_user.id, message.text])
            global to_deletekeyboard
            to_deletekeyboard = bot.send_message(message.from_user.id, text="Виберіть категорію розміщень", reply_markup=keyboard_osnownikategorii)
        else:
            bot.send_message(message.from_user.id, text="Це не схоже на текст. Введіть будь ласка текст", reply_markup=markup_reply)
            bot.register_next_step_handler(message, reg_phone)


def zagolovok_obiavlenia(message):
    if message.text == 'Відмінити замовлення ❌':
        keyboardotmenazakaza = types.InlineKeyboardMarkup()
        key_yes_bez_photo = types.InlineKeyboardButton(text='Так', callback_data='yesotmenazakaza')
        keyboardotmenazakaza.add(key_yes_bez_photo)
        key_bez_photo = types.InlineKeyboardButton(text='Ні', callback_data='nootmenazakaza')
        keyboardotmenazakaza.add(key_bez_photo)
        question = 'Відмінити оформлення замовлення ❌'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboardotmenazakaza)
    else:
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_reply.add(buttonotmenazakaza)
        foundinlist = 0
        if message.content_type == 'text':
            for i in range(len(Azagolovok_obiavlenia_onlytext)):
                for j in range(len(Azagolovok_obiavlenia_onlytext[i])):
                    if Azagolovok_obiavlenia_onlytext[i][j] == message.from_user.id:
                        Azagolovok_obiavlenia_onlytext[i][j + 1] = message.text
                        foundinlist = 1
            if foundinlist == 0:
                Azagolovok_obiavlenia_onlytext.append([message.from_user.id, message.text])
            bot.send_message(message.from_user.id, "Напишіть будь ласка текст оголошення", reply_markup=markup_reply)
            bot.register_next_step_handler(message, text_ogoloshenya)
        else:
            bot.send_message(message.from_user.id, text="Це не схоже на текст. Введіть будь ласка текст", reply_markup=markup_reply)
            bot.register_next_step_handler(message, zagolovok_obiavlenia)


def text_ogoloshenya(message):
    if message.text == 'Відмінити замовлення ❌':
        keyboardotmenazakaza = types.InlineKeyboardMarkup()
        key_yes_bez_photo = types.InlineKeyboardButton(text='Так', callback_data='yesotmenazakaza')
        keyboardotmenazakaza.add(key_yes_bez_photo)
        key_bez_photo = types.InlineKeyboardButton(text='Ні', callback_data='nootmenazakaza')
        keyboardotmenazakaza.add(key_bez_photo)
        question = 'Відмінити оформлення замовлення ❌'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboardotmenazakaza)
    else:
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_reply.add(buttonotmenazakaza)
        foundinlist = 0
        if message.content_type == 'text':
            for i in range(len(Atext_ogoloshenya_onlytext)):
                for j in range(len(Atext_ogoloshenya_onlytext[i])):
                    if Atext_ogoloshenya_onlytext[i][j] == message.from_user.id:
                        Atext_ogoloshenya_onlytext[i][j + 1] = message.text
                        foundinlist = 1
            if foundinlist == 0:
                Atext_ogoloshenya_onlytext.append([message.from_user.id, message.text])
            bot.send_message(message.from_user.id, "Напишіть будь ласка ціну яка буде вказана в оглошенні. Наприклад:100грн або 250$", reply_markup=markup_reply)
            bot.register_next_step_handler(message, price_uslugi)
        else:
            bot.send_message(message.from_user.id, text="Це не схоже на текст. Введіть будь ласка текст", reply_markup=markup_reply)
            bot.register_next_step_handler(message, text_ogoloshenya)


def price_uslugi(message):
    if message.text == 'Відмінити замовлення ❌':
        keyboardotmenazakaza = types.InlineKeyboardMarkup()
        key_yes_bez_photo = types.InlineKeyboardButton(text='Так', callback_data='yesotmenazakaza')
        keyboardotmenazakaza.add(key_yes_bez_photo)
        key_bez_photo = types.InlineKeyboardButton(text='Ні', callback_data='nootmenazakaza')
        keyboardotmenazakaza.add(key_bez_photo)
        question = 'Відмінити оформлення замовлення ❌'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboardotmenazakaza)
    else:
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_reply.add(buttonotmenazakaza)
        foundinlist = 0
        if message.content_type == 'text':
            for i in range(len(Aprice_uslugi_onlytext)):
                for j in range(len(Aprice_uslugi_onlytext[i])):
                    if Aprice_uslugi_onlytext[i][j] == message.from_user.id:
                        Aprice_uslugi_onlytext[i][j + 1] = message.text
                        foundinlist = 1
            if foundinlist == 0:
                Aprice_uslugi_onlytext.append([message.from_user.id, message.text])
            bot.send_message(message.from_user.id, "Вкажіть контакти для розміщення в оголошенні (ПІБ , тел, сайт, email)", reply_markup=markup_reply)
            bot.register_next_step_handler(message, kontaktitorozmist_in_ogoloshemya)
        else:
            bot.send_message(message.from_user.id, text="Це не схоже на текст. Введіть будь ласка текст", reply_markup=markup_reply)
            bot.register_next_step_handler(message, price_uslugi)

def kontaktitorozmist_in_ogoloshemya(message):
    if message.text == 'Відмінити замовлення ❌':
        keyboardotmenazakaza = types.InlineKeyboardMarkup()
        key_yes_bez_photo = types.InlineKeyboardButton(text='Так', callback_data='yesotmenazakaza')
        keyboardotmenazakaza.add(key_yes_bez_photo)
        key_bez_photo = types.InlineKeyboardButton(text='Ні', callback_data='nootmenazakaza')
        keyboardotmenazakaza.add(key_bez_photo)
        question = 'Відмінити оформлення замовлення ❌'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboardotmenazakaza)
    else:
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_reply.add(buttonotmenazakaza)
        foundinlist = 0
        if message.content_type == 'text':
            for i in range(len(Akontaktitorozmist_in_ogoloshemya_onlytext)):
                for j in range(len(Akontaktitorozmist_in_ogoloshemya_onlytext[i])):
                    if Akontaktitorozmist_in_ogoloshemya_onlytext[i][j] == message.from_user.id:
                        Akontaktitorozmist_in_ogoloshemya_onlytext[i][j + 1] = message.text
                        foundinlist = 1
            if foundinlist == 0:
                Akontaktitorozmist_in_ogoloshemya_onlytext.append([message.from_user.id, message.text])
            bot.send_message(message.from_user.id, "Вкажіть будь ласка регіон розміщення (Наприклад:Київ, Умань, Вся Україна)", reply_markup=markup_reply)
            bot.register_next_step_handler(message, regionrozmist_in_ogoloshemya)
        else:
            bot.send_message(message.from_user.id, text="Це не схоже на текст. Введіть будь ласка текст", reply_markup=markup_reply)
            bot.register_next_step_handler(message, kontaktitorozmist_in_ogoloshemya)


def regionrozmist_in_ogoloshemya(message):
    if message.text == 'Відмінити замовлення ❌':
        keyboardotmenazakaza = types.InlineKeyboardMarkup()
        key_yes_bez_photo = types.InlineKeyboardButton(text='Так', callback_data='yesotmenazakaza')
        keyboardotmenazakaza.add(key_yes_bez_photo)
        key_bez_photo = types.InlineKeyboardButton(text='Ні', callback_data='nootmenazakaza')
        keyboardotmenazakaza.add(key_bez_photo)
        question = 'Відмінити оформлення замовлення ❌'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboardotmenazakaza)
    else:
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_reply.add(buttonotmenazakaza)
        foundinlist = 0
        if message.content_type == 'text':
            for i in range(len(Aregionrozmist_in_ogoloshemya_onlytext)):
                for j in range(len(Aregionrozmist_in_ogoloshemya_onlytext[i])):
                    if Aregionrozmist_in_ogoloshemya_onlytext[i][j] == message.from_user.id:
                        Aregionrozmist_in_ogoloshemya_onlytext[i][j + 1] = message.text
                        foundinlist = 1
            if foundinlist == 0:
                Aregionrozmist_in_ogoloshemya_onlytext.append([message.from_user.id, message.text])
            bot.send_message(message.from_user.id, "Вкажіть будь ласка термін розміщення (тиждень, місяць, пів-року, рік)", reply_markup=markup_reply)
            bot.register_next_step_handler(message, termin_rozmist_in_ogoloshemya)
        else:
            bot.send_message(message.from_user.id, text="Це не схоже на текст. Введіть будь ласка текст", reply_markup=markup_reply)
            bot.register_next_step_handler(message, regionrozmist_in_ogoloshemya)


def termin_rozmist_in_ogoloshemya(message):
    if message.text == 'Відмінити замовлення ❌':
        keyboardotmenazakaza = types.InlineKeyboardMarkup()
        key_yes_bez_photo = types.InlineKeyboardButton(text='Так', callback_data='yesotmenazakaza')
        keyboardotmenazakaza.add(key_yes_bez_photo)
        key_bez_photo = types.InlineKeyboardButton(text='Ні', callback_data='nootmenazakaza')
        keyboardotmenazakaza.add(key_bez_photo)
        question = 'Відмінити оформлення замовлення ❌'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboardotmenazakaza)
    else:
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_reply.add(buttonotmenazakaza)
        foundinlist = 0
        if message.content_type == 'text':
            for i in range(len(Aterminrozmist_in_ogoloshemya_onlytext)):
                for j in range(len(Aterminrozmist_in_ogoloshemya_onlytext[i])):
                    if Aterminrozmist_in_ogoloshemya_onlytext[i][j] == message.from_user.id:
                        Aterminrozmist_in_ogoloshemya_onlytext[i][j + 1] = message.text
                        foundinlist = 1
            if foundinlist == 0:
                Aterminrozmist_in_ogoloshemya_onlytext.append([message.from_user.id, message.text])
            bot.send_message(message.from_user.id, "Додайте фото публікації", reply_markup=markup_reply)
            bot.register_next_step_handler(message, dobavtephotopublikatsiy)
        else:
            bot.send_message(message.from_user.id, text="Це не схоже на текст. Введіть будь ласка текст", reply_markup=markup_reply)
            bot.register_next_step_handler(message, termin_rozmist_in_ogoloshemya)



def dobavtephotopublikatsiy(message):
    markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup_reply.add(button1, button2, button3, button4, button5, button6)
    foundinlist = 0
    try:
        for i in range(len(Aphotopublikatsiy)):
            for j in range(len(Aphotopublikatsiy[i])):
                if Aphotopublikatsiy[i][j] == message.from_user.id:
                    Aphotopublikatsiy[i][j + 1] = message.photo[-1].file_id
                    foundinlist = 1
        if foundinlist == 0:
            Aphotopublikatsiy.append([message.from_user.id, message.photo[-1].file_id])
        foundinlist = 0
        bot.send_photo(message.from_user.id, message.photo[-1].file_id)
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Так', callback_data='yes')
        keyboard.add(key_yes)
        key_no = types.InlineKeyboardButton(text='Ні', callback_data='no')
        keyboard.add(key_no)
        question = 'Підтвердити замовлення ?'
        bot.send_message(message.from_user.id, text="Ваше замовлення прийнято системою.", reply_markup=markup_reply)
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
    except:
        foundinlist = 0
        for i in range(len(Aphotopublikatsiy_bezphoto)):
            for j in range(len(Aphotopublikatsiy_bezphoto[i])):
                if Aphotopublikatsiy_bezphoto[i][j] == message.from_user.id:
                    Aphotopublikatsiy_bezphoto[i][j + 1] = message.text
                    foundinlist = 1
        if foundinlist == 0:
            Aphotopublikatsiy_bezphoto.append([message.from_user.id, message.text])
        bot.send_message(message.from_user.id, 'Це не схоже на фото але я запишу це. Потім фото ви зможете відправити менеджеру @rozmist_com_ua')
        keyboard_bez_photo = types.InlineKeyboardMarkup()
        key_yes_bez_photo = types.InlineKeyboardButton(text='Так', callback_data='yesbezphoto')
        keyboard_bez_photo.add(key_yes_bez_photo)
        key_bez_photo = types.InlineKeyboardButton(text='Ні', callback_data='nobezphoto')
        keyboard_bez_photo.add(key_bez_photo)
        question = 'Підтвердити замовлення ?'
        bot.send_message(message.from_user.id, text="Ваше замовлення прийнято системою. 🏁", reply_markup=markup_reply)
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard_bez_photo)









@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global to_deletekeyboard
    notoclick = 0
    stopclick = 0
    notoclick_oformzak = 0
    stopclick_oformzak = 0
    nomer_zakaza = 0
    foundinlist = 0
    startingzakaz = 0
    if call.data == "yes":
        for i in range(len(Astopclick_oformzak)):
            for j in range(len(Astopclick_oformzak[i])):
                if Astopclick_oformzak[i][j] == call.message.chat.id:
                    stopclick_oformzak = Astopclick_oformzak[i][j + 1]
                    foundinlist = 1
        if foundinlist == 0:
            Astopclick_oformzak.append([call.message.chat.id, 0])
            stopclick_oformzak = 0
        foundinlist = 0
        for i in range(len(Anotoclick_oformzak)):
            for j in range(len(Anotoclick_oformzak[i])):
                if Anotoclick_oformzak[i][j] == call.message.chat.id:
                    Anotoclick_oformzak[i][j + 1] = 1
                    foundinlist = 1
                    notoclick_oformzak = 1
        if foundinlist == 0:
            Anotoclick_oformzak.append([call.message.chat.id, 1])
            notoclick_oformzak = 1
        foundinlist = 0
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_reply.add(button1, button2, button3, button4,button5,button6)
        if stopclick_oformzak == 0 and notoclick_oformzak == 1:
            for i in range(len(Astopclick_oformzak)):
                for j in range(len(Astopclick_oformzak[i])):
                    if Astopclick_oformzak[i][j] == call.message.chat.id:
                        Astopclick_oformzak[i][j + 1] = 1
                        foundinlist = 1
            if foundinlist == 0:
                Astopclick_oformzak.append([call.message.chat.id, 1])
            foundinlist = 0
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


            for i in range(len(Anomer_zakaza)):
                for j in range(len(Anomer_zakaza[i])):
                    if Anomer_zakaza[i][j] == call.message.chat.id:
                        nomer_zakaza = cursor.execute("SELECT userID FROM zakazy ORDER BY userID DESC LIMIT 1;").fetchall()
                        nomer_zakaza = nomer_zakaza[0][0]
                        nomer_zakaza = str(nomer_zakaza)
                        Anomer_zakaza[i][j + 1] = nomer_zakaza
                        foundinlist = 1
            if foundinlist == 0:
                nomer_zakaza = cursor.execute("SELECT userID FROM zakazy ORDER BY userID DESC LIMIT 1;").fetchall()
                nomer_zakaza = nomer_zakaza[0][0]
                nomer_zakaza = str(nomer_zakaza)
                Anomer_zakaza.append([call.message.chat.id, nomer_zakaza])
            foundinlist = 0

            sendtoadmin_info(call.message.chat.id)
            connect.commit()
            obnowclickdanni(call.message.chat.id)
            bot.send_message(call.message.chat.id, "Номер вашого замовлення : " + nomer_zakaza + " Будь ласка збережіть його")
            bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == "yesotmenazakaza":
        for i in range(len(Aname)):
            for j in range(len(Aname[i])):
                if Aname[i][j] == call.message.chat.id:
                    Aname[i][j + 1] = ""
                    foundinlist = 1
        if foundinlist == 0:
            Aname.append([call.message.chat.id, ""])
        foundinlist = 0
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_reply.add(button1, button2, button3, button4,button5,button6)
        for i in range(len(Astopclick_oformzak)):
            for j in range(len(Astopclick_oformzak[i])):
                if Astopclick_oformzak[i][j] == call.message.chat.id:
                    stopclick_oformzak = Astopclick_oformzak[i][j + 1]
                    foundinlist = 1
        if foundinlist == 0:
            Astopclick_oformzak.append([call.message.chat.id, 0])
            stopclick_oformzak = 0
        foundinlist = 0
        for i in range(len(Anotoclick_oformzak)):
            for j in range(len(Anotoclick_oformzak[i])):
                if Anotoclick_oformzak[i][j] == call.message.chat.id:
                    Anotoclick_oformzak[i][j + 1] = 1
                    foundinlist = 1
                    notoclick_oformzak = 1
        if foundinlist == 0:
            Anotoclick_oformzak.append([call.message.chat.id, 1])
            notoclick_oformzak = 1
        foundinlist = 0
        if stopclick_oformzak == 0 and notoclick_oformzak == 1:
            for i in range(len(Astopclick_oformzak)):
                for j in range(len(Astopclick_oformzak[i])):
                    if Astopclick_oformzak[i][j] == call.message.chat.id:
                        Astopclick_oformzak[i][j + 1] = 1
                        foundinlist = 1
            if foundinlist == 0:
                Astopclick_oformzak.append([call.message.chat.id, 1])
            foundinlist = 0
            bot.send_message(call.message.chat.id, "Ви відхилили ваше замовлення. ❌")
            bot.send_message(call.message.chat.id, "Ви можете повторно оформити замовлення або запитати в мене щось інше)))", reply_markup=markup_reply)
            obnowclickdanni(call.message.chat.id)
            bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == "nootmenazakaza":
        for i in range(len(Aname)):
            for j in range(len(Aname[i])):
                if Aname[i][j] == call.message.chat.id:
                    Aname[i][j + 1] = ""
                    foundinlist = 1
        if foundinlist == 0:
            Aname.append([call.message.chat.id, ""])
        foundinlist = 0
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_reply.add(buttonotmenazakaza)
        for i in range(len(Astopclick_oformzak)):
            for j in range(len(Astopclick_oformzak[i])):
                if Astopclick_oformzak[i][j] == call.message.chat.id:
                    stopclick_oformzak = Astopclick_oformzak[i][j + 1]
                    foundinlist = 1
        if foundinlist == 0:
            Astopclick_oformzak.append([call.message.chat.id, 0])
            stopclick_oformzak = 0
        foundinlist = 0
        for i in range(len(Anotoclick_oformzak)):
            for j in range(len(Anotoclick_oformzak[i])):
                if Anotoclick_oformzak[i][j] == call.message.chat.id:
                    Anotoclick_oformzak[i][j + 1] = 1
                    foundinlist = 1
                    notoclick_oformzak = 1
        if foundinlist == 0:
            Anotoclick_oformzak.append([call.message.chat.id, 1])
            notoclick_oformzak = 1
        foundinlist = 0
        if stopclick_oformzak == 0 and notoclick_oformzak == 1:
            stopclick_oformzak = 1
            bot.send_message(call.message.chat.id, "Добре, тоді починаємо оформляти замовлення з самого початку ✅", reply_markup=markup_reply)
            bot.send_message(call.message.chat.id, "Скажіть будь ласка як мені до вас звертатись")
            obnowclickdanni(call.message.chat.id)
            obnowclickstartornozakaz(call.message.chat.id)
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.register_next_step_handler(call.message, reg_name)
    elif call.data == "yesbezphoto":
        notoclick_oformzak = 1
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_reply.add(button1, button2, button3, button4,button5,button6)
        if stopclick_oformzak == 0 and notoclick_oformzak == 1:
            for i in range(len(Astopclick_oformzak)):
                for j in range(len(Astopclick_oformzak[i])):
                    if Astopclick_oformzak[i][j] == call.message.chat.id:
                        Astopclick_oformzak[i][j + 1] = 1
                        foundinlist = 1
            if foundinlist == 0:
                Astopclick_oformzak.append([call.message.chat.id, 1])
            foundinlist = 0
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
            for i in range(len(Anomer_zakaza)):
                for j in range(len(Anomer_zakaza[i])):
                    if Anomer_zakaza[i][j] == call.message.chat.id:
                        nomer_zakaza = cursor.execute("SELECT userID FROM zakazy ORDER BY userID DESC LIMIT 1;").fetchall()
                        nomer_zakaza = nomer_zakaza[0][0]
                        nomer_zakaza = str(nomer_zakaza)
                        Anomer_zakaza[i][j + 1] = nomer_zakaza
                        foundinlist = 1
            if foundinlist == 0:
                nomer_zakaza = cursor.execute("SELECT userID FROM zakazy ORDER BY userID DESC LIMIT 1;").fetchall()
                nomer_zakaza = nomer_zakaza[0][0]
                nomer_zakaza = str(nomer_zakaza)
                Anomer_zakaza.append([call.message.chat.id, nomer_zakaza])
            foundinlist = 0
            sendtoadmin_info_bezphoto(call.message.chat.id)
            connect.commit()
            obnowclickdanni(call.message.chat.id)
            bot.send_message(call.message.chat.id, "Номер вашого замовлення : " + nomer_zakaza + " Будь ласка збережіть його")
            bot.delete_message(call.message.chat.id, call.message.message_id)
    elif call.data == "no":
        for i in range(len(Aname)):
            for j in range(len(Aname[i])):
                if Aname[i][j] == call.message.chat.id:
                    Aname[i][j + 1] = ""
                    foundinlist = 1
        if foundinlist == 0:
            Aname.append([call.message.chat.id, ""])
        foundinlist = 0
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_reply.add(button1, button2, button3, button4,button5,button6)
        for i in range(len(Astopclick_oformzak)):
            for j in range(len(Astopclick_oformzak[i])):
                if Astopclick_oformzak[i][j] == call.message.chat.id:
                    stopclick_oformzak = Astopclick_oformzak[i][j + 1]
                    foundinlist = 1
        if foundinlist == 0:
            Astopclick_oformzak.append([call.message.chat.id, 0])
            stopclick_oformzak = 0
        foundinlist = 0
        for i in range(len(Anotoclick_oformzak)):
            for j in range(len(Anotoclick_oformzak[i])):
                if Anotoclick_oformzak[i][j] == call.message.chat.id:
                    Anotoclick_oformzak[i][j + 1] = 1
                    foundinlist = 1
                    notoclick_oformzak = 1
        if foundinlist == 0:
            Anotoclick_oformzak.append([call.message.chat.id, 1])
            notoclick_oformzak = 1
        foundinlist = 0
        if stopclick_oformzak == 0 and notoclick_oformzak == 1:
            for i in range(len(Astopclick_oformzak)):
                for j in range(len(Astopclick_oformzak[i])):
                    if Astopclick_oformzak[i][j] == call.message.chat.id:
                        Astopclick_oformzak[i][j + 1] = 1
                        foundinlist = 1
            if foundinlist == 0:
                Astopclick_oformzak.append([call.message.chat.id, 1])
            foundinlist = 0
            bot.send_message(call.message.chat.id, "Ви відхилили ваше замовлення. ❌", reply_markup=markup_reply)
            bot.send_message(call.message.chat.id, "Ви можете повторно оформити замовлення або запитати в мене щось інше)))")
            obnowclickdanni(call.message.chat.id)
            bot.delete_message(call.message.chat.id, call.message.message_id)
            #bot.register_next_step_handler(call.message,reg_name)
    elif call.data == "nobezphoto":
        for i in range(len(Aname)):
            for j in range(len(Aname[i])):
                if Aname[i][j] == call.message.chat.id:
                    Aname[i][j + 1] = ""
                    foundinlist = 1
        if foundinlist == 0:
            Aname.append([call.message.chat.id, ""])
        foundinlist = 0
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_reply.add(button1, button2, button3, button4,button5,button6)
        for i in range(len(Astopclick_oformzak)):
            for j in range(len(Astopclick_oformzak[i])):
                if Astopclick_oformzak[i][j] == call.message.chat.id:
                    stopclick_oformzak = Astopclick_oformzak[i][j + 1]
                    foundinlist = 1
        if foundinlist == 0:
            Astopclick_oformzak.append([call.message.chat.id, 0])
            stopclick_oformzak = 0
        foundinlist = 0
        for i in range(len(Anotoclick_oformzak)):
            for j in range(len(Anotoclick_oformzak[i])):
                if Anotoclick_oformzak[i][j] == call.message.chat.id:
                    Anotoclick_oformzak[i][j + 1] = 1
                    foundinlist = 1
                    notoclick_oformzak = 1
        if foundinlist == 0:
            Anotoclick_oformzak.append([call.message.chat.id, 1])
            notoclick_oformzak = 1
        foundinlist = 0
        if stopclick_oformzak == 0 and notoclick_oformzak == 1:
            for i in range(len(Astopclick_oformzak)):
                for j in range(len(Astopclick_oformzak[i])):
                    if Astopclick_oformzak[i][j] == call.message.chat.id:
                        Astopclick_oformzak[i][j + 1] = 1
                        foundinlist = 1
            if foundinlist == 0:
                Astopclick_oformzak.append([call.message.chat.id, 1])
            foundinlist = 0
            bot.send_message(call.message.chat.id, "Ви відхилили ваше замовлення. ❌", reply_markup=markup_reply)
            bot.send_message(call.message.chat.id, "Ви можете повторно оформити замовлення або запитати в мене щось інше)))")
            obnowclickdanni(call.message.chat.id)
            bot.delete_message(call.message.chat.id, call.message.message_id)
            #bot.register_next_step_handler(call.message,reg_name)
    elif call.data == "go_to_manager":
        bot.send_message(call.message.chat.id,"@rozmist_com_ua")
    elif call.data == "oform_zakaz":
        for i in range(len(Astartingzakaz)):
            for j in range(len(Astartingzakaz[i])):
                if Astartingzakaz[i][j] == call.message.chat.id:
                    if Astartingzakaz[i][j + 1] == 0:
                        Astartingzakaz[i][j + 1] = 1
                        foundinlist = 1
                        startingzakaz = 0
                    elif Astartingzakaz[i][j + 1] == 1:
                        foundinlist = 1
                        startingzakaz = 1
        if foundinlist == 0:
            Astartingzakaz.append([call.message.chat.id, 1])
            startingzakaz = 0
        foundinlist = 0

        if startingzakaz == 0:
            markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup_reply.add(buttonotmenazakaza)
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.send_message(call.message.chat.id,"Скажіть будь ласка як мені до вас звертатись", reply_markup=markup_reply)
            bot.register_next_step_handler(call.message,reg_name)
    elif call.data == "see_card_rozmist":
        bot.send_message(call.message.chat.id, allsitestext)
    elif call.data == "key1_detskiymir":
        for i in range(len(Astopclick)):
            for j in range(len(Astopclick[i])):
                if Astopclick[i][j] == call.message.chat.id:
                    stopclick = Astopclick[i][j + 1]
                    foundinlist = 1
        if foundinlist == 0:
            Astopclick.append([call.message.chat.id, 0])
            stopclick = 0
        foundinlist = 0
        for i in range(len(Anotoclick)):
            for j in range(len(Anotoclick[i])):
                if Anotoclick[i][j] == call.message.chat.id:
                    Anotoclick[i][j + 1] = 1
                    foundinlist = 1
                    notoclick = 1
        if foundinlist == 0:
            Anotoclick_oformzak.append([call.message.chat.id, 1])
            notoclick = 1
        if stopclick == 0 and notoclick == 1:
            for i in range(len(Aosnownaya_kategoriya_todatabase)):
                for j in range(len(Aosnownaya_kategoriya_todatabase[i])):
                    if Aosnownaya_kategoriya_todatabase[i][j] == call.message.chat.id:
                        Aosnownaya_kategoriya_todatabase[i][j + 1] = "Дитячий світ"
                        foundinlist = 1
            if foundinlist == 0:
                Aosnownaya_kategoriya_todatabase.append([call.message.chat.id, "Дитячий світ"])
            foundinlist = 0
            bot.send_message(call.message.chat.id, "Ваша категорія дитячий світ")
            bot.send_message(call.message.chat.id, "Введіть заголовок оголошення")
            for i in range(len(Astopclick)):
                for j in range(len(Astopclick[i])):
                    if Astopclick[i][j] == call.message.chat.id:
                        Astopclick[i][j + 1] = 1
                        foundinlist = 1
            if foundinlist == 0:
                Astopclick.append([call.message.chat.id, 1])
            foundinlist = 0
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.register_next_step_handler(call.message,zagolovok_obiavlenia)
    elif call.data == "key2_neruhomist":
        for i in range(len(Astopclick)):
            for j in range(len(Astopclick[i])):
                if Astopclick[i][j] == call.message.chat.id:
                    stopclick = Astopclick[i][j + 1]
                    foundinlist = 1
        if foundinlist == 0:
            Astopclick.append([call.message.chat.id, 0])
            stopclick = 0
        foundinlist = 0
        for i in range(len(Anotoclick)):
            for j in range(len(Anotoclick[i])):
                if Anotoclick[i][j] == call.message.chat.id:
                    Anotoclick[i][j + 1] = 1
                    foundinlist = 1
                    notoclick = 1
        if foundinlist == 0:
            Anotoclick_oformzak.append([call.message.chat.id, 1])
            notoclick = 1
        if stopclick == 0 and notoclick == 1:
            for i in range(len(Aosnownaya_kategoriya_todatabase)):
                for j in range(len(Aosnownaya_kategoriya_todatabase[i])):
                    if Aosnownaya_kategoriya_todatabase[i][j] == call.message.chat.id:
                        Aosnownaya_kategoriya_todatabase[i][j + 1] = "Нерухомість"
                        foundinlist = 1
            if foundinlist == 0:
                Aosnownaya_kategoriya_todatabase.append([call.message.chat.id, "Нерухомість"])
            foundinlist = 0
            bot.send_message(call.message.chat.id, "Ваша категорія Нерухомість")
            bot.send_message(call.message.chat.id, "Введіть заголовок оголошення")
            for i in range(len(Astopclick)):
                for j in range(len(Astopclick[i])):
                    if Astopclick[i][j] == call.message.chat.id:
                        Astopclick[i][j + 1] = 1
                        foundinlist = 1
            if foundinlist == 0:
                Astopclick.append([call.message.chat.id, 1])
            foundinlist = 0
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.register_next_step_handler(call.message,zagolovok_obiavlenia)
    elif call.data == "key3_transport":
        for i in range(len(Astopclick)):
            for j in range(len(Astopclick[i])):
                if Astopclick[i][j] == call.message.chat.id:
                    stopclick = Astopclick[i][j + 1]
                    foundinlist = 1
        if foundinlist == 0:
            Astopclick.append([call.message.chat.id, 0])
            stopclick = 0
        foundinlist = 0
        for i in range(len(Anotoclick)):
            for j in range(len(Anotoclick[i])):
                if Anotoclick[i][j] == call.message.chat.id:
                    Anotoclick[i][j + 1] = 1
                    foundinlist = 1
                    notoclick = 1
        if foundinlist == 0:
            Anotoclick_oformzak.append([call.message.chat.id, 1])
            notoclick = 1
        if stopclick == 0 and notoclick == 1:
            for i in range(len(Aosnownaya_kategoriya_todatabase)):
                for j in range(len(Aosnownaya_kategoriya_todatabase[i])):
                    if Aosnownaya_kategoriya_todatabase[i][j] == call.message.chat.id:
                        Aosnownaya_kategoriya_todatabase[i][j + 1] = "Транспорт"
                        foundinlist = 1
            if foundinlist == 0:
                Aosnownaya_kategoriya_todatabase.append([call.message.chat.id, "Транспорт"])
            foundinlist = 0
            bot.send_message(call.message.chat.id, "Ваша категорія Транспорт")
            bot.send_message(call.message.chat.id, "Введіть заголовок оголошення")
            for i in range(len(Astopclick)):
                for j in range(len(Astopclick[i])):
                    if Astopclick[i][j] == call.message.chat.id:
                        Astopclick[i][j + 1] = 1
                        foundinlist = 1
            if foundinlist == 0:
                Astopclick.append([call.message.chat.id, 1])
            foundinlist = 0
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.register_next_step_handler(call.message,zagolovok_obiavlenia)
    elif call.data == "key4_avtozapchasti":
        for i in range(len(Astopclick)):
            for j in range(len(Astopclick[i])):
                if Astopclick[i][j] == call.message.chat.id:
                    stopclick = Astopclick[i][j + 1]
                    foundinlist = 1
        if foundinlist == 0:
            Astopclick.append([call.message.chat.id, 0])
            stopclick = 0
        foundinlist = 0
        for i in range(len(Anotoclick)):
            for j in range(len(Anotoclick[i])):
                if Anotoclick[i][j] == call.message.chat.id:
                    Anotoclick[i][j + 1] = 1
                    foundinlist = 1
                    notoclick = 1
        if foundinlist == 0:
            Anotoclick_oformzak.append([call.message.chat.id, 1])
            notoclick = 1
        if stopclick == 0 and notoclick == 1:
            for i in range(len(Aosnownaya_kategoriya_todatabase)):
                for j in range(len(Aosnownaya_kategoriya_todatabase[i])):
                    if Aosnownaya_kategoriya_todatabase[i][j] == call.message.chat.id:
                        Aosnownaya_kategoriya_todatabase[i][j + 1] = "Авто-Запчастини"
                        foundinlist = 1
            if foundinlist == 0:
                Aosnownaya_kategoriya_todatabase.append([call.message.chat.id, "Авто-Запчастини"])
            foundinlist = 0
            bot.send_message(call.message.chat.id, "Ваша категорія Авто-Запчастини")
            bot.send_message(call.message.chat.id, "Введіть заголовок оголошення")
            for i in range(len(Astopclick)):
                for j in range(len(Astopclick[i])):
                    if Astopclick[i][j] == call.message.chat.id:
                        Astopclick[i][j + 1] = 1
                        foundinlist = 1
            if foundinlist == 0:
                Astopclick.append([call.message.chat.id, 1])
            foundinlist = 0
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.register_next_step_handler(call.message,zagolovok_obiavlenia)
    elif call.data == "key5_work":
        for i in range(len(Astopclick)):
            for j in range(len(Astopclick[i])):
                if Astopclick[i][j] == call.message.chat.id:
                    stopclick = Astopclick[i][j + 1]
                    foundinlist = 1
        if foundinlist == 0:
            Astopclick.append([call.message.chat.id, 0])
            stopclick = 0
        foundinlist = 0
        for i in range(len(Anotoclick)):
            for j in range(len(Anotoclick[i])):
                if Anotoclick[i][j] == call.message.chat.id:
                    Anotoclick[i][j + 1] = 1
                    foundinlist = 1
                    notoclick = 1
        if foundinlist == 0:
            Anotoclick_oformzak.append([call.message.chat.id, 1])
            notoclick = 1
        if stopclick == 0 and notoclick == 1:
            for i in range(len(Aosnownaya_kategoriya_todatabase)):
                for j in range(len(Aosnownaya_kategoriya_todatabase[i])):
                    if Aosnownaya_kategoriya_todatabase[i][j] == call.message.chat.id:
                        Aosnownaya_kategoriya_todatabase[i][j + 1] = "Робота"
                        foundinlist = 1
            if foundinlist == 0:
                Aosnownaya_kategoriya_todatabase.append([call.message.chat.id, "Робота"])
            foundinlist = 0
            bot.send_message(call.message.chat.id, "Ваша категорія Робота")
            bot.send_message(call.message.chat.id, "Введіть заголовок оголошення")
            for i in range(len(Astopclick)):
                for j in range(len(Astopclick[i])):
                    if Astopclick[i][j] == call.message.chat.id:
                        Astopclick[i][j + 1] = 1
                        foundinlist = 1
            if foundinlist == 0:
                Astopclick.append([call.message.chat.id, 1])
            foundinlist = 0
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.register_next_step_handler(call.message,zagolovok_obiavlenia)
    elif call.data == "key6_tvarini":
        for i in range(len(Astopclick)):
            for j in range(len(Astopclick[i])):
                if Astopclick[i][j] == call.message.chat.id:
                    stopclick = Astopclick[i][j + 1]
                    foundinlist = 1
        if foundinlist == 0:
            Astopclick.append([call.message.chat.id, 0])
            stopclick = 0
        foundinlist = 0
        for i in range(len(Anotoclick)):
            for j in range(len(Anotoclick[i])):
                if Anotoclick[i][j] == call.message.chat.id:
                    Anotoclick[i][j + 1] = 1
                    foundinlist = 1
                    notoclick = 1
        if foundinlist == 0:
            Anotoclick_oformzak.append([call.message.chat.id, 1])
            notoclick = 1
        if stopclick == 0 and notoclick == 1:
            for i in range(len(Aosnownaya_kategoriya_todatabase)):
                for j in range(len(Aosnownaya_kategoriya_todatabase[i])):
                    if Aosnownaya_kategoriya_todatabase[i][j] == call.message.chat.id:
                        Aosnownaya_kategoriya_todatabase[i][j + 1] = "Тварини"
                        foundinlist = 1
            if foundinlist == 0:
                Aosnownaya_kategoriya_todatabase.append([call.message.chat.id, "Тварини"])
            foundinlist = 0
            bot.send_message(call.message.chat.id, "Ваша категорія Тварини")
            bot.send_message(call.message.chat.id, "Введіть заголовок оголошення")
            for i in range(len(Astopclick)):
                for j in range(len(Astopclick[i])):
                    if Astopclick[i][j] == call.message.chat.id:
                        Astopclick[i][j + 1] = 1
                        foundinlist = 1
            if foundinlist == 0:
                Astopclick.append([call.message.chat.id, 1])
            foundinlist = 0
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.register_next_step_handler(call.message,zagolovok_obiavlenia)
    elif call.data == "key7_domisad":
        for i in range(len(Astopclick)):
            for j in range(len(Astopclick[i])):
                if Astopclick[i][j] == call.message.chat.id:
                    stopclick = Astopclick[i][j + 1]
                    foundinlist = 1
        if foundinlist == 0:
            Astopclick.append([call.message.chat.id, 0])
            stopclick = 0
        foundinlist = 0
        for i in range(len(Anotoclick)):
            for j in range(len(Anotoclick[i])):
                if Anotoclick[i][j] == call.message.chat.id:
                    Anotoclick[i][j + 1] = 1
                    foundinlist = 1
                    notoclick = 1
        if foundinlist == 0:
            Anotoclick_oformzak.append([call.message.chat.id, 1])
            notoclick = 1
        if stopclick == 0 and notoclick == 1:
            for i in range(len(Aosnownaya_kategoriya_todatabase)):
                for j in range(len(Aosnownaya_kategoriya_todatabase[i])):
                    if Aosnownaya_kategoriya_todatabase[i][j] == call.message.chat.id:
                        Aosnownaya_kategoriya_todatabase[i][j + 1] = "Дом і сад"
                        foundinlist = 1
            if foundinlist == 0:
                Aosnownaya_kategoriya_todatabase.append([call.message.chat.id, "Дом і сад"])
            foundinlist = 0
            bot.send_message(call.message.chat.id, "Ваша категорія Дом і сад")
            bot.send_message(call.message.chat.id, "Введіть заголовок оголошення")
            for i in range(len(Astopclick)):
                for j in range(len(Astopclick[i])):
                    if Astopclick[i][j] == call.message.chat.id:
                        Astopclick[i][j + 1] = 1
                        foundinlist = 1
            if foundinlist == 0:
                Astopclick.append([call.message.chat.id, 1])
            foundinlist = 0
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.register_next_step_handler(call.message,zagolovok_obiavlenia)
    elif call.data == "key8_elektronica":
        for i in range(len(Astopclick)):
            for j in range(len(Astopclick[i])):
                if Astopclick[i][j] == call.message.chat.id:
                    stopclick = Astopclick[i][j + 1]
                    foundinlist = 1
        if foundinlist == 0:
            Astopclick.append([call.message.chat.id, 0])
            stopclick = 0
        foundinlist = 0
        for i in range(len(Anotoclick)):
            for j in range(len(Anotoclick[i])):
                if Anotoclick[i][j] == call.message.chat.id:
                    Anotoclick[i][j + 1] = 1
                    foundinlist = 1
                    notoclick = 1
        if foundinlist == 0:
            Anotoclick_oformzak.append([call.message.chat.id, 1])
            notoclick = 1
        if stopclick == 0 and notoclick == 1:
            for i in range(len(Aosnownaya_kategoriya_todatabase)):
                for j in range(len(Aosnownaya_kategoriya_todatabase[i])):
                    if Aosnownaya_kategoriya_todatabase[i][j] == call.message.chat.id:
                        Aosnownaya_kategoriya_todatabase[i][j + 1] = "Електроніка"
                        foundinlist = 1
            if foundinlist == 0:
                Aosnownaya_kategoriya_todatabase.append([call.message.chat.id, "Електроніка"])
            foundinlist = 0
            bot.send_message(call.message.chat.id, "Ваша категорія Електроніка")
            bot.send_message(call.message.chat.id, "Введіть заголовок оголошення")
            for i in range(len(Astopclick)):
                for j in range(len(Astopclick[i])):
                    if Astopclick[i][j] == call.message.chat.id:
                        Astopclick[i][j + 1] = 1
                        foundinlist = 1
            if foundinlist == 0:
                Astopclick.append([call.message.chat.id, 1])
            foundinlist = 0
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.register_next_step_handler(call.message,zagolovok_obiavlenia)
    elif call.data == "key9_biznestaposlugi":
        for i in range(len(Astopclick)):
            for j in range(len(Astopclick[i])):
                if Astopclick[i][j] == call.message.chat.id:
                    stopclick = Astopclick[i][j + 1]
                    foundinlist = 1
        if foundinlist == 0:
            Astopclick.append([call.message.chat.id, 0])
            stopclick = 0
        foundinlist = 0
        for i in range(len(Anotoclick)):
            for j in range(len(Anotoclick[i])):
                if Anotoclick[i][j] == call.message.chat.id:
                    Anotoclick[i][j + 1] = 1
                    foundinlist = 1
                    notoclick = 1
        if foundinlist == 0:
            Anotoclick_oformzak.append([call.message.chat.id, 1])
            notoclick = 1
        if stopclick == 0 and notoclick == 1:
            for i in range(len(Aosnownaya_kategoriya_todatabase)):
                for j in range(len(Aosnownaya_kategoriya_todatabase[i])):
                    if Aosnownaya_kategoriya_todatabase[i][j] == call.message.chat.id:
                        Aosnownaya_kategoriya_todatabase[i][j + 1] = "Бізнес та послуги"
                        foundinlist = 1
            if foundinlist == 0:
                Aosnownaya_kategoriya_todatabase.append([call.message.chat.id, "Бізнес та послуги"])
            foundinlist = 0
            bot.send_message(call.message.chat.id, "Ваша категорія Бізнес та послуги")
            bot.send_message(call.message.chat.id, "Введіть заголовок оголошення")
            for i in range(len(Astopclick)):
                for j in range(len(Astopclick[i])):
                    if Astopclick[i][j] == call.message.chat.id:
                        Astopclick[i][j + 1] = 1
                        foundinlist = 1
            if foundinlist == 0:
                Astopclick.append([call.message.chat.id, 1])
            foundinlist = 0
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.register_next_step_handler(call.message,zagolovok_obiavlenia)
    elif call.data == "key10_modaistil":
        for i in range(len(Astopclick)):
            for j in range(len(Astopclick[i])):
                if Astopclick[i][j] == call.message.chat.id:
                    stopclick = Astopclick[i][j + 1]
                    foundinlist = 1
        if foundinlist == 0:
            Astopclick.append([call.message.chat.id, 0])
            stopclick = 0
        foundinlist = 0
        for i in range(len(Anotoclick)):
            for j in range(len(Anotoclick[i])):
                if Anotoclick[i][j] == call.message.chat.id:
                    Anotoclick[i][j + 1] = 1
                    foundinlist = 1
                    notoclick = 1
        if foundinlist == 0:
            Anotoclick_oformzak.append([call.message.chat.id, 1])
            notoclick = 1
        if stopclick == 0 and notoclick == 1:
            for i in range(len(Aosnownaya_kategoriya_todatabase)):
                for j in range(len(Aosnownaya_kategoriya_todatabase[i])):
                    if Aosnownaya_kategoriya_todatabase[i][j] == call.message.chat.id:
                        Aosnownaya_kategoriya_todatabase[i][j + 1] = "Мода та стиль"
                        foundinlist = 1
            if foundinlist == 0:
                Aosnownaya_kategoriya_todatabase.append([call.message.chat.id, "Мода та стиль"])
            foundinlist = 0
            bot.send_message(call.message.chat.id, "Ваша категорія Мода та стиль")
            bot.send_message(call.message.chat.id, "Введіть заголовок оголошення")
            for i in range(len(Astopclick)):
                for j in range(len(Astopclick[i])):
                    if Astopclick[i][j] == call.message.chat.id:
                        Astopclick[i][j + 1] = 1
                        foundinlist = 1
            if foundinlist == 0:
                Astopclick.append([call.message.chat.id, 1])
            foundinlist = 0
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.register_next_step_handler(call.message,zagolovok_obiavlenia)
    elif call.data == "key11_hobbiotdihisport":
        for i in range(len(Astopclick)):
            for j in range(len(Astopclick[i])):
                if Astopclick[i][j] == call.message.chat.id:
                    stopclick = Astopclick[i][j + 1]
                    foundinlist = 1
        if foundinlist == 0:
            Astopclick.append([call.message.chat.id, 0])
            stopclick = 0
        foundinlist = 0
        for i in range(len(Anotoclick)):
            for j in range(len(Anotoclick[i])):
                if Anotoclick[i][j] == call.message.chat.id:
                    Anotoclick[i][j + 1] = 1
                    foundinlist = 1
                    notoclick = 1
        if foundinlist == 0:
            Anotoclick_oformzak.append([call.message.chat.id, 1])
            notoclick = 1
        if stopclick == 0 and notoclick == 1:
            for i in range(len(Aosnownaya_kategoriya_todatabase)):
                for j in range(len(Aosnownaya_kategoriya_todatabase[i])):
                    if Aosnownaya_kategoriya_todatabase[i][j] == call.message.chat.id:
                        Aosnownaya_kategoriya_todatabase[i][j + 1] = "Хоббі відпочинок та спорт"
                        foundinlist = 1
            if foundinlist == 0:
                Aosnownaya_kategoriya_todatabase.append([call.message.chat.id, "Хоббі відпочинок та спорт"])
            foundinlist = 0
            bot.send_message(call.message.chat.id, "Ваша категорія Хоббі відпочинок та спорт")
            bot.send_message(call.message.chat.id, "Введіть заголовок оголошення")
            for i in range(len(Astopclick)):
                for j in range(len(Astopclick[i])):
                    if Astopclick[i][j] == call.message.chat.id:
                        Astopclick[i][j + 1] = 1
                        foundinlist = 1
            if foundinlist == 0:
                Astopclick.append([call.message.chat.id, 1])
            foundinlist = 0
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.register_next_step_handler(call.message,zagolovok_obiavlenia)
    elif call.data == "key12_otdamdarom":
        for i in range(len(Astopclick)):
            for j in range(len(Astopclick[i])):
                if Astopclick[i][j] == call.message.chat.id:
                    stopclick = Astopclick[i][j + 1]
                    foundinlist = 1
        if foundinlist == 0:
            Astopclick.append([call.message.chat.id, 0])
            stopclick = 0
        foundinlist = 0
        for i in range(len(Anotoclick)):
            for j in range(len(Anotoclick[i])):
                if Anotoclick[i][j] == call.message.chat.id:
                    Anotoclick[i][j + 1] = 1
                    foundinlist = 1
                    notoclick = 1
        if foundinlist == 0:
            Anotoclick_oformzak.append([call.message.chat.id, 1])
            notoclick = 1
        if stopclick == 0 and notoclick == 1:
            for i in range(len(Aosnownaya_kategoriya_todatabase)):
                for j in range(len(Aosnownaya_kategoriya_todatabase[i])):
                    if Aosnownaya_kategoriya_todatabase[i][j] == call.message.chat.id:
                        Aosnownaya_kategoriya_todatabase[i][j + 1] = "Віддам даром"
                        foundinlist = 1
            if foundinlist == 0:
                Aosnownaya_kategoriya_todatabase.append([call.message.chat.id, "Віддам даром"])
            foundinlist = 0
            bot.send_message(call.message.chat.id, "Ваша категорія Віддам даром")
            bot.send_message(call.message.chat.id, "Введіть заголовок оголошення")
            for i in range(len(Astopclick)):
                for j in range(len(Astopclick[i])):
                    if Astopclick[i][j] == call.message.chat.id:
                        Astopclick[i][j + 1] = 1
                        foundinlist = 1
            if foundinlist == 0:
                Astopclick.append([call.message.chat.id, 1])
            foundinlist = 0
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.register_next_step_handler(call.message,zagolovok_obiavlenia)
    elif call.data == "key13_obminiay":
        for i in range(len(Astopclick)):
            for j in range(len(Astopclick[i])):
                if Astopclick[i][j] == call.message.chat.id:
                    stopclick = Astopclick[i][j + 1]
                    foundinlist = 1
        if foundinlist == 0:
            Astopclick.append([call.message.chat.id, 0])
            stopclick = 0
        foundinlist = 0
        for i in range(len(Anotoclick)):
            for j in range(len(Anotoclick[i])):
                if Anotoclick[i][j] == call.message.chat.id:
                    Anotoclick[i][j + 1] = 1
                    foundinlist = 1
                    notoclick = 1
        if foundinlist == 0:
            Anotoclick_oformzak.append([call.message.chat.id, 1])
            notoclick = 1
        if stopclick == 0 and notoclick == 1:
            for i in range(len(Aosnownaya_kategoriya_todatabase)):
                for j in range(len(Aosnownaya_kategoriya_todatabase[i])):
                    if Aosnownaya_kategoriya_todatabase[i][j] == call.message.chat.id:
                        Aosnownaya_kategoriya_todatabase[i][j + 1] = "Обміняю"
                        foundinlist = 1
            if foundinlist == 0:
                Aosnownaya_kategoriya_todatabase.append([call.message.chat.id, "Обміняю"])
            foundinlist = 0
            bot.send_message(call.message.chat.id, "Ваша категорія Обміняю")
            bot.send_message(call.message.chat.id, "Введіть заголовок оголошення")
            for i in range(len(Astopclick)):
                for j in range(len(Astopclick[i])):
                    if Astopclick[i][j] == call.message.chat.id:
                        Astopclick[i][j + 1] = 1
                        foundinlist = 1
            if foundinlist == 0:
                Astopclick.append([call.message.chat.id, 1])
            foundinlist = 0
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.register_next_step_handler(call.message,zagolovok_obiavlenia)




bot.polling(none_stop=True, interval=0)
