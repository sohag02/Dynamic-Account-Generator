from time import sleep
import os

from pyrate_limiter import (BucketFullException, Duration, Limiter,
                            MemoryListBucket, MemoryQueueBucket, RequestRate)
from telegram import (InlineKeyboardButton, InlineKeyboardMarkup,
                      ReplyKeyboardMarkup, replymarkup)
from telegram.ext import (CallbackContext, CallbackQueryHandler,
                          CommandHandler, ConversationHandler, Filters,
                          InlineQueryHandler, MessageHandler, TypeHandler,
                          Updater, dispatcher, filters)
from telegram.ext.dispatcher import DispatcherHandlerStop


TOKEN = "1692696716:AAEiNle1ZjBkOLiJKbjuJqYxD5QyNAxbG80"
PORT = int(os.environ('PORT','8443'))

channel = -1001206083299
channel_username = "@Sohag_t"
ch_link = "t.me/DynamicBots"

admins = ['Sohag02','AnuragZ','Jabed02','TheDynamicOwner','Devi_l007']

limit_per_day = 2


def limit(user):
    rate = RequestRate(2, Duration.DAY)
    limiter = Limiter(rate, bucket_class=MemoryListBucket)

    identity = user
    try:
        limiter.try_acquire(identity)
        return True
    except BucketFullException as err:
        return False
        

def start(update, context):
    user_id = update.message.from_user.id
    check_id = str(user_id)
    file = open("user_list.txt", "r")
    user_list = file.readlines()
    user_list = ''.join(user_list).replace(r'\n',"").split()
    print(user_list)
    if check_id in user_list:
        pass
        print("a")
        file.close()
    else:
        file = open("user_list.txt", "a")
        file.write("\n")
        file.write(str(user_id))
        print("b")

    check = context.bot.get_chat_member(channel, user_id = update.message.from_user.id) #1048643192
    if check.status in ['administrator','creator','member']:
        update.message.reply_text("𝗛𝗲𝗹𝗹𝗼 @{username},\n"
                                "➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                "This bot can provide premium accounts of different services\n"
                                "➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                "𝗨𝘀𝗲 /accounts to Get Accounts\n" 
                                "➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                "✅𝗖𝗥𝗘𝗗𝗜𝗧𝗦:- @DynamicBots\n"
                                "➖➖➖➖➖➖➖➖➖➖➖➖\n".format(username = update.effective_user.username))
    else:
        keyboard = [[InlineKeyboardButton("JOIN HERE✅", url=ch_link),]]
        r = InlineKeyboardMarkup(keyboard)
        update.message.reply_text("TO ACCESS THIS BOT IN ORDER TO CLAIM FREE ACCOUNTS DAILY YOU NEED TO JOIN THE BELOW CHANNEL!",
                                    reply_markup=r)


