# 🎓 DamaphAcademy - Ethiopian Student Study Helper Bot

A comprehensive Telegram bot designed to help Ethiopian students excel in their studies through organized resources, study tips, motivation, and interactive learning tools.

## 🌟 Features

- **📚 Subject Resources**: Organized study materials for:
  - Mathematics (ሂሳብ)
  - Science (ሳይንስ)
  - English Language
  - Amharic (አማርኛ)
  - History (ታሪክ)

- **💡 Study Tips**: Proven techniques to improve learning efficiency
- **🎯 Study Schedule**: Pre-designed study schedules to maximize productivity
- **🏆 Motivation Quotes**: Daily motivational messages
- **👋 Interactive Commands**: Easy-to-use commands for quick access

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Telegram Bot Token (from [BotFather](https://t.me/botfather))
- pip (Python package manager)

### Installation Steps

1. **Clone the repository**
```bash
git clone https://github.com/Damaph-sketch/Telagram_bot.git
cd Telagram_bot
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Setup environment variables**
```bash
cp .env.example .env
```

5. **Add your Telegram Bot Token**
   - Open `.env` file
   - Replace `your_bot_token_here` with your actual token from BotFather
   ```
   TELEGRAM_BOT_TOKEN=your_actual_token_here
   ```

6. **Run the bot**
```bash
python bot.py
```

## 📖 Available Commands

| Command | Description |
|---------|-------------|
| `/start` | Start the bot and see welcome message |
| `/help` | View all available commands |
| `/subjects` | Browse all study subjects |
| `/math` | Access mathematics resources |
| `/science` | Access science resources |
| `/english` | Access English language resources |
| `/amharic` | Access Amharic resources |
| `/history` | Access history resources |
| `/tips` | Get study tips and techniques |
| `/motivation` | Receive motivational quotes |
| `/schedule` | Get a sample study schedule |

## 🎯 How to Use the Bot

1. **Start**: Send `/start` to begin
2. **Explore**: Use `/subjects` to browse available study materials
3. **Learn**: Send `/tips` to receive study advice
4. **Get Inspired**: Use `/motivation` for daily inspiration
5. **Plan**: Use `/schedule` to get a structured study plan

## 📁 Project Structure

```
Telagram_bot/
├── bot.py              # Main bot application
├── requirements.txt    # Python dependencies
├── .env.example       # Environment configuration template
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## 📦 Dependencies

- **python-telegram-bot** (v20.7): Official Telegram Bot API wrapper
- **python-dotenv** (v1.0.0): Environment variable management
- **requests** (v2.31.0): HTTP library

## 🔧 Configuration

### Environment Setup

Create a `.env` file in the root directory with your bot token:

```env
TELEGRAM_BOT_TOKEN=your_bot_token_here
```

**How to get a Telegram Bot Token:**
1. Open Telegram
2. Search for @BotFather
3. Send `/newbot`
4. Follow the instructions
5. Copy the token and paste it in `.env`

## 📚 Study Resources

### Subjects Covered

**Mathematics (ሂሳብ)**
- Algebra, Geometry, Calculus, Statistics, Trigonometry

**Science (ሳይንስ)**
- Biology, Chemistry, Physics, Environmental Science

**English**
- Grammar, Vocabulary, Reading, Writing, Speaking

**Amharic (አማርኛ)**
- Grammar, Literature, Writing, Comprehension

**History (ታሪክ)**
- Ethiopian History, World History, Ancient Civilizations

### Study Tips Included

- Pomodoro Technique (25 min study + 5 min rest)
- Time management strategies
- Effective note-taking methods
- Group study benefits
- Sleep and nutrition importance
- Regular practice recommendations

## 🔐 Security Notes

⚠️ **Important:**
- Never commit your `.env` file to GitHub
- Never share your bot token with anyone
- Keep your bot token private and secure
- Use `.gitignore` to prevent accidental token uploads

## 🎓 Features in Detail

### Interactive Subject Selection
- Click buttons to select subjects
- Get curated topics for each subject
- Receive subject-specific study tips

### Motivational System
- Random motivational quotes
- Encouragement messages
- Success mindset building

### Study Planning
- Sample daily schedule
- Time allocation suggestions
- Break recommendations

## 🔄 How It Works

```
User sends command → Bot processes → Bot responds with info/buttons
                                   ↓
                        User clicks button → Bot shows details
```

## 🚀 Future Enhancements

- [ ] Database for tracking user progress
- [ ] Quiz and assessment features
- [ ] Scheduled reminders
- [ ] File sharing (PDFs, notes)
- [ ] Integration with educational websites
- [ ] User profiles and statistics
- [ ] AI-powered Q&A system
- [ ] Exam preparation guides

## 🐛 Troubleshooting

### Bot won't start
- Check if bot token is correct in `.env`
- Verify internet connection
- Ensure Python 3.8+ is installed

### Commands not working
- Make sure you're using `/` before commands
- Check bot is running (`python bot.py` in terminal)
- Restart the bot

### Dependencies error
- Run: `pip install -r requirements.txt`
- Update pip: `pip install --upgrade pip`

## 📞 Support

For help:
1. Check the `/help` command in the bot
2. Review this README
3. Check your internet connection
4. Restart the bot

## 💡 Tips for Best Results

- Run the bot on a server for 24/7 availability
- Customize the study tips for your curriculum
- Add more subjects as needed
- Share with other Ethiopian students!

## 📄 License

This project is open source and free to use.

## 🙏 About

Created with ❤️ for Ethiopian students by **Damaph-sketch**

---

**DamaphAcademy** - *Education for Everyone* 🎓

ትምህርት ለሁሉም ሰው
