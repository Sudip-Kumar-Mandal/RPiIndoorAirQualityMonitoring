from telepot import Bot
import analyse_data

api_key = "6955890484:AAF_VE-dFoTArmh3s8-ymp4MXeDQJ8LJZYQ"
chat_id = "1224531480"

bot = Bot(api_key)

with open("analysed_data/text.txt", mode='r') as file:
  stats = file.read()

formatted_message = f'''
**Stats**
```
{stats}
```
'''

bot.sendMessage(chat_id, formatted_message, parse_mode="Markdown")
bot.sendPhoto(chat_id, photo=open('analysed_data/chart.png', 'rb'))