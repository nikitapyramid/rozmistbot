import telebot
from telebot import types

token = ""



dogoviroferty = "Читайте договір у нас на сайті https://www.rozmist.com.ua/dogovoroferty.html"



allsitestext = "1.https://www.057.ua/\n2.https://www.board.com.ua/\n3.https://www.ukrhome.net/\n4.https://www.portal.kharkov.ua/board/\n5.https://www.freetorg.com.ua/\n6.http://ukrapk.com/board/\n7.https://www.freeboard.com.ua/board.php\n8.http://kiev.localmart.ua/\n9.http://www.ukrcommerce.com/\n10.http://odessa24.net/board/\n11.http://buysell.com.ua/\n12.https://optiua.info/ru/adv_feed.php\n13.https://bazar.ua/kiev/search/\n14.https://stolbik.ua/\n15.http://globaltrade.com.ua/\n16.https://kiev.sindom.com.ua/\n17.http://www.ukrobyava.com.ua/\n18.https://kyiv.ukrboard.com.ua/\n19.https://kiev.bboard.com.ua/\n20.https://kiev.bboard.com.ua/\n21.https://www.ukrhard.com.ua/\n22.https://eam.com.ua/\n23.https://bulletin-board.com.ua/\n24.https://ukrgo.com.ua/\n25.https://onboard.net.ua/board/\n26.https://ukrcomp.com.ua/\n27.https://udt.com.ua/\n28.https://mobile-phones.com.ua/\n29.https://freelist.com.ua/\n30.https://vdalo.com.ua/\n31.https://vtorge.com.ua/\n32.https://businessland.com.ua/\n33.https://bizmarket.com.ua/\n34.https://aviso-online.com.ua/\n35.https://dosochka.com.ua/\n36.https://classifieds.com.ua/\n37.https://igazeta.com.ua/\n38.https://prodaga.com.ua/\n39.https://privatmarket.com/\n40.https://tradecenter.com.ua/\n41.https://tradecenter.com.ua/\n42.https://nashadoska.com/\n43.https://kharkovmarket.com/\n44.https://www.webdoska.com/\n45.https://kievmarket.com/\n46.https://www.webdoska.net\n47.http://kiev.adiso.com.ua/\n48.https://www.tolkay.com.ua/\n49.https://kievboard.com/\n50.http://gorodnaladoni.com/kiev/\n51.https://kiev.salexy.com.ua/\n52.https://myboard.com.ua/\n53.https://www.44.ua/\n54.http://pomidore.com/\n55.https://jarmarok.com.ua/ru/\n56.https://prosto.ua/\n57.http://sdachi.net.ua/\n58.http://www.ekomok.kiev.ua/\n59.https://torbinka.com/kiev/\n60.http://www.torginform.kiev.ua/\n61.http://www.ilotok.kiev.ua/\n62.https://www.62.ua/\n63.https://www.0642.ua/\n64.https://www.048.ua/\n65.https://www.3652.ru/\n66.https://www.061.ua/\n67.https://www.056.ua/\n68.https://www.032.ua/\n69.https://www.0512.com.ua/\n70.https://www.0542.ua/\n71.https://www.0352.ua/\n72.https://www.0412.ua/\n73.https://www.0532.ua/\n74.https://www.0432.ua/\n75.https://www.0522.ua/\n76.https://www.0552.ua/\n77.https://www.0342.ua/\n78.https://www.0362.ua/\n79.https://www.0332.ua/\n80.https://kiev.avizinfo.com.ua/\n81.http://kiev.comissionka.net/\n82.https://takinado.com.ua/kiev/\n83.https://allkharkov.info/\n84.http://board.club.co.ua/\n85.http://aviso.at.ua/board/\n86.https://obyavlenie.com.ua/\n87.http://ad-free.ru/\n88.https://sbo.ua/kiev/\n89.https://www.i-r.kiev.ua/\n90.https://www.vsesdelki.kiev.ua/\n91.https://www.admir.kiev.ua/\n92.https://jandooo.com/\n93.https://ukrainebazar.com/\n94.http://www.pulsinfo.ua/\n95.http://doska24.info/board/\n96.http://board.i.ua/\n97.http://board.join.ua/\n98.http://fn.at.ua/\n99.https://www.portal.kharkov.ua/\n100.http://bazar.ua/\n"


