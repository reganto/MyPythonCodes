# -*- coding: utf-8 -*-
import os
import telebot
from telebot import types
from models import User


bot = telebot.TeleBot(os.environ.get('LU_BOT_TOKEN'))
ADMIN_CHAT_ID = os.environ.get('ADMIN_CHAT_ID')


def main_menu(message):
    try:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        markup.row('دانشجو', 'استاد', 'منابع', 'چارت')
        markup.row('درباره', 'خاطره', 'فرصت شغلی', 'سوال')
        markup.row('امنیت', 'سامانه ها')
        markup.row('بستن منو')

        bot.send_message(
            message.chat.id,
            'از منو انتخاب کنید',
            reply_markup=markup
        )
    except Exception as e:
        bot.send_message(message.chat.id, 'متاسفانه مشکلی پیش اومده.لطفا این مشکل رو به توسعه دهنده اطلاع بدید')


@bot.message_handler(commands=['start'])
def show_main_menu(message):
    try:

        # save new users
        query = User.select().where(User.chat_id==message.chat.id)

        flag = True
        for u in query:
            if str(message.chat.id) == str(u.chat_id):
                flag = False
        if flag:
            if message.chat.username == None:
                message.chat.username = 'unknown'
            record = User(
                chat_id=message.chat.id,
                username=message.chat.username
            )
            record.save()

        main_menu(message)
    except Exception as e:
        bot.send_message(message.chat.id, 'متاسفانه مشکلی پیش اومده.لطفا این مشکل رو به توسعه دهنده اطلاع بدید')
        

# *********************************************** chart
@bot.message_handler(func= lambda message: message.text != None and message.text=='چارت' )
def show_chart(message):
    bot.send_message(
        message.chat.id,
        'اینم چارت گروه',
    )
    bot.send_photo(
        message.chat.id,
        'http://bayanbox.ir/download/5969340884174825489/chart.jpg'
    )
    show_main_menu(message)

# ********************************************* resources
def show_terms_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.row('ترم چهار', 'ترم سه', 'ترم دو', 'ترم یک')
    markup.row('ترم هشت', 'ترم هفت', 'ترم شش', 'ترم پنج')
    markup.row('بازگشت')

    msg = bot.reply_to(message, 'ترم مورد نظر خود را انتخاب کنید', reply_markup=markup)
    return msg


def term_aval(message):
    try:
        chat_id = message.chat.id
        
        if message.text == 'مبانی کامپیوتر و برنامه نویسی':
            
            inline_markup = types.InlineKeyboardMarkup(row_width=2)
            btn1 = types.InlineKeyboardButton('نسخه اصلی', 'shorturl.at/bhAFH')
            btn2 = types.InlineKeyboardButton('نسخه فارسی', 'shorturl.at/szINS')
            inline_markup.add(btn1, btn2)

            msg = '''
                برای ترم اول و درس برنامه نویسی معمولا کتاب "سی پلاس پلاس جعفرنژاد قمی" معرفی می شود اما برای یادگیری بهتر کتاب " دیتل اند دیتل" توصیه می شود.نسخه ی فارسی این کتاب کامل نیست!
            '''
            
            bot.send_message(
                chat_id,
                msg,
                reply_markup=inline_markup
            )
            
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.row('مبانی کامپیوتر و برنامه نویسی')
            markup.row('بازگشت')
            msg = bot.reply_to(message, 'درس مورد نظر را انتخاب کنید')
            bot.register_next_step_handler(msg, term_aval)
        elif message.text == 'بازگشت':
            resources(message)
        else:
            msg = bot.reply_to(message, 'یک گزینه درست انتخاب کنید')
            bot.register_next_step_handler(msg, term_aval)
    except Exception as e:
        bot.send_message(chat_id, 'متاسفانه مشکلی پیش اومده.لطفا این مشکل رو به توسعه دهنده اطلاع بدید{}'.format(e))


def term_do(message):
    try:
        chat_id = message.chat.id

        if message.text == 'برنامه سازی پیشرفته':

            inline_markup = types.InlineKeyboardMarkup(row_width=2)
            btn1 = types.InlineKeyboardButton('نسخه اصلی Epub', 'shorturl.at/epsD7')
            btn2 = types.InlineKeyboardButton('راهنمای باز کردن فایل', 'shorturl.at/fgiFS')
            inline_markup.add(btn2, btn1)

            msg = '''
                    برای این درس کتاب "برنامه نویسی به زبان جاوا"آقای جعفرنژاد قمی معرفی می شود ولی برای یادگیری بهتر کتاب "دیتل اند دیتل" توصیه می شود
            '''
            bot.send_message(
                chat_id,
                msg,
                reply_markup=inline_markup
            )

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.row('برنامه سازی پیشرفته')
            markup.row('بازگشت')
            msg = bot.reply_to(message, 'درس مورد نظر را انتخاب کنید')
            bot.register_next_step_handler(msg, term_aval)
        elif message.text == 'بازگشت':
            resources(message)
        else:
            msg = bot.reply_to(message, 'یک گزینه درست انتخاب کنید')
            bot.register_next_step_handler(msg, term_aval)
    except Exception as e:
        bot.send_message(chat_id, 'متاسفانه مشکلی پیش اومده.لطفا این مشکل رو به توسعه دهنده اطلاع بدید')


