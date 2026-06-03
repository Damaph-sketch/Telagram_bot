#!/usr/bin/env python3
"""
DamaphAcademy - Enhanced Ethiopian Student Study Helper Telegram Bot
Now with AI-powered features using Google Gemini via DamaphAI
"""

import os
import logging
import random
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes, ConversationHandler
from damaph_ai import get_ai_instance

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

# Get AI instance
ai = get_ai_instance()

# Conversation states
ASKING_QUESTION, ASKING_HOMEWORK, ASKING_CONCEPT, ASKING_ESSAY = range(4)

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

# Motivational quotes
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

1. **Set Clear Goals** - Know exactly what you need to study each day
2. **Use Pomodoro Technique** - Study 25 min, rest 5 min
3. **Get Good Sleep** - Sleep at least 8 hours every night
4. **Take Active Notes** - Write in your own words
5. **Study in Groups** - Learn from classmates
6. **Practice Regularly** - Do exercises and past papers
7. **Stay Healthy** - Eat nutritious food and exercise
8. **Minimize Distractions** - Turn off your phone
9. **Review Regularly** - Don't just cram before exams
10. **Stay Positive** - Believe in yourself!
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    welcome_message = f"""
🎓 **Welcome to DamaphAcademy with AI!** 🎓

Hello {user.first_name}! 👋

I'm **DamaphAcademy**, your AI-powered study helper bot!
Now enhanced with **DamaphAI** for intelligent homework help, Q&A, and more!

**What I can help you with:**
📚 Study Resources - Organized by subject
💡 Study Tips - Proven learning techniques
⏰ Study Schedules - Time management plans
🏆 Motivation - Daily encouragement
🤖 **AI Features:**
   • Ask homework questions
   • Get concept explanations
   • Review your essays
   • Generate study guides

**Try these commands:**
/help - See all available commands
/subjects - Browse study subjects
/ask - Ask DamaphAI any question
/homework - Get homework help
/explain - Understand concepts
/essay - Get essay feedback
/schedule - Get a study plan
/motivation - Get motivated!
"""
    await update.message.reply_text(welcome_message, parse_mode='Markdown')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    help_text = """
**DamaphAcademy Commands:**

**📚 Study Commands:**
/start - Start the bot
/help - Show this help message
/subjects - Browse all study subjects
/tips - Learn study techniques
/schedule - Get a study plan
/motivation - Get motivational quotes

**🤖 AI Commands:**
/ask - Ask DamaphAI any question
/homework - Get homework help (step-by-step)
/explain - Understand a concept
/essay - Get essay feedback & improvement
/guide - Generate a study guide

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

async def ask_question(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Start conversation to ask DamaphAI a question."""
    await update.message.reply_text(
        "🤖 **Ask DamaphAI Anything!**\n\n"
        "What would you like to ask? "
        "(You can ask about any subject - Math, Science, English, Amharic, History, etc.)\n\n"
        "Type /cancel to stop.",
        parse_mode='Markdown'
    )
    return ASKING_QUESTION

