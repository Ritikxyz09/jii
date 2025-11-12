import os
import random
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Your Bot Token (already added)
BOT_TOKEN = "8565663576:AAFnaC-qxL2WC0ELRk8wJhDS_86BJm23gwM"

# Enhanced chat responses
RESPONSES = [
    "Hello! Nice to talk with you! 😊",
    "How's your day going?",
    "That's interesting! Tell me more.",
    "I'd love to hear more about that!",
    "What do you enjoy doing in your free time?",
    "That sounds wonderful!",
    "I'm here to chat with you!",
    "How are you feeling today?",
    "That's really cool!",
    "Thanks for sharing that with me!",
    "What's on your mind?",
    "I'm listening...",
    "That's amazing!",
    "Hope you're having a great day! 🌟",
    "You're such an interesting person!",
    "I enjoy our conversations! 💫",
    "That's a great perspective!",
    "Tell me something new you learned today!",
    "What makes you happy?",
    "You have a wonderful way of thinking!",
    "I appreciate you talking with me!",
    "That's so thoughtful of you!",
    "You're amazing! 🌈",
    "What are your dreams and aspirations?",
    "You have a great sense of humor! 😄",
    "That's very insightful!",
    "I love your energy! ⚡",
    "You're doing great!",
    "What's your favorite memory?",
    "You have such a positive vibe! 🌸"
]

# Special responses for specific keywords
KEYWORD_RESPONSES = {
    "hello": ["Hi there! 👋", "Hello! Nice to see you!", "Hey! How can I help?"],
    "how are you": ["I'm doing great! Thanks for asking! 😊", "I'm wonderful! How about you?", "All good here! How are you?"],
    "name": ["I'm your friendly chat bot! 🤖", "You can call me ChatPal!", "I'm your digital friend!"],
    "love": ["That's so sweet! 💖", "Aww, thank you!", "You're making me blush! 😊"],
    "happy": ["That's awesome! 😄", "Happiness looks good on you!", "So glad to hear that! 🎉"],
    "sad": ["I'm here for you 💕", "Would you like to talk about it?", "Sending you positive vibes! 🌈"],
    "thank": ["You're welcome! 😊", "Anytime!", "Happy to help! 🌟"],
    "bye": ["Goodbye! Take care! 👋", "See you later! 😊", "Bye! Hope to chat again soon!"],
    "music": ["I love music too! 🎵", "What's your favorite song?", "Music makes everything better!"],
    "food": ["Food is amazing! 🍕", "What's your favorite cuisine?", "I could talk about food all day!"],
    "movie": ["Movies are great! 🎬", "What's your favorite film?", "I love watching stories unfold!"],
    "game": ["Games are fun! 🎮", "Do you play video games?", "I enjoy game conversations!"]
}

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_text(
        f"Hi {user.first_name}! 👋\n"
        "I'm your friendly chat companion! 🤖\n"
        "Just send me a message and I'll reply!\n\n"
        "Commands:\n"
        "/start - Start chatting\n"
        "/help - Show help\n"
        "/chat - Start random chat\n"
        "/fun - Get a fun message\n\n"
        "Let's have a great conversation! 💫"
    )

def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text(
        "🌟 **How to use me:**\n\n"
        "Just send me any message and I'll respond!\n\n"
        "📋 **Available commands:**\n"
        "/start - Start the bot\n"
        "/help - Show this help\n"
        "/chat - Start a conversation\n"
        "/fun - Get a fun surprise\n"
        "/info - Bot information\n\n"
        "💬 **I can talk about:**\n"
        "• Your day\n• Feelings\n• Interests\n• Dreams\n• And much more!"
    )

def chat_command(update: Update, context: CallbackContext) -> None:
    """Start a random chat."""
    chat_starters = [
        "Let's chat! 💬 What's on your mind today?",
        "Conversation time! 🎉 Tell me something interesting!",
        "I'm all ears! 👂 What would you like to talk about?",
        "Yay! Chat time! 💫 Share your thoughts with me!",
        "Let's have a wonderful conversation! 🌈 What's new?"
    ]
    update.message.reply_text(random.choice(chat_starters))

def fun_command(update: Update, context: CallbackContext) -> None:
    """Send a fun message."""
    fun_messages = [
        "🌟 You're amazing! Never forget that!",
        "😊 Keep smiling! It looks good on you!",
        "💫 The world is better with you in it!",
        "🌈 You're capable of amazing things!",
        "🎉 Today is going to be great!",
        "✨ You have a beautiful soul!",
        "🦋 Believe in yourself like I believe in you!",
        "🌻 Your positivity is contagious!",
        "⚡ You're stronger than you think!",
        "🎈 Sending you good vibes!"
    ]
    update.message.reply_text(random.choice(fun_messages))

def info_command(update: Update, context: CallbackContext) -> None:
    """Show bot information."""
    update.message.reply_text(
        "🤖 **About Me:**\n\n"
        "I'm a friendly chatbot created to have pleasant conversations!\n\n"
        "💡 **My Purpose:**\n"
        "• Provide friendly company\n"
        "• Engage in positive chats\n"
        "• Spread good vibes\n"
        "• Be a good listener\n\n"
        "Remember: I'm an AI friend here to make your day better! 🌟"
    )

def echo(update: Update, context: CallbackContext) -> None:
    """Respond to user messages with intelligent replies."""
    user_message = update.message.text
    
    # Don't respond to commands
    if user_message.startswith('/'):
        return
    
    # Check for keywords and respond accordingly
    response = get_intelligent_response(user_message.lower())
    update.message.reply_text(response)

def get_intelligent_response(message):
    """Generate an intelligent response based on message content."""
    # Check for specific keywords first
    for keyword, responses in KEYWORD_RESPONSES.items():
        if keyword in message:
            return random.choice(responses)
    
    # Check for question patterns
    if any(word in message for word in ['?', 'what', 'how', 'why', 'when', 'where', 'who']):
        question_responses = [
            "That's a great question! What do you think?",
            "I'd love to know your thoughts on that first!",
            "Interesting question! Let me think about that...",
            "What's your perspective on that?",
            "That really makes me think! 🤔"
        ]
        return random.choice(question_responses)
    
    # Check for emotional words
    emotion_words = ['excited', 'happy', 'joy', 'amazing', 'wonderful', 'beautiful']
    if any(word in message for word in emotion_words):
        return "I love your positive energy! 🌟"
    
    # Default to random response
    return random.choice(RESPONSES)

def main():
    """Start the bot."""
    try:
        # Create the Updater and pass it your bot's token.
        updater = Updater(BOT_TOKEN)
        
        # Get the dispatcher to register handlers
        dispatcher = updater.dispatcher
        
        # Register command handlers
        dispatcher.add_handler(CommandHandler("start", start))
        dispatcher.add_handler(CommandHandler("help", help_command))
        dispatcher.add_handler(CommandHandler("chat", chat_command))
        dispatcher.add_handler(CommandHandler("fun", fun_command))
        dispatcher.add_handler(CommandHandler("info", info_command))
        
        # Register message handler - FIXED: using filters instead of Filters
        dispatcher.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
        
        # Start the Bot
        print("🤖 Bot is starting...")
        print("✅ Token loaded successfully!")
        print("📍 Press Ctrl+C to stop the bot")
        print("🌐 Bot is now live on Telegram!")
        
        updater.start_polling()
        
        # Run the bot until you press Ctrl-C
        updater.idle()
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Please check your bot token and internet connection.")

if __name__ == '__main__':
    main()
