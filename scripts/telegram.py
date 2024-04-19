from telepot import Bot
import telegram_secrets as tele
import analyse_data

bot = Bot(tele.api_key)

with open("analysed_data/text.txt", mode='r') as file:
  stats = file.read()

formatted_message = f'''
**Stats**
```
{stats}
```
'''

bot.sendMessage(tele.chat_id, formatted_message, parse_mode="Markdown")
bot.sendPhoto(tele.chat_id, photo=open('analysed_data/chart.png', 'rb'))