oformzakaztext = "Для оформлення замовлення відправте менеджеру в telegram @rozmist_com_ua наступні данні:\n- Категорія розміщення\n- Заголовок\n- Текст оголошення\n- Ціна в оголошенні\n- Зображення(рекомендуємо)\n- Регіон розміщення\n- Контактна інформация яка буде вказана в оголошенні(Телефон, Email, Сайт, Ім'я)\n- Період розміщення: тиждень, місяць, пів-року, рік.\n\n\nПісля оформлення замовлення будь ласка проведіть оплату в 350 грн та очікуйте виконання на протязі 3 робочих днів"


oplatatext = "До сплати 350 грн за розміщення на 100 дошок оголошень. Оплата приймається на карту ПриватБанк або за реквізитами:\n\nБудера Василь Васильович: 4149629388086803\n\nНаименование получателя: КОРП.IНТЕЛЕКТУАЛЬНИХ ТЕХНОЛОГIЙ ТОВ Код отримувача: 40286580 Рахунок IBAN: UA363052990000026000006200766 Банк: АТ КБ ПРИВАТ_БАНК\n\nВ коментарії до платежу обов'язково вкажіть - Оплата за розміщення на дошках оголошень в іншому випадку оплата буде вважатися не дійсною.\n\nПісля проведення оплати відправте нам чек на email адресу rozmist.com.ua@gmail.com або в telegram @rozmist_com_ua. Ваше замовлення буде виконане на протязі 3 робочих днів після підтвердження оплати\n\n"

keyboard_osnownikategorii = types.InlineKeyboardMarkup()
key1_detskiymir = types.InlineKeyboardButton(text='Дитячий світ', callback_data='key1_detskiymir')
keyboard_osnownikategorii.add(key1_detskiymir)
key2_neruhomist = types.InlineKeyboardButton(text='Нерухомість', callback_data='key2_neruhomist')
keyboard_osnownikategorii.add(key2_neruhomist)
key3_transport = types.InlineKeyboardButton(text='Транспорт', callback_data='key3_transport')
keyboard_osnownikategorii.add(key3_transport)
key4_avtozapchasti = types.InlineKeyboardButton(text='Авто-Запчастини', callback_data='key4_avtozapchasti')
keyboard_osnownikategorii.add(key4_avtozapchasti)
key5_work = types.InlineKeyboardButton(text='Робота', callback_data='key5_work')
keyboard_osnownikategorii.add(key5_work)
key6_tvarini = types.InlineKeyboardButton(text='Тварини', callback_data='key6_tvarini')
keyboard_osnownikategorii.add(key6_tvarini)
key7_domisad = types.InlineKeyboardButton(text='Дом і сад', callback_data='key7_domisad')
keyboard_osnownikategorii.add(key7_domisad)
key8_elektronica = types.InlineKeyboardButton(text='Електроніка', callback_data='key8_elektronica')
keyboard_osnownikategorii.add(key8_elektronica)
key9_biznestaposlugi = types.InlineKeyboardButton(text='Бізнес та послуги', callback_data='key9_biznestaposlugi')
keyboard_osnownikategorii.add(key9_biznestaposlugi)
key10_modaistil = types.InlineKeyboardButton(text='Мода та стиль', callback_data='key10_modaistil')
keyboard_osnownikategorii.add(key10_modaistil)
key11_hobbiotdihisport = types.InlineKeyboardButton(text='Хоббі відпочинок та спорт',callback_data='key11_hobbiotdihisport')
keyboard_osnownikategorii.add(key11_hobbiotdihisport)
key12_otdamdarom = types.InlineKeyboardButton(text='Віддам даром', callback_data='key12_otdamdarom')
keyboard_osnownikategorii.add(key12_otdamdarom)
key13_obminiay = types.InlineKeyboardButton(text='Обміняю', callback_data='key13_obminiay')
keyboard_osnownikategorii.add(key13_obminiay)