def term_se(message):
    try:
        chat_id = message.chat.id

        bot.send_message(chat_id, 'در تکمیل منابع کمک کنید')
        if message.text == 'بازگشت':
            resources(message)
    except Exception as e:
        bot.send_message(chat_id, 'متاسفانه مشکلی پیش اومده.لطفا این مشکل رو به توسعه دهنده اطلاع بدید')


def term_char(message):
    try:
        chat_id = message.chat.id

        bot.send_message(chat_id, 'در تکمیل منابع کمک کنید')
        if message.text == 'بازگشت':
            resources(message)
    except Exception as e:
        bot.send_message(chat_id, 'متاسفانه مشکلی پیش اومده.لطفا این مشکل رو به توسعه دهنده اطلاع بدید')


def term_panj(message):
    try:
        chat_id = message.chat.id

        bot.send_message(chat_id, 'در تکمیل منابع کمک کنید')
        if message.text == 'بازگشت':
            resources(message)
    except Exception as e:
        bot.send_message(chat_id, 'متاسفانه مشکلی پیش اومده.لطفا این مشکل رو به توسعه دهنده اطلاع بدید')


def term_shesh(message):
    try:
        chat_id = message.chat.id

        bot.send_message(chat_id, 'در تکمیل منابع کمک کنید')
        if message.text == 'بازگشت':
            resources(message)
    except Exception as e:
        bot.send_message(chat_id, 'متاسفانه مشکلی پیش اومده.لطفا این مشکل رو به توسعه دهنده اطلاع بدید')



def term_haft(message):
    try:
        chat_id = message.chat.id

        bot.send_message(chat_id, 'در تکمیل منابع کمک کنید')
        if message.text == 'بازگشت':
            resources(message)
    except Exception as e:
        bot.send_message(chat_id, 'متاسفانه مشکلی پیش اومده.لطفا این مشکل رو به توسعه دهنده اطلاع بدید')
    


def term_hasht(message):
    try:
        chat_id = message.chat.id

        bot.send_message(chat_id, 'در تکمیل منابع کمک کنید')
        if message.text == 'بازگشت':
            resources(message)
    except Exception as e:
        bot.send_message(chat_id, 'متاسفانه مشکلی پیش اومده.لطفا این مشکل رو به توسعه دهنده اطلاع بدید')
    
    
def term_dispatcher(message):
    try:
        chat_id = message.chat.id
        term = message.text

        if term == 'ترم یک':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.row('مبانی کامپیوتر و برنامه نویسی')
            markup.row('بازگشت')
            msg = bot.reply_to(message, 'درس مورد نظر را انتخاب کنید', reply_markup=markup)
            bot.register_next_step_handler(msg, term_aval)
        elif term == 'ترم دو':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.row('برنامه سازی پیشرفته')
            markup.row('بازگشت')
            msg = bot.reply_to(message, 'درس مورد نظر را انتخاب کنید', reply_markup=markup)
            bot.register_next_step_handler(msg, term_do)
        elif term == 'ترم سه':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.row('بازگشت')
            msg = bot.reply_to(message, 'درس مورد نظر را انتخاب کنید', reply_markup=markup)
            bot.register_next_step_handler(msg, term_se)
        elif term == 'ترم چهار':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.row('بازگشت')
            msg = bot.reply_to(message, 'درس مورد نظر را انتخاب کنید', reply_markup=markup)
            bot.register_next_step_handler(msg, term_char)
        elif term == 'ترم پنج':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.row('Not implemented yet ;)')
            markup.row('بازگشت')
            msg = bot.reply_to(message, 'درس مورد نظر را انتخاب کنید', reply_markup=markup)
            bot.register_next_step_handler(msg, term_panj)
        elif term == 'ترم شش':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.row('بازگشت')
            msg = bot.reply_to(message, 'درس مورد نظر را انتخاب کنید', reply_markup=markup)
            bot.register_next_step_handler(msg, term_shesh)
        elif term == 'ترم هفت':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.row('بازگشت')
            msg = bot.reply_to(message, 'درس مورد نظر را انتخاب کنید', reply_markup=markup)
            bot.register_next_step_handler(msg, term_haft)
        elif term == 'ترم هشت':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.row('بازگشت')
            msg = bot.reply_to(message, 'درس مورد نظر را انتخاب کنید', reply_markup=markup)
            bot.register_next_step_handler(msg, term_hasht)
        elif term == 'بازگشت':
            show_main_menu(message)
        else:
            msg = bot.reply_to(message, 'یک گزینه درست انتخاب کنید')
            bot.register_next_step_handler(msg, term_dispatcher)
    except Exception as e:
        bot.send_message(chat_id, 'متاسفانه مشکلی پیش اومده.لطفا این مشکل رو به توسعه دهنده اطلاع بدید')