def upload(update, context):
            if context.args[0] == "zee5":           
                file = open("hits\\zee5.txt", "a")
                hit_list = context.args 
                r = hit_list[0]
                hit_list.remove(r)
                print(hit_list)
                for x in hit_list:
                    file.write(x)
                    file.write("\n")
                file.close()
                update.message.reply_text("Zee5 Upload SUCCESSFULL!")

            elif context.args[0] == "nord":
                file = open("hits\\nordvpn.txt", "a")
                hit_list = context.args
                r = hit_list[0]
                hit_list.remove(r)
                print(hit_list)
                for x in hit_list:
                    file.write(x)
                    file.write("\n")
                file.close()
                update.message.reply_text("Nord VPN Upload SUCCESSFULL!")

            elif context.args[0] == "voot":
                file = open("hits\\voot.txt", "a")
                hit_list = context.args
                r = hit_list[0]
                hit_list.remove(r)
                print(hit_list)
                for x in hit_list:
                    file.write(x)
                    file.write("\n")
                file.close()
                update.message.reply_text("Voot Upload SUCCESSFULL!")

            elif context.args[0] == "ipvanish":
                file = open("hits\\ipvanish.txt", "a")
                hit_list = context.args
                r = hit_list[0]
                hit_list.remove(r)
                print(hit_list)
                for x in hit_list:
                    file.write(x)
                    file.write("\n")
                file.close()
                update.message.reply_text("IPvanish Upload SUCCESSFULL!")

            elif context.args[0] == "uplay":
                file = open("hits\\uplay.txt", "a")
                hit_list = context.args
                r = hit_list[0]
                hit_list.remove(r)
                print(hit_list)
                for x in hit_list:
                    file.write(x)
                    file.write("\n")
                file.close()
                update.message.reply_text("Uplay Upload SUCCESSFULL!")

            elif context.args[0] == "altbalaji":
                file = open("hits\\altbalaji.txt", "a")
                hit_list = context.args
                r = hit_list[0]
                hit_list.remove(r)
                print(hit_list)
                for x in hit_list:
                    file.write(x)
                    file.write("\n")
                file.close()
                update.message.reply_text("Altbalaji Upload SUCCESSFULL!")

            elif context.args[0] == "hulu":
                file = open("hits\\hulu.txt", "a")
                hit_list = context.args
                r = hit_list[0]
                hit_list.remove(r)
                print(hit_list)
                for x in hit_list:
                    file.write(x)
                    file.write("\n")
                file.close()
                update.message.reply_text("Hulu Upload SUCCESSFULL!")

            elif context.args[0] == "wwe":
                file = open("hits\\wwe.txt", "a")
                hit_list = context.args
                r = hit_list[0]
                hit_list.remove(r)
                print(hit_list)
                for x in hit_list:
                    file.write(x)
                    file.write("\n")
                file.close()
                update.message.reply_text("WWE Upload SUCCESSFULL!")

            elif context.args[0] == "crunchyroll":
                file = open("hits\\crunchyroll.txt", "a")
                hit_list = context.args
                r = hit_list[0]
                hit_list.remove(r)
                for x in hit_list:
                    file.write(x)
                    file.write("\n")
                file.close()
                update.message.reply_text("Crunchyroll Upload SUCCESSFULL!")

            else:
                update.message.reply_text("UPLOAD UNSUCCESFULL\n"
                                        "Please specify service name\n"
                                        "Format: /upload <service> <hits>")