keyboard_nextcategorii_detskiymir = types.InlineKeyboardMarkup()
key1_1_vserubrikidetskimir = types.InlineKeyboardButton(text='Всі рубрики дитячий світ',callback_data='key1_1_vserubrikidetskimir')
keyboard_nextcategorii_detskiymir.add(key1_1_vserubrikidetskimir)
key1_2_detskiyodiag = types.InlineKeyboardButton(text='Дитячий одяг',callback_data='key1_2_detskiyodiag')
keyboard_nextcategorii_detskiymir.add(key1_2_detskiyodiag)
key1_3_litachevzutia = types.InlineKeyboardButton(text='Дитяче взуття',callback_data='key1_3_litachevzutia')
keyboard_nextcategorii_detskiymir.add(key1_3_litachevzutia)
key1_4_ditiachikoliaski = types.InlineKeyboardButton(text='Дитячі коляски',callback_data='key1_4_ditiachikoliaski')
keyboard_nextcategorii_detskiymir.add(key1_4_ditiachikoliaski)
key1_5_ditiachimebli = types.InlineKeyboardButton(text='Дитячі меблі',callback_data='key1_5_ditiachimebli')
keyboard_nextcategorii_detskiymir.add(key1_5_ditiachimebli)
key1_6_igrashki = types.InlineKeyboardButton(text='Іграшки',callback_data='key1_6_igrashki')
keyboard_nextcategorii_detskiymir.add(key1_6_igrashki)
key1_7_ditiachiitransport = types.InlineKeyboardButton(text='Дитячий транспорт',callback_data='key1_7_ditiachiitransport')
keyboard_nextcategorii_detskiymir.add(key1_7_ditiachiitransport)
key1_8_ditiachaida = types.InlineKeyboardButton(text='Дитяча їжа',callback_data='key1_8_ditiachaida')
keyboard_nextcategorii_detskiymir.add(key1_8_ditiachaida)
key1_9_tovaridliashkolnikiv = types.InlineKeyboardButton(text='Товари для школярів',callback_data='key1_9_tovaridliashkolnikiv')
keyboard_nextcategorii_detskiymir.add(key1_9_tovaridliashkolnikiv)
key1_10_inshiditiachitovari = types.InlineKeyboardButton(text='Інші дитячі товари',callback_data='key1_10_inshiditiachitovari')
keyboard_nextcategorii_detskiymir.add(key1_10_inshiditiachitovari)





keyboard_nextcategorii_neruhomist = types.InlineKeyboardMarkup()
key2_1_vserubrikidenedwizhimost = types.InlineKeyboardButton(text='Все в рубриці нерухомість',callback_data='key2_1_vserubrikidenedwizhimost')
keyboard_nextcategorii_neruhomist.add(key2_1_vserubrikidenedwizhimost)
key2_2_kvartirikomnaty = types.InlineKeyboardButton(text='Квартири, кімнати',callback_data='key2_2_kvartirikomnaty')
keyboard_nextcategorii_neruhomist.add(key2_2_kvartirikomnaty)
key2_3_budinki = types.InlineKeyboardButton(text='Будинки',callback_data='key2_3_budinki')
keyboard_nextcategorii_neruhomist.add(key2_3_budinki)
key2_4_zemlia = types.InlineKeyboardButton(text='Земля',callback_data='key2_4_zemlia')
keyboard_nextcategorii_neruhomist.add(key2_4_zemlia)
key2_5_kommerceneruhomist = types.InlineKeyboardButton(text='Комерційна нерухомімть',callback_data='key2_5_kommerceneruhomist')
keyboard_nextcategorii_neruhomist.add(key2_5_kommerceneruhomist)
key2_6_garazhiparkowki = types.InlineKeyboardButton(text='Гаражі, парковки',callback_data='key2_6_garazhiparkowki')
keyboard_nextcategorii_neruhomist.add(key2_6_garazhiparkowki)
key2_7_posurorendajhitla = types.InlineKeyboardButton(text='Подобова оренда житла',callback_data='key2_7_posurorendajhitla')
keyboard_nextcategorii_neruhomist.add(key2_7_posurorendajhitla)
key2_8_propozividzabudovnika = types.InlineKeyboardButton(text='Пропозиції від забудовника',callback_data='key2_8_propozividzabudovnika')
keyboard_nextcategorii_neruhomist.add(key2_8_propozividzabudovnika)
key2_9_neruhomistzakordonom = types.InlineKeyboardButton(text='Нерухомість за кордоном',callback_data='key2_9_neruhomistzakordonom')
keyboard_nextcategorii_neruhomist.add(key2_9_neruhomistzakordonom)










