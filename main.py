import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = '7808581622:AAEazy78GkY_pic3hyxmjTpgmA-Hnups8wo'  # Replace with your actual bot token
bot = telebot.TeleBot(API_TOKEN)

# Menu data from the image
menu_data = {
    "Monday": {
        "Breakfast": {"menu": "Pav Bhaji, Tea", "image": "path/to/pav_bhaji_image.jpg"},
        "Lunch": {"menu": "Mix Veg, Dal Fry, Green Peas Pulao, Raita, Chapati and Fruits", "image": "path/to/mix_veg_image.jpg"},
        "Snacks": {"menu": "Masala Pav, Tea", "image": "path/to/masala_pav_image.jpg"},
        "Dinner": {"menu": "Matar Paneer/ Palak Paneer, Black Dal, Plain Rice, Shahi Tukda, Chapati", "image": "path/to/matar_paneer_image.jpg"}
    },
    "Tuesday": {
        "Breakfast": {"menu": "Poha, Black Chana/ Dalia, Coconut Chutney, Coffee", "image": "path/to/poha_image.jpg"},
        "Lunch": {"menu": "Rajma Masala, Aloo Bhindi Dry, Plain Rice, Curd, Salad, Chapati and Fruits", "image": "path/to/rajma_image.jpg"},
        "Snacks": {"menu": "Samosa, Chutney, Tea", "image": "path/to/samosa_image.jpg"},
        "Dinner": {"menu": "Chhole Masala, Dal Fry, Masala Rice, Chapati, Methi Roti, Sheera", "image": "path/to/chhole_image.jpg"}
    },
    "Wednesday": {
        "Breakfast": {"menu": "Idli, Sambhar/ Coconut Chutney, Tea", "image": "path/to/idli_image.jpg"},
        "Lunch": {"menu": "Dal Makhni, Chana Cabbage Dry, Zeera Rice, Curd, Chapati and Fruits", "image": "path/to/dal_makhni_image.jpg"},
        "Snacks": {"menu": "Vada Pav, Tea", "image": "path/to/vada_pav_image.jpg"},
        "Dinner": {"menu": "Paneer Kofta/ Chicken Curry, Dal Fry, Rice, Chapati, Fruit Custard", "image": "path/to/paneer_kofta_image.jpg"}
    },
    "Thursday": {
        "Breakfast": {"menu": "Puri Bhaji, Tea", "image": "path/to/puri_bhaji_image.jpg"},
        "Lunch": {"menu": "Veg Biryani, Curry, Papad, Raita and Fruits", "image": "path/to/veg_biryani_image.jpg"},
        "Snacks": {"menu": "Poha, Chutney, Coffee", "image": "path/to/poha_snack_image.jpg"},
        "Dinner": {"menu": "Aloo Gobhi/ Veg Tawa, Chana Dal Palak, Zeera Rice, Ajwain Chapati, Gulab Jamun", "image": "path/to/aloo_gobhi_image.jpg"}
    },
    "Friday": {
        "Breakfast": {"menu": "Bread Butter Jam, Veg Cutlet/ Boiled Eggs (2 pcs), Tea", "image": "path/to/bread_butter_image.jpg"},
        "Lunch": {"menu": "Aloo Matar, Dahi Kadi, Onion Pakoda (2 pcs), Plain Rice, Salad, Roti and Fruits", "image": "path/to/aloo_matar_image.jpg"},
        "Snacks": {"menu": "Bread Pakoda, Chutney, Tea", "image": "path/to/bread_pakoda_image.jpg"},
        "Dinner": {"menu": "Paneer Kadai/ Egg Curry, Plain Rice, Dal Fry, Chapati, Shevai Kheer", "image": "path/to/paneer_kadai_image.jpg"}
    },
    "Saturday": {
        "Breakfast": {"menu": "Aloo Paratha, Curd, Tea", "image": "path/to/aloo_paratha_image.jpg"},
        "Lunch": {"menu": "Methi Roti/ Chhole Bhature, Rice, Dal Fry, Boondi Raita, Salad and Fruits", "image": "path/to/chhole_bhature_image.jpg"},
        "Snacks": {"menu": "Bhel (Onion + Chutney + Chilies Incl.), Coffee", "image": "path/to/bhel_image.jpg"},
        "Dinner": {"menu": "Soyabean Sabzi, Masoor Dal Fry, Masala Rice, Chapati, Rice Kheer, Chinese Food (Chow Mein, Fried Rice, Soup)", "image": "path/to/soyabean_image.jpg"}
    },
    "Sunday": {
        "Breakfast": {"menu": "Onion-Tomato Uttapam/ Veg Upma, Sambhar, Tea", "image": "path/to/uttapam_image.jpg"},
        "Lunch": {"menu": "Black Chana Masala, Dal Fry, Rice, Raita, Chapati and Fruits", "image": "path/to/black_chana_image.jpg"},
        "Snacks": {"menu": "Cream Bun, Tea", "image": "path/to/cream_bun_image.jpg"},
        "Dinner": {"menu": "Aloo Palak/ Aloo Mattar, Panchratan Dal, Green Peas Pulao, Puri/ Methi Roti, Sabudana Kheer", "image": "path/to/aloo_palak_image.jpg"}
    }
}