def stats(update, context):
    try:
        s = context.args[0]
        if context.args[0] == "zee5":
            file = open(f"hits\\{s}.txt", "r")
            l = file.readlines()
            a = len(l)
            update.message.reply_text("ZEE5 STATS\n\nAccounts Remainning : {a}".format(a=a))
        elif context.args[0] == "nord":
            file = open(f"hits\\{s}.txt", "r")
            l = file.readlines()
            a = len(l)
            update.message.reply_text("NORD VPN STATS\n\nAccounts Remainning : {a}".format(a=a))
        elif context.args[0] == "voot":
            file = open(f"hits\\{s}.txt", "r")
            l = file.readlines()
            a = len(l)
            update.message.reply_text("VOOT STATS\n\nAccounts Remainning : {a}".format(a=a))
        elif context.args[0] == "ipvanish":
            file = open(f"hits\\{s}.txt", "r")
            l = file.readlines()
            a = len(l)
            update.message.reply_text("IPVANISH VPN STATS\n\nAccounts Remainning : {a}".format(a=a))
        elif context.args[0] == "uplay":   
            file = open(f"hits\\{s}.txt", "r")
            l = file.readlines()
            a = len(l)  
            update.message.reply_text("UPLAY STATS\n\nAccounts Remainning : {a}".format(a=a))
        elif context.args[0] == "altbalaji": 
            file = open(f"hits\\{s}.txt", "r")
            l = file.readlines()
            a = len(l)       
            update.message.reply_text("ALTBALAJI STATS\n\nAccounts Remainning : {a}".format(a=a))
        elif context.args[0] == "hulu": 
            file = open(f"hits\\{s}.txt", "r")
            l = file.readlines()
            a = len(l)       
            update.message.reply_text("HULU STATS\n\nAccounts Remainning : {a}".format(a=a))
        elif context.args[0] == "wwe":  
            file = open(f"hits\\{s}.txt", "r")
            l = file.readlines()
            a = len(l)      
            update.message.reply_text("WWE STATS\n\nAccounts Remainning : {a}".format(a=a))
        elif context.args[0] == "crunchyroll": 
            file = open(f"hits\\{s}.txt", "r")
            l = file.readlines()
            a = len(l)       
            update.message.reply_text("CRUNCHYROLL STATS\n\nAccounts Remainning : {a}".format(a=a))
    except:
        zee5_len = len(open("hits\\zee5.txt", "r").readlines())
        nord_len = len(open("hits\\nordvpn.txt", "r").readlines())
        voot_len = len(open("hits\\voot.txt", "r").readlines())
        ipvanish_len = len(open("hits\\ipvanish.txt", "r").readlines())
        uplay_len = len(open("hits\\uplay.txt", "r").readlines())
        altbalaji_len = len(open("hits\\altbalaji.txt", "r").readlines())
        hulu_len = len(open("hits\\hulu.txt", "r").readlines())
        wwe_len = len(open("hits\\wwe.txt", "r").readlines())
        crunchyroll_len = len(open("hits\\crunchyroll.txt", "r").readlines())
        total_len = sum([zee5_len, nord_len, voot_len, ipvanish_len, uplay_len, hulu_len, wwe_len, crunchyroll_len])
        update.message.reply_text("STATS\n\n"
                                    "ZEE5 : {}\n"
                                    "NORD VPN : {}\n"
                                    "VOOT : {}\n"
                                    "IPVANISH : {}\n"
                                    "UPLAY : {}\n"
                                    "ALTBALAJI : {}\n"
                                    "HULU : {}\n"
                                    "WWE : {}\n"
                                    "CRUNCHYROLL : {}\n\n"
                                    "TOTAL : {}".format(zee5_len, nord_len, voot_len, ipvanish_len, uplay_len,
                                    altbalaji_len, hulu_len, wwe_len, crunchyroll_len, total_len))
        

def accounts(update, context):
    check = context.bot.get_chat_member(channel, user_id = update.message.from_user.id)
    if check.status in ['administrator','creator','member']:
        keyboard = [
            [
                InlineKeyboardButton("ZEE5", callback_data="zee5"),
                InlineKeyboardButton("NORDVPN", callback_data="nord"),
            ],
            [
                InlineKeyboardButton("VOOT", callback_data="voot"),
                InlineKeyboardButton("IPVANISH", callback_data="ipvanish"),
            ],
            [
                InlineKeyboardButton("UPLAY", callback_data="uplay"),
                InlineKeyboardButton("ALTBALAJI", callback_data="altbalaji"),
            ],
            [
                InlineKeyboardButton("HULU", callback_data="hulu"),
                InlineKeyboardButton("WWE", callback_data="wwe"),
            ],
            [
                InlineKeyboardButton("CRUNCHYROLL", callback_data="crunchyroll"),
            ],
        ]

        acc_list = InlineKeyboardMarkup(keyboard)
        update.message.reply_text("PLEASE CHOOSE WHICH ACCOUNT WOULD YOU LIKE TO GET FROM @AccountsGeneratorBot",
                                reply_markup=acc_list)
    else:
        keyboard = [[InlineKeyboardButton("JOIN HERE✅", url=ch_link),]]
        r = InlineKeyboardMarkup(keyboard)
        update.message.reply_text("TO ACCESS THIS BOT IN ORDER TO CLAIM FREE ACCOUNTS DAILY YOU NEED TO JOIN THE BELOW CHANNEL!\n"
                                    "START THE BOT AGAIN AFTER JOINNING",
                                    reply_markup=r)


def prepend(List, r):
    r += '{0}'
    List = [r.format(i) for i in List]
    List = ('\n'.join(map(str, List)))
    return(List)