@bot.message_handler(func= lambda message: message.text is not None and message.text=='منابع')
def resources(message):
    msg = show_terms_menu(message)
    bot.register_next_step_handler(msg, term_dispatcher)

# *********************************************************************************


# ********************************************** broadcast
def retrive_all_users():
    query = User.select(User.chat_id)
    result = (u.chat_id for u in query)
    return result


def broadcast_msg(message):
    gen = retrive_all_users()
    try:
        while True:
            cid = next(gen)
            if cid == ADMIN_CHAT_ID:
                pass
            else:
                bot.send_message(
                    cid,
                    '''
                    پیام : 
                    \n
                    '''+message.text
                )
    except Exception as e:
        bot.send_message(message.chat.id, 'end')
    


@bot.message_handler(commands=['broadcast'])
def echo_broadcast_msg(message):
    if message.chat.id == 447010443:
        msg = bot.reply_to(message, 'write message')
        bot.register_next_step_handler(msg, broadcast_msg)
    else:
        bot.send_message(message.chat.id, 'Access denied')
# *******************************************************************


# ***************************************************************************** samaneha

@bot.message_handler(func=lambda message: message.text is not None and message.text=='سامانه ها')
def samaneha(message):
    chat_id = message.chat.id

    markup = types.InlineKeyboardMarkup(row_width=3)
    btn1 = types.InlineKeyboardButton('سامانه سجاد', 'https://portal.saorg.ir/')
    btn2 = types.InlineKeyboardButton('اتوماسیون تغذیه', 'http://nd.lu.ac.ir/')
    btn3 = types.InlineKeyboardButton('سیستم گلستان', 'https://golestan.lu.ac.ir/Forms/AuthenticateUser/main.htm')
    markup.add(btn1, btn2, btn3)

    bot.send_message(
        chat_id,
        'سیستم های مورد نیاز',
        reply_markup=markup
    )
    show_main_menu(message)
# **********************************************************************************


# ******************************************************************************* security

def security(message):
    chat_id = message.chat.id
    content = message.text
    try:
        if content == 'مشاهده':
            user = User.select().where(User.chat_id==chat_id).get()
            if user.username == 'unknown':
                user.username = None
            bot.send_message(
                chat_id,
                '''
                Telegram unique id: {}
                \n
                Username: {}
                '''.format(user.chat_id, user.username)
            )
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('پاک کردن')
            btn2 = types.KeyboardButton('مشاهده')
            btn3 = types.KeyboardButton('بازگشت')
            markup.row(btn1, btn2)
            markup.row(btn3)
            msg = bot.reply_to(message, 'انتخاب کنید', reply_markup=markup)
            bot.register_next_step_handler(msg, security)
        elif content == 'پاک کردن':
            user = User.select().where(User.chat_id==chat_id).get()
            status = user.delete_instance()
            if status == 1:
                bot.send_message(
                    chat_id,
                    '''
                    اطلاعات شماپاک شد.برای شروع دوباره از دستور /start استفاده کنید
                    '''
                )
            else:
                bot.send_message(
                    chat_id,
                    '''
                    خطا! اطلاعات شما پاک نشد. با توسعه دهنده تماس بگیرید
                    '''
                )
        elif content == 'بازگشت':
            show_main_menu(message)
        else:
            bot.send_message(
                chat_id,
                'یک گزینه درست انتخاب کنید'
            )
    except Exception as e:
        bot.send_message(chat_id, 'متاسفانه مشکلی پیش اومده.لطفا این مشکل رو به توسعه دهنده اطلاع بدید')


@bot.message_handler(func=lambda message: message.text is not None and message.text=='امنیت')
def echo_security(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('پاک کردن')
    btn2 = types.KeyboardButton('مشاهده')
    btn3 = types.KeyboardButton('بازگشت')
    markup.row(btn1, btn2)
    markup.row(btn3)

    msg = bot.reply_to(
        message, 
        '''
        با شروع کار با ربات،‌اطلاعاتی از شما در دیتا بیس ربات ذخیره می شود. چنانچه مایل به مشاهده ی اطلاعات دخیره شده یا حذف آن ها هستید، از منوی زیر انتخاب کنید
        ''',
        reply_markup=markup
    )
    bot.register_next_step_handler(msg, security)

bot.polling()
