import telepot
import time
from telepot.loop import MessageLoop
from imtosy import imtosy
global count
count = 0

def handle(msg):
    global count
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'photo':
        bot.download_file(msg['photo'][-1]['file_id'], './file'+str(count)+'.jpg')
        imtosy('file'+str(count)+'.jpg',30,3000)
        bot.sendPhoto(chat_id,open('file'+str(count)+'result.jpg', 'rb'))
        count += 1

basic_auth = ('fovlaxcorpA9', 'D8r5KdS')
SetProxy = telepot.api.set_proxy("https://191.101.148.35:34512", basic_auth)
bot = telepot.Bot('985081018:AAHm2N1iQjUasHXsIVGv1AUL8aLrl-MpNd4')

MessageLoop(bot, handle).run_as_thread()



while 1:
    time.sleep(10);


