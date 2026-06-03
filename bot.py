#!/usr/bin/env python3
"""
DamaphAcademy - Ethiopian Student Study Helper Telegram Bot
A comprehensive bot designed to help Ethiopian students with their studies
"""

import os
import logging
import random
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Get bot token
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

if not BOT_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN not found in environment variables")

# Study resources database
STUDY_RESOURCES = {
    'math': {
        'name': 'ሂሳብ (Mathematics)',
        'topics': ['Algebra', 'Geometry', 'Calculus', 'Statistics', 'Trigonometry'],
        'tips': '✏️ Practice math at least 30 minutes every day!'
    },
    'science': {
        'name': 'ሳይንስ (Science)',
        'topics': ['Biology', 'Chemistry', 'Physics', 'Environmental Science'],
        'tips': '🔬 Understand science through practical experiments!'
    },
    'english': {
        'name': 'English (English Language)',
        'topics': ['Grammar', 'Vocabulary', 'Reading', 'Writing', 'Speaking'],
        'tips': '📖 Learn one new word every day!'
    },
    'amharic': {
        'name': 'አማርኛ (Amharic)',
        'topics': ['Grammar', 'Literature', 'Writing', 'Comprehension'],
        'tips': '📚 Practice writing Amharic carefully!'
    },
    'history': {
        'name': 'ታሪክ (History)',
        'topics': ['Ethiopian History', 'World History', 'Ancient Civilizations'],
        'tips': '🏛️ Understand history by connecting events and dates!'
    }
}

# Motivational quotes in English and Amharic
MOTIVATIONAL_QUOTES = [
    '🌟 "Education is not the filling of a pail, but the lighting of a fire." - William Butler Yeats',
    '💪 "Success is no accident. It is hard work, perseverance, learning, studying, sacrifice and most of all, love of what you are doing."',
    '🎯 "The future belongs to those who believe in the beauty of their dreams."',
    '📖 "Education is the most powerful weapon which you can use to change the world."',
    '🏆 "You are capable of achieving great things!"',
    '⭐ "Every expert was once a beginner."',
    '🚀 "The only way to do great work is to love what you do."'
]

# Study tips
STUDY_TIPS = """
**🎯 Best Study Tips for Success:**

1. **Set Clear Goals**
   - Know exactly what you need to study each day

2. **Use the Pomodoro Technique**
   - Study for 25 minutes, then take a 5-minute break
   - Repeat 4 times, then take a longer break

3. **Get Good Sleep**
   - Sleep at least 8 hours every night
   - A rested mind learns better

4. **Take Active Notes**
   - Don't just highlight - write in your own words
   - Summarize key points

5. **Study in Groups**
   - Learn from classmates
   - Teach others to reinforce your knowledge

6. **Practice Regularly**
   - Do exercises and past papers
   - Practice makes perfect!

7. **Stay Healthy**
   - Eat nutritious food
   - Exercise regularly
   - Stay hydrated

8. **Minimize Distractions**
   - Turn off your phone
   - Find a quiet place to study
   - Focus completely on your work

9. **Review Regularly**
   - Don't just cram before exams
   - Review material weekly

10. **Stay Positive**
    - Believe in yourself
    - Celebrate small victories
    - Don't give up!
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    welcome_message = f"""
🎓 **Welcome to DamaphAcademy!** 🎓

Hello {user.first_name}! 👋

I'm **DamaphAcademy**, your personal study helper bot!
I'm here to help you succeed in your studies with resources, tips, and motivation.

**What I can help you with:**
📚 Study Resources - Organized by subject
💡 Study Tips - Proven learning techniques
⏰ Study Schedules - Time management plans
🏆 Motivation - Daily encouragement
🎯 Subject Help - Math, Science, English, Amharic, History

**Try these commands:**
/help - See all available commands
/subjects - Browse study subjects
/motivation - Get motivated!
/tips - Learn study techniques
/schedule - Get a study plan
"""
    await update.message.reply_text(welcome_message, parse_mode='Markdown')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    help_text = """
**DamaphAcademy Commands:**

**Main Commands:**
/start - Start the bot
/help - Show this help message
/subjects - Browse all study subjects
/motivation - Get motivational quotes
/tips - Learn study techniques
/schedule - Get a study plan