keyboard_nextcategorii_transport = types.InlineKeyboardMarkup()
key3_1_vsevrubrizi = types.InlineKeyboardButton(text='Все в рубриці транспорт',callback_data='key3_1_vsevrubrizi')
keyboard_nextcategorii_transport.add(key3_1_vsevrubrizi)
key3_2_lehkoviavto = types.InlineKeyboardButton(text='Легкові автомобілі',callback_data='key3_2_lehkoviavto')
keyboard_nextcategorii_transport.add(key3_2_lehkoviavto)
key3_3_avtoizpolshi = types.InlineKeyboardButton(text='Автомобілі з Польші',callback_data='key3_3_avtoizpolshi')
keyboard_nextcategorii_transport.add(key3_3_avtoizpolshi)
key3_4_gruzoviavto = types.InlineKeyboardButton(text='Грузові автомобілі',callback_data='key3_4_gruzoviavto')
keyboard_nextcategorii_transport.add(key3_4_gruzoviavto)
key3_5_gruzavtoizpolsha = types.InlineKeyboardButton(text='Грузові автомобілі з Польщі',callback_data='key3_5_gruzavtoizpolsha')
keyboard_nextcategorii_transport.add(key3_5_gruzavtoizpolsha)
key3_6_avtobusi = types.InlineKeyboardButton(text='Автобуси',callback_data='key3_6_avtobusi')
keyboard_nextcategorii_transport.add(key3_6_avtobusi)
key3_7_motozikli = types.InlineKeyboardButton(text='Мотоцикли',callback_data='key3_7_motozikli')
keyboard_nextcategorii_transport.add(key3_7_motozikli)
key3_8_speztehnika = types.InlineKeyboardButton(text='Спецтехніка',callback_data='key3_8_speztehnika')
keyboard_nextcategorii_transport.add(key3_8_speztehnika)
key3_9_silhoztehnika = types.InlineKeyboardButton(text='Сіль-хоз техніка',callback_data='key3_9_silhoztehnika')
keyboard_nextcategorii_transport.add(key3_9_silhoztehnika)
key3_10_vodnitransport = types.InlineKeyboardButton(text='Водний транспорт',callback_data='key3_10_vodnitransport')
keyboard_nextcategorii_transport.add(key3_10_vodnitransport)
key3_11_vozdushnitransport = types.InlineKeyboardButton(text='Повітряний транспорт',callback_data='key3_11_vozdushnitransport')
keyboard_nextcategorii_transport.add(key3_11_vozdushnitransport)
key3_12_prizepybudinkinakoleash = types.InlineKeyboardButton(text='Прицепи, будинки на колесах',callback_data='key3_12_prizepybudinkinakoleash')
keyboard_nextcategorii_transport.add(key3_12_prizepybudinkinakoleash)
key3_13_inshiitransport = types.InlineKeyboardButton(text='Інщий транспорт',callback_data='key3_13_inshiitransport')
keyboard_nextcategorii_transport.add(key3_13_inshiitransport)







keyboard_nextcategorii_avtozapchasti = types.InlineKeyboardMarkup()
key4_1_vsevrubrizi_avtozapchasti = types.InlineKeyboardButton(text='Все в рубриці автозапчастини',callback_data='key4_1_vsevrubrizi_avtozapchasti')
keyboard_nextcategorii_avtozapchasti.add(key4_1_vsevrubrizi_avtozapchasti)
key4_2_avtozapchastitaaksesuari = types.InlineKeyboardButton(text='Автозапчастини та аксесуари',callback_data='key4_2_avtozapchastitaaksesuari')
keyboard_nextcategorii_avtozapchasti.add(key4_2_avtozapchastitaaksesuari)
key4_3_shinidiskikolesa = types.InlineKeyboardButton(text='Шини, диски та колеса',callback_data='key4_3_shinidiskikolesa')
keyboard_nextcategorii_avtozapchasti.add(key4_3_shinidiskikolesa)
key4_4_zapchstsilhoztexnika = types.InlineKeyboardButton(text='Запчастини для сільхоз-техніки',callback_data='key4_4_zapchstsilhoztexnika')
keyboard_nextcategorii_avtozapchasti.add(key4_4_zapchstsilhoztexnika)
key4_5_motozapchasti = types.InlineKeyboardButton(text='Мото запчастини',callback_data='key4_5_motozapchasti')
keyboard_nextcategorii_avtozapchasti.add(key4_5_motozapchasti)
key4_6_inshizapchasti = types.InlineKeyboardButton(text='Інші запчастини',callback_data='key4_6_inshizapchasti')
keyboard_nextcategorii_avtozapchasti.add(key4_6_inshizapchasti)