def button_click(update, context):
    query = update.callback_query
    query.answer()
    p = query.data
    name = query.data.upper()

    if query.data != "Dyno" or "admin_list":
        print(1)
        l = limit(update.effective_chat.id)
        if l == True:
            print(2)
            if query.data == "zee5":
                
                    file = open(f"hits\\{p}.txt", "r+")
                    zee5_list = file.readlines()

                    if len(zee5_list) == 0:
                        query.edit_message_text(f"{p} accounts are currently Out of stock")
                    else:
                        acc = zee5_list[0]
                        print(acc)
                        split = acc.split(":")
                        print(split)
                        email = split[0]
                        print(email)
                        acc_pass = split[1]

                        query.edit_message_text("😍HERE'S YOUR REQUESTED ACCOUNT😍\n"
                                                "➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                                "👉🏻REQUESTED:- {name}\n"
                                                "👉🏻EMAIL:- {email}\n"
                                                "👉🏻PASSWORD:- {acc_pass}\n"
                                                "➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                                "❤️THANK YOU FOR USING @AccountsGeneratorBot\n"
                                                "➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                                "🔥BOT BY:- @TheDynamicNetwork🔥".format(name=name, acc_pass=acc_pass, email=email))

                        zee5_list.remove(acc)

                        file.close()
                        print(zee5_list)
                        file = open(f"hits\\{p}.txt", "w+")
                        zee5_list = ''.join(zee5_list).replace(r'\n',"").split()
                        print(zee5_list)
                        for x in zee5_list:
                            file.write(x)
                            file.write("\n")
                        file.close()
        
            elif query.data == "nord":
                file = open(f"hits\\{p}.txt", "r+")
                hit_list = file.readlines()
                if len(hit_list) == 0:
                    query.edit_message_text(f"{p} accounts are currently Out of stock")
                else:
                    acc = hit_list[0]
                    print(acc)
                    split = acc.split(":")
                    print(split)
                    email = split[0]
                    print(email)
                    acc_pass = split[1]

                    query.edit_message_text("😍HERE'S YOUR REQUESTED ACCOUNT😍\n"
                                            "➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                            "👉🏻REQUESTED:- {name}\n"
                                            "👉🏻EMAIL:- {email}\n"
                                            "👉🏻PASSWORD:- {acc_pass}\n"
                                            "➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                            "❤️THANK YOU FOR USING  @AccountsGeneratorBot\n"
                                            "➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                            "🔥 BOT BY:- @TheDynamicNetwork 🔥".format(name=name, acc_pass=acc_pass, email=email))

                    hit_list.remove(acc) 

                    file.close()
                    print(hit_list)
                    file = open(f"hits\\{p}.txt", "w+")
                    hit_list = ''.join(hit_list).replace(r'\n',"").split()
                    print(hit_list)
                    for x in hit_list:
                        file.write(x)
                        file.write("\n")
                    file.close()     

            elif query.data == "voot":
                file = open(f"hits\\{p}.txt", "r+")
                hit_list = file.readlines()
                if len(hit_list) == 0:
                    query.edit_message_text(f"{p} accounts are currently Out of stock")
                else:
                    acc = hit_list[0]
                    print(acc)
                    split = acc.split(":")
                    print(split)
                    email = split[0]
                    print(email)
                    acc_pass = split[1]

                    query.edit_message_text("😍HERE'S YOUR REQUESTED ACCOUNT😍\n"
                                            "➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                            "👉🏻REQUESTED:- {name}\n"
                                            "👉🏻EMAIL:- {email}\n"
                                            "👉PASSWORD:- {acc_pass}\n"
                                            "➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                            "❤️THANK YOU FOR USING  @AccountsGeneratorBot\n"
                                            "➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                            "🔥 BOT BY:- @TheDynamicNetwork 🔥".format(name=name, acc_pass=acc_pass, email=email))

                    hit_list.remove(acc)

                    file.close()
                    print(hit_list)
                    file = open(f"hits\\{p}.txt", "w+")
                    hit_list = ''.join(hit_list).replace(r'\n',"").split()
                    print(hit_list)
                    for x in hit_list:
                        file.write(x)
                        file.write("\n")
                    file.close()

            elif query.data == "ipvanish":
                file = open(f"hits\\{p}.txt", "r+")
                hit_list = file.readlines()
                if len(hit_list) == 0:
                    query.edit_message_text(f"{p} accounts are currently Out of stock")
                else:
                    acc = hit_list[0]
                    print(acc)
                    split = acc.split(":")
                    print(split)
                    email = split[0]
                    print(email)
                    acc_pass = split[1]

                    query.edit_message_text("😍HERE'S YOUR REQUESTED ACCOUNT😍\n"
                                            "➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                            "👉🏻REQUESTED:- {name}\n"
                                            "👉🏻EMAIL:- {email}\n"
                                            "👉🏻PASSWORD:- {acc_pass}\n"
                                            "➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                            "❤️THANK YOU FOR USING  @AccountsGeneratorBot\n"
                                            "➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                            "🔥 BOT BY:- @TheDynamicNetwork 🔥".format(name=name, acc_pass=acc_pass, email=email))

                    hit_list.remove(acc)

                    file.close()
                    print(hit_list)
                    file = open(f"hits\\{p}.txt", "w+")
                    hit_list = ''.join(hit_list).replace(r'\n',"").split()
                    print(hit_list)
                    for x in hit_list:
                        file.write(x)
                        file.write("\n")
                    file.close()

            elif query.data == "uplay":
                file = open(f"hits\\{p}.txt", "r+")
                hit_list = file.readlines()
                if len(hit_list) == 0:
                    query.edit_message_text(f"{p} accounts are currently Out of stock")
                else:
                    acc = hit_list[0]
                    print(acc)
                    split = acc.split(":")
                    print(split)
                    email = split[0]
                    print(email)
                    acc_pass = split[1]

                    query.edit_message_text("😍HERE'S YOUR REQUESTED ACCOUNT😍\n"
                                            "➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                            "👉🏻REQUESTED:- {name}\n"
                                            "👉🏻EMAIL:- {email}\n"
                                            "👉🏻PASSWORD:- {acc_pass}\n"
                                            "➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                            "❤️THANK YOU FOR USING  @AccountsGeneratorBot\n"
                                            "➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                            "🔥 BOT BY:- @TheDynamicNetwork 🔥".format(name=name, acc_pass=acc_pass, email=email))

                    hit_list.remove(acc)

                    file.close()
                    print(hit_list)
                    file = open(f"hits\\{p}.txt", "w+")
                    hit_list = ''.join(hit_list).replace(r'\n',"").split()
                    print(hit_list)
                    for x in hit_list:
                        file.write(x)
                        file.write("\n")
                    file.close()

            elif query.data == "altbalaji":
                file = open(f"hits\\{p}.txt", "r+")
                hit_list = file.readlines()
                if len(hit_list) == 0:
                    query.edit_message_text(f"{p} accounts are currently Out of stock")
                else:
                    acc = hit_list[0]
                    print(acc)
                    split = acc.split(":")
                    print(split)
                    email = split[0]
                    print(email)
                    acc_pass = split[1]

                    query.edit_message_text("😍HERE'S YOUR REQUESTED ACCOUNT😍\n"
                                            "➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                            "👉🏻REQUESTED:- {name}\n"
                                            "👉🏻EMAIL:- {email}\n"
                                            "👉🏻PASSWORD:- {acc_pass}\n"
                                            "➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                            "❤️THANK YOU FOR USING  @AccountsGeneratorBot\n"
                                            "➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                            "🔥 BOT BY:- @TheDynamicNetwork 🔥".format(name=name, acc_pass=acc_pass, email=email))

                    hit_list.remove(acc)

                    file.close()
                    print(hit_list)
                    file = open(f"hits\\{p}.txt", "w+")
                    hit_list = ''.join(hit_list).replace(r'\n',"").split()
                    print(hit_list)
                    for x in hit_list:
                        file.write(x)
                        file.write("\n")
                    file.close()

            elif query.data == "wwe":
                file = open(f"hits\\{p}.txt", "r+")
                hit_list = file.readlines()
                if len(hit_list) == 0:
                    query.edit_message_text(f"{p} accounts are currently Out of stock")
                else:
                    acc = hit_list[0]
                    print(acc)
                    split = acc.split(":")
                    print(split)
                    email = split[0]
                    print(email)
                    acc_pass = split[1]

                    query.edit_message_text("😍HERE'S YOUR REQUESTED ACCOUNT😍\n"
                                            "➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                            "👉🏻REQUESTED:- {name}\n"
                                            "👉🏻EMAIL:- {email}\n"
                                            "👉🏻PASSWORD:- {acc_pass}\n"
                                            "➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                            "❤️THANK YOU FOR USING  @AccountsGeneratorBot\n"
                                            "➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                            "🔥 BOT BY:- @TheDynamicNetwork 🔥".format(name=name, acc_pass=acc_pass, email=email))

                    hit_list.remove(acc)

                    file.close()
                    print(hit_list)
                    file = open(f"hits\\{p}.txt", "w+")
                    hit_list = ''.join(hit_list).replace(r'\n',"").split()
                    print(hit_list)
                    for x in hit_list:
                        file.write(x)
                        file.write("\n")
                    file.close()

            elif query.data == "crunchyroll":
                file = open(f"hits\\{p}.txt", "r+")
                hit_list = file.readlines()
                if len(hit_list) == 0:
                    query.edit_message_text(f"{p} accounts are currently Out of stock")
                else:
                    acc = hit_list[0]
                    print(acc)
                    split = acc.split(":")
                    print(split)
                    email = split[0]
                    print(email)
                    acc_pass = split[1]

                    query.edit_message_text("😍HERE'S YOUR REQUESTED ACCOUNT😍\n"
                                            "➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                            "👉🏻REQUESTED:- {name}\n"
                                            "👉🏻EMAIL:- {email}\n"
                                            "👉🏻PASSWORD:- {acc_pass}\n"
                                            "➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                            "❤️THANK YOU FOR USING @AccountsGeneratorBot\n"
                                            "➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                            "🔥 BOT BY:- @TheDynamicNetwork 🔥".format(name=name, acc_pass=acc_pass, email=email))

                    hit_list.remove(acc)

                    file.close()
                    print(hit_list)
                    file = open(f"hits\\{p}.txt", "w+")
                    hit_list = ''.join(hit_list).replace(r'\n',"").split()
                    print(hit_list)
                    for x in hit_list:
                        file.write(x)
                        file.write("\n")
                    file.close()
            elif query.data == "admin_list":
                a = '@'
                b = prepend(admins, a)
                query.edit_message_text(f"ADMIN LIST\n\n{b}")
                
        elif l == False:
            print(3)
            query.edit_message_text("Your Daily Limit is Over! Visit us again tomorrow for free account!"
                                    "To increase Your limit by paying Contact:- @TheDynamicOwner\n"
                                    "Limit : 2 Ac/day")


def admin(update, context):
    #file = open("admin_list.txt", "r")
    #a = file.readlines()
    #file.close()
    keyboard = [[InlineKeyboardButton("ADMIN LIST", callback_data="admin_list"),]]
    r = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("ADMIN PANEL\n\n"
                                "Total admins : {n}\n\n"
                                "Admin Commands\n\n"
                                "/stats <service> : Service stats \n"
                                "/user_stats: Total Users\n"
                                "/broadcast: Broadcast a msg to all users\n\n"
                                #"/add_admin : Add Admin\n"
                                #"/rem_admin : Remove admins\n\n"
                                "/upload <service> : Upload combos\n"
                                "/clear_db <service> : Reset database of a service\n"
                                "/clear_db : Reset Total Database".format(n=len(admins)), reply_markup=r)


def rem_admin(update, context):
    rem = context.args[0]
    r = rem.replace('@','')
    file = open("admin_list.txt", "r")
    l = file.readlines()
    file.close()
    if r in l:
        l.remove(r)
        file = open("admin_list.txt", "w")
        for x in l:
            file.write(x)
            file.write("\n")
        update.message.reply_text(f"@{rem} was removed from Admins")
    else:
        update.message.reply_text(f"@{r} couldn't be Found in Admin list")

        
def add_admin(update, context):
    print("w")
    try:
        add = context.args[0]
        Filters.user.add_usernames(username = add)
        update.message.reply_text("{r} was succesfully added".format(r=add))
        print("s")
    except:
        raise
        update.message.reply_text("{r} can't be add".format(r=add))


def message(update, context):
    check = context.bot.get_chat_member("@Sohag_t", user_id = update.message.from_user.id)
    if check.status in ['administrator','creator','member']:
        update.message.reply_text("This is not a valid command\nUse /start for guide")
    else:
        keyboard = [[InlineKeyboardButton("JOIN HERE✅", url=ch_link),]]
        r = InlineKeyboardMarkup(keyboard)
        update.message.reply_text("TO ACCESS THIS BOT IN ORDER TO CLAIM FREE ACCOUNTS DAILY YOU NEED TO JOIN THE BELOW CHANNEL!",
                                    reply_markup=r)


def non_admin(update, context):
    update.message.reply_text("Your are not an admin of This Bot")


def user_stats(update, context):
    file = open("user_list.txt", "r")
    user_list = file.readlines()
    total_users = len(user_list)
    update.message.reply_text(f"Total Users: {total_users}")


def broadcast(update, context):
    file = open("user_list.txt", "r")
    user_list = file.readlines()
    print(user_list)
    msg = context.args
    msg_str = " "
    msg_str = msg_str.join(msg)
    msg = update.message.reply_text("Sending Broadcast...")
    fails = 0
    try:
        for x in user_list:
            try:
                context.bot.send_message(chat_id= x, text=msg_str)
                sleep(0.04)
            except:
                fails += 1
        msg.edit_text(f"Broadcast Sent Successfully\nFails: {fails}\nsuccess: {len(user_list)-fails}")
    except:
        update.message.reply_text("Broadcast Failed")


def clear_db(update, context):
    try:
        s = context.args[0]
        file = open(f"hits\\{s}.txt", "w+")
        file.truncate(0)
        file.close()
    except:
        zee5 = (open("hits\\zee5.txt", "w")).truncate(0)
        nord = (open("hits\\nordvpn.txt", "w")).truncate(0)
        voot = (open("hits\\voot.txt", "w")).truncate(0)
        ipvanish = (open("hits\\ipvanish.txt", "w")).truncate(0)
        uplay = (open("hits\\uplay.txt", "w")).truncate(0)
        altbalaji = (open("hits\\altbalaji.txt", "w")).truncate(0)
        hulu = (open("hits\\hulu.txt", "w")).truncate(0)
        wwe = (open("hits\\wwe.txt", "w")).truncate(0)
        crunchyroll = (open("hits\\crunchyroll.txt", "w")).truncate(0)




updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher


dispatcher.add_handler(CommandHandler("start", start), group=1)
dispatcher.add_handler(CommandHandler("accounts", accounts), group=1)
dispatcher.add_handler(CommandHandler("upload", upload, Filters.user(username=admins)), group=1)
dispatcher.add_handler(CommandHandler("admin", admin, Filters.user(username=admins)), group=1)
dispatcher.add_handler(CallbackQueryHandler(button_click), group=1)
dispatcher.add_handler(CommandHandler("clear", clear_db, Filters.user(username=admins)), group=1)
dispatcher.add_handler(CommandHandler("rem_admin", rem_admin, Filters.user(username=admins)), group=1)
dispatcher.add_handler(CommandHandler("add_admin", add_admin, Filters.user(username=admins)), group=1)
dispatcher.add_handler(CommandHandler("broadcast", broadcast, Filters.user(username=admins)), group=1)
dispatcher.add_handler(CommandHandler("stats", stats, Filters.user(username=admins)), group=1)
dispatcher.add_handler(CommandHandler("user_stats", user_stats, Filters.user(username=admins)), group=1)
dispatcher.add_handler(CommandHandler(["stats", "upload", "admin", "broadcast"], non_admin, ~Filters.user(username=admins)), group=1)
dispatcher.add_handler(MessageHandler(Filters.all & (~ Filters.caption_entity("bot_command")), message), group=1)

updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
updater.bot.set_webhook("https://dynamic-account-generator.herokuapp.com/")
updater.idle()