**Subject Commands:**
/math - Mathematics resources
/science - Science resources
/english - English language resources
/amharic - Amharic language resources
/history - History resources

**Quick Tips:**
✏️ Study for 25 minutes, rest for 5 (Pomodoro)
🎯 Set clear daily goals
📝 Take notes actively
🔄 Practice regularly
😴 Sleep 8 hours per night
"""
    await update.message.reply_text(help_text, parse_mode='Markdown')

async def subjects(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show available subjects with inline buttons."""
    keyboard = [
        [InlineKeyboardButton("📐 Mathematics", callback_data='subject_math')],
        [InlineKeyboardButton("🔬 Science", callback_data='subject_science')],
        [InlineKeyboardButton("📖 English", callback_data='subject_english')],
        [InlineKeyboardButton("📚 Amharic", callback_data='subject_amharic')],
        [InlineKeyboardButton("🏛️ History", callback_data='subject_history')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        '**Choose a subject to learn:** 📚',
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def subject_button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle subject button presses."""
    query = update.callback_query
    await query.answer()
    
    subject_key = query.data.replace('subject_', '')
    subject = STUDY_RESOURCES.get(subject_key)
    
    if subject:
        message = f"""
**{subject['name']}** 📖

**Main Topics:**
"""
        for i, topic in enumerate(subject['topics'], 1):
            message += f"\n{i}. {topic}"
        
        message += f"\n\n**Tip:** {subject['tips']}"
        
        await query.edit_message_text(
            text=message,
            parse_mode='Markdown'
        )
    else:
        await query.edit_message_text(text="Subject not found.")

async def motivation(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a motivational quote."""
    quote = random.choice(MOTIVATIONAL_QUOTES)
    await update.message.reply_text(quote, parse_mode='Markdown')

async def tips(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send study tips."""
    await update.message.reply_text(STUDY_TIPS, parse_mode='Markdown')

async def schedule(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a study schedule template."""
    schedule_text = """
**📅 Sample Study Schedule:**

**Afternoon Session:**
- 🕖 3:00 - 3:30 PM: Rest and refresh
- 🕖 3:30 - 4:00 PM: Mathematics
- 🕖 4:00 - 4:30 PM: Science
- 🕖 4:30 - 5:00 PM: English / Break

**Evening Session:**
- 🕘 7:00 - 7:30 PM: Group study / Discussion
- 🕘 7:30 - 8:00 PM: Amharic / History
- 🕘 8:00 - 8:30 PM: Review and practice
- 🕘 8:30+ PM: Rest and prepare for bed

**Tips for Success:**
✅ Adjust this schedule to fit your needs
✅ Don't overload yourself - quality over quantity
✅ Take breaks every 25-30 minutes
✅ Stay consistent with your routine
✅ Get enough sleep
✅ Eat healthy food
✅ Exercise regularly

Remember: *Consistency is key to success!* 🎯
"""
    await update.message.reply_text(schedule_text, parse_mode='Markdown')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo user message and provide help."""
    message = update.message.text
    response = f"""
I received your message: **"{message}"**

However, I'm designed to help with specific study commands.

Try using these commands:
/help - See all available commands
📚 /subjects - Browse study materials
💡 /tips - Get study advice
🎓 /motivation - Get motivated
📅 /schedule - Get a study plan
"""
    await update.message.reply_text(response, parse_mode='Markdown')

def main() -> None:
    """Start the bot."""
    # Create the Application
    application = Application.builder().token(BOT_TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("subjects", subjects))
    application.add_handler(CommandHandler("motivation", motivation))
    application.add_handler(CommandHandler("tips", tips))
    application.add_handler(CommandHandler("schedule", schedule))
    
    # Subject commands
    application.add_handler(CommandHandler("math", subjects))
    application.add_handler(CommandHandler("science", subjects))
    application.add_handler(CommandHandler("english", subjects))
    application.add_handler(CommandHandler("amharic", subjects))
    application.add_handler(CommandHandler("history", subjects))

    # Handle button callbacks and messages
    application.add_handler(CallbackQueryHandler(subject_button))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot
    logger.info("DamaphAcademy Bot is running...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    logger.info("Starting DamaphAcademy Telegram Bot...")
    main()
