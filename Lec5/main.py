from telegram import Update
from telegram.ext import *


async def hello(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("5565678844:AAHcLJFaRngdp-7pkMwjbb1AiSe-3CWdJyg")

app.add_handler(CommandHandler("hello", hello))
print('server start')
app.run_polling()

# import matplotlib.pyplot as plt
# import numpy as np

# # Fixing random state for reproducibility
# np.random.seed(19680801)


# plt.rcdefaults()
# fig, ax = plt.subplots()

# # Example data
# people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
# y_pos = np.arange(len(people))
# performance = 3 + 10 * np.random.rand(len(people))
# error = np.random.rand(len(people))

# ax.barh(y_pos, performance, xerr=error, align='center')
# ax.set_yticks(y_pos, labels=people)
# ax.invert_yaxis()  # labels read top-to-bottom
# ax.set_xlabel('Performance')
# ax.set_title('How fast do you want to go today?')

# plt.show()


# import emoji
# print(emoji.emojize('Python is :thumbs_up:'))


# from progress.bar import Bar
# import time
# bar = Bar('Loading', fill='#', suffix='%(percent)d%%')
# for i in range(100):
#     time.sleep(0.1)
#     bar.next()
# bar.finish()



# from isOdd import isOdd
#
# print(isOdd(1))
# print(isOdd(4))