keyboard_nextcategorii_robota = types.InlineKeyboardMarkup()
key5_1_vsevrubrikerabota = types.InlineKeyboardButton(text='Все в рубриці робота',callback_data='key5_1_vsevrubrikerabota')
keyboard_nextcategorii_robota.add(key5_1_vsevrubrikerabota)
key5_2_rozdribnatorgivla = types.InlineKeyboardButton(text='Роздрібна торгівля',callback_data='key5_2_rozdribnatorgivla')
keyboard_nextcategorii_robota.add(key5_2_rozdribnatorgivla)
key5_3_transportlogistika = types.InlineKeyboardButton(text='Транспорт, логістика',callback_data='key5_3_transportlogistika')
keyboard_nextcategorii_robota.add(key5_3_transportlogistika)
key5_4_budivniztvo = types.InlineKeyboardButton(text='Будівництво',callback_data='key5_4_budivniztvo')
keyboard_nextcategorii_robota.add(key5_4_budivniztvo)
key5_5_telekomunikazii = types.InlineKeyboardButton(text='Телекомунікації',callback_data='key5_5_telekomunikazii')
keyboard_nextcategorii_robota.add(key5_5_telekomunikazii)
key5_6_barirestorani = types.InlineKeyboardButton(text='Бари, ресторани',callback_data='key5_6_barirestorani')
keyboard_nextcategorii_robota.add(key5_6_barirestorani)
key5_7_jurispridentsiyaibuhalteria = types.InlineKeyboardButton(text='Юрисприденція та бухгалтерія',callback_data='key5_7_jurispridentsiyaibuhalteria')
keyboard_nextcategorii_robota.add(key5_7_jurispridentsiyaibuhalteria)
key5_8_upravlinnapersonalom = types.InlineKeyboardButton(text='Управління персоналом HR',callback_data='key5_8_upravlinnapersonalom')
keyboard_nextcategorii_robota.add(key5_8_upravlinnapersonalom)
key5_9_ohoronabezpeka = types.InlineKeyboardButton(text='Охорона, безпека',callback_data='key5_9_ohoronabezpeka')
keyboard_nextcategorii_robota.add(key5_9_ohoronabezpeka)
key5_10_domashniypersonal = types.InlineKeyboardButton(text='Домашній персонал',callback_data='key5_10_domashniypersonal')
keyboard_nextcategorii_robota.add(key5_10_domashniypersonal)
key5_11_krasafitnessport = types.InlineKeyboardButton(text='Краса, фітнес, спорт',callback_data='key5_11_krasafitnessport')
keyboard_nextcategorii_robota.add(key5_11_krasafitnessport)
key5_12_turizmvidpochinokrozvagy = types.InlineKeyboardButton(text='Туризм, відпочинок, розваги',callback_data='key5_12_turizmvidpochinokrozvagy')
keyboard_nextcategorii_robota.add(key5_12_turizmvidpochinokrozvagy)
key5_13_navchanya = types.InlineKeyboardButton(text='Навчання',callback_data='key5_13_navchanya')
keyboard_nextcategorii_robota.add(key5_13_navchanya)
key5_14_kulturamisteztvo = types.InlineKeyboardButton(text='Культура, мистецтво',callback_data='key5_14_kulturamisteztvo')
keyboard_nextcategorii_robota.add(key5_14_kulturamisteztvo)
key5_15_medichinafarmakologia = types.InlineKeyboardButton(text='Медицина, фармакологія',callback_data='key5_15_medichinafarmakologia')
keyboard_nextcategorii_robota.add(key5_15_medichinafarmakologia)
key5_16_itsphera = types.InlineKeyboardButton(text='IT сфера',callback_data='key5_16_itsphera')
keyboard_nextcategorii_robota.add(key5_16_itsphera)
key5_17_bankifinansy = types.InlineKeyboardButton(text='Банки, фінанси',callback_data='key5_17_bankifinansy')
keyboard_nextcategorii_robota.add(key5_17_bankifinansy)
key5_18_neruhomist = types.InlineKeyboardButton(text='Нерухомість',callback_data='key5_18_neruhomist')
keyboard_nextcategorii_robota.add(key5_18_neruhomist)
key5_19_marketingdisainreklama = types.InlineKeyboardButton(text='Маркетинг, реклама, дизайн',callback_data='key5_19_marketingdisainreklama')
keyboard_nextcategorii_robota.add(key5_19_marketingdisainreklama)
key5_20_virobniztvoenergetika = types.InlineKeyboardButton(text='Виробництво, енергетика',callback_data='key5_20_virobniztvoenergetika')
keyboard_nextcategorii_robota.add(key5_20_virobniztvoenergetika)
key5_21_agrobiznes = types.InlineKeyboardButton(text='Агро бізнес',callback_data='key5_21_agrobiznes')
keyboard_nextcategorii_robota.add(key5_21_agrobiznes)
key5_22_chastkovazainatist = types.InlineKeyboardButton(text='Часткова зайнятість',callback_data='key5_22_chastkovazainatist')
keyboard_nextcategorii_robota.add(key5_22_chastkovazainatist)
key5_23_dlyastudentiv = types.InlineKeyboardButton(text='Для студентів',callback_data='key5_23_dlyastudentiv')
keyboard_nextcategorii_robota.add(key5_23_dlyastudentiv)