user_data = {}

# Start command handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_data[message.chat.id] = {}
    markup = InlineKeyboardMarkup(row_width=3)

    # Creating buttons for each day with emojis
    days = [
        ("Monday", "🌞 Monday"), 
        ("Tuesday", "🌮 Tuesday"),
        ("Wednesday", "🍲 Wednesday"), 
        ("Thursday", "🍱 Thursday"), 
        ("Friday", "🍔 Friday"), 
        ("Saturday", "🍕 Saturday"), 
        ("Sunday", "🍜 Sunday")
    ]

    for day, label in days:
        markup.add(InlineKeyboardButton(label, callback_data=f"day_{day}"))

    welcome_message = (
        "👋 Welcome to the Meal Info Bot! \n\n"
        "Please select a day of the week to get the meal information:"
    )
    bot.send_message(message.chat.id, welcome_message, reply_markup=markup, parse_mode="Markdown")

# Handler for day selection
@bot.callback_query_handler(func=lambda call: call.data.startswith("day_"))
def select_meal_type(call):
    day = call.data.split("_")[1]
    user_data[call.message.chat.id]["day"] = day

    markup = InlineKeyboardMarkup(row_width=2)
    # Creating buttons for meal types with emojis
    meal_types = [
        ("Breakfast", "☕ Breakfast"), 
        ("Lunch", "🍛 Lunch"), 
        ("Snacks", "🍪 Snacks"), 
        ("Dinner", "🍽 Dinner")
    ]

    for meal_type, label in meal_types:
        markup.add(InlineKeyboardButton(label, callback_data=f"meal_{meal_type}"))

    bot.edit_message_text(
        f"You selected {day}. \n\nNow, please choose the type of meal:", 
        chat_id=call.message.chat.id, 
        message_id=call.message.message_id, 
        reply_markup=markup,
        parse_mode="Markdown"
    )

# Handler for meal type selection
@bot.callback_query_handler(func=lambda call: call.data.startswith("meal_"))
def show_menu(call):
    meal_type = call.data.split("_")[1]
    day = user_data.get(call.message.chat.id, {}).get("day")

    # Check if the day and meal type are valid
    if day and meal_type in menu_data.get(day, {}):
        meal_data = menu_data[day][meal_type]
        menu_text = meal_data["menu"]
        image_path = meal_data["image"]

        # Send the menu in bold with an emoji and markdown formatting
        bot.edit_message_text(
            f"🍽 Here is the menu for {meal_type} on {day}:\n\n"
            f"{menu_text}",
            chat_id=call.message.chat.id, 
            message_id=call.message.message_id,
            parse_mode="Markdown"
        )

        # Send the image corresponding to the meal
        try:
            with open(image_path, 'rb') as img:
                bot.send_photo(call.message.chat.id, img)
        except FileNotFoundError:
            bot.send_message(call.message.chat.id, "😋 yumm yumm")

    else:
        bot.edit_message_text(
            "⚠ Menu not available for this selection.",
            chat_id=call.message.chat.id, 
            message_id=call.message.message_id,
            parse_mode="Markdown"
        )

    # Option to offer further assistance or end session
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(InlineKeyboardButton("🔄 Get More Info", callback_data="more_info"))
    markup.add(InlineKeyboardButton("🚪 End Session", callback_data="end_session"))

    bot.send_message(call.message.chat.id, "Would you like further assistance?", reply_markup=markup)

bot.polling(none_stop=True)

#
