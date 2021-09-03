import telebot

bot = telebot.TeleBot('1933672908:AAHFFpPpDPSsNfDgLTsLKCwT7hxkUN9l4Jc')


@bot.message_handler(commands=['start'])
def send_welcome(message):

  reply_keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
  # reply_keyboard.row('✅ Add', '🖊️ Edit')
  #reply_keyboard.row('1', '2', '3', '4', '5', '6', '7', '8')
  #reply_keyboard.row('9', '10', '11', '12', '13', '14', '15', '16')
  #reply_keyboard.row('17', '18', '19', '20', '21', '22', '23', '24')
  #reply_keyboard.row('25', '26', '27', '28', '29', '30', '31')

  #reply_keyboard.row('Jan', 'Feb', 'Mar', 'Apr')
  #reply_keyboard.row('May', 'Jun', 'Jul', 'Aug')
  #reply_keyboard.row('Sep', 'Oct', 'Nov', 'Dec')

  #reply_keyboard.row('Січ', 'Лют', 'Бер', 'Кві')
  #reply_keyboard.row('Тра', 'Чер', 'Лип', 'Сер')
  #reply_keyboard.row('Вер', 'Жов', 'Лис', 'Гру')

  reply_keyboard.row('👨‍👩‍👦 Friends & family', '👑 Money & career')
  reply_keyboard.row('💪 Health & body', '💡 Mind & creativity')
  reply_keyboard.row('⏳ Philosophy & spirituality')
  
  reply_keyboard.row('↩️ Back', 'Skip ➡️')
  bot.send_message(message.from_user.id, "What type it was?", reply_markup=reply_keyboard)

bot.polling(none_stop=True)