async def process_question(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Process the user's question with AI."""
    question = update.message.text
    
    # Show loading message
    loading_msg = await update.message.reply_text("🤖 DamaphAI is thinking... ⏳")
    
    try:
        # Get AI response
        response = ai.answer_question(question, subject="General")
        
        # Send response
        await update.message.reply_text(f"🤖 **DamaphAI Response:**\n\n{response}", parse_mode='Markdown')
        
        await loading_msg.delete()
        await update.message.reply_text("Ask another question with /ask or type /help for more options!")
        
        return ConversationHandler.END
        
    except Exception as e:
        await loading_msg.delete()
        await update.message.reply_text(f"❌ Error: {str(e)[:100]}")
        return ConversationHandler.END

async def homework_help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Start conversation for homework help."""
    await update.message.reply_text(
        "📝 **Homework Help from DamaphAI**\n\n"
        "Send me your homework problem and I'll help you solve it step-by-step!\n\n"
        "Type /cancel to stop.",
        parse_mode='Markdown'
    )
    return ASKING_HOMEWORK

async def process_homework(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Process homework problem with AI."""
    problem = update.message.text
    
    # Show loading message
    loading_msg = await update.message.reply_text("🤖 Analyzing your homework... ⏳")
    
    try:
        # Get AI response
        response = ai.solve_homework(problem, subject="General", level="high school")
        
        # Send response
        await update.message.reply_text(f"📝 **Solution:**\n\n{response}", parse_mode='Markdown')
        
        await loading_msg.delete()
        await update.message.reply_text("Need help with another problem? Send /homework")
        
        return ConversationHandler.END
        
    except Exception as e:
        await loading_msg.delete()
        await update.message.reply_text(f"❌ Error: {str(e)[:100]}")
        return ConversationHandler.END

async def explain_concept(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Start conversation for concept explanation."""
    await update.message.reply_text(
        "💡 **Concept Explanation**\n\n"
        "What concept would you like me to explain? "
        "(e.g., 'Photosynthesis', 'Quadratic equations', 'French Revolution')\n\n"
        "Type /cancel to stop.",
        parse_mode='Markdown'
    )
    return ASKING_CONCEPT

async def process_concept(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Process concept explanation with AI."""
    concept = update.message.text
    
    # Show loading message
    loading_msg = await update.message.reply_text("🤖 Explaining concept... ⏳")
    
    try:
        # Get AI response
        response = ai.explain_concept(concept, subject="General", detail_level="medium")
        
        # Send response
        await update.message.reply_text(f"💡 **Explanation:**\n\n{response}", parse_mode='Markdown')
        
        await loading_msg.delete()
        await update.message.reply_text("Need another explanation? Send /explain")
        
        return ConversationHandler.END
        
    except Exception as e:
        await loading_msg.delete()
        await update.message.reply_text(f"❌ Error: {str(e)[:100]}")
        return ConversationHandler.END

async def essay_feedback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Start conversation for essay review."""
    await update.message.reply_text(
        "✍️ **Essay Review**\n\n"
        "Send me your essay and I'll provide feedback on grammar, structure, and content!\n\n"
        "Type /cancel to stop.",
        parse_mode='Markdown'
    )
    return ASKING_ESSAY

async def process_essay(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Process essay with AI."""
    essay = update.message.text
    
    # Show loading message
    loading_msg = await update.message.reply_text("🤖 Reviewing your essay... ⏳")
    
    try:
        # Get AI response
        response = ai.check_and_improve_essay(essay, subject="General")
        
        # Send response
        await update.message.reply_text(f"✍️ **Feedback:**\n\n{response}", parse_mode='Markdown')
        
        await loading_msg.delete()
        await update.message.reply_text("Need another review? Send /essay")
        
        return ConversationHandler.END
        
    except Exception as e:
        await loading_msg.delete()
        await update.message.reply_text(f"❌ Error: {str(e)[:100]}")
        return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancel conversation."""
    await update.message.reply_text("❌ Cancelled. How can I help you? /help")
    return ConversationHandler.END

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
✅ Don't overload yourself
✅ Take breaks every 25-30 minutes
✅ Stay consistent
✅ Get enough sleep

*Consistency is key to success!* 🎯
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
🤖 /ask - Ask DamaphAI
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
    
    # AI conversation handlers
    ask_handler = ConversationHandler(
        entry_points=[CommandHandler("ask", ask_question)],
        states={
            ASKING_QUESTION: [MessageHandler(filters.TEXT & ~filters.COMMAND, process_question)]
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )
    
    homework_handler = ConversationHandler(
        entry_points=[CommandHandler("homework", homework_help)],
        states={
            ASKING_HOMEWORK: [MessageHandler(filters.TEXT & ~filters.COMMAND, process_homework)]
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )
    
    concept_handler = ConversationHandler(
        entry_points=[CommandHandler("explain", explain_concept)],
        states={
            ASKING_CONCEPT: [MessageHandler(filters.TEXT & ~filters.COMMAND, process_concept)]
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )
    
    essay_handler = ConversationHandler(
        entry_points=[CommandHandler("essay", essay_feedback)],
        states={
            ASKING_ESSAY: [MessageHandler(filters.TEXT & ~filters.COMMAND, process_essay)]
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )
    
    application.add_handler(ask_handler)
    application.add_handler(homework_handler)
    application.add_handler(concept_handler)
    application.add_handler(essay_handler)

    # Handle button callbacks and messages
    application.add_handler(CallbackQueryHandler(subject_button))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot
    logger.info("DamaphAcademy Bot with AI is running...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    logger.info("Starting DamaphAcademy Enhanced Bot with DamaphAI...")
    main()
