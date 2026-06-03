# 🎓 DamaphAcademy - Ethiopian Student Study Helper Bot

A comprehensive Telegram bot designed to help Ethiopian students excel in their studies through organized resources, study tips, motivation, and **AI-powered features** using Google Gemini.

## 🌟 Features

### 📚 Study Subjects
- Mathematics (ሂሳብ)
- Science (ሳይንስ)
- English Language
- Amharic (አማርኛ)
- History (ታሪክ)

### 🤖 AI-Powered Features (DamaphAI)
- **Ask Questions** - Get instant answers to any study question
- **Homework Help** - Step-by-step solutions to homework problems
- **Concept Explanations** - Understand difficult concepts easily
- **Essay Feedback** - Get your essays reviewed and improved
- **Study Guides** - Generate comprehensive study materials

### 💡 Other Features
- Study Tips & Techniques
- Daily Motivation Quotes
- Study Schedules
- Interactive Commands
- Bilingual Support (English & Amharic)

---

## 🚀 Quick Start - Deploy on Railway (FREE!)

### **For Mobile Users (No Computer Needed!)** 📱

Railway lets your bot run **24/7 for FREE** on the cloud!

#### **Step 1: Sign Up on Railway** 
1. Open your phone browser
2. Go to: **https://railway.app**
3. Click **"Start Project"**
4. Sign up with **GitHub** (recommended)
5. Authorize Railway

#### **Step 2: Deploy Your Bot**
1. Click **"Create New Project"**
2. Click **"Deploy from GitHub"**
3. Select: **Damaph-sketch/Telagram_bot**
4. Click **"Deploy"**
5. Wait for Railway to build (2-5 minutes)

#### **Step 3: Add Your API Keys** 🔑
1. In Railway dashboard, click your project
2. Click **"Variables"** tab
3. Add these variables:

**Variable 1:**
- Name: `TELEGRAM_BOT_TOKEN`
- Value: Your BotFather token

**Variable 2:**
- Name: `GEMINI_API_KEY`
- Value: Your Gemini API key

4. Save variables

#### **Step 4: Get Your API Keys**

**Telegram Bot Token:**
1. Open Telegram on your phone
2. Search: **@BotFather**
3. Send: `/newbot`
4. Follow instructions to create bot
5. Copy the **token** you receive
6. Paste in Railway variables

**Google Gemini API Key:**
1. Open browser, go: **https://ai.google.dev**
2. Click **"Get API Key"**
3. Sign in with Google account
4. Create new API key
5. Copy it
6. Paste in Railway variables

#### **Step 5: Your Bot is Running!** ✅
- Railway auto-deploys your bot
- Bot runs 24/7 automatically
- No need to keep phone on
- No computer needed!

---

## 💻 Local Setup (For Computer Users)

### **Prerequisites**
- Python 3.8+
- Git
- pip

### **Installation**

1. **Clone repository**
```bash
git clone https://github.com/Damaph-sketch/Telagram_bot.git
cd Telagram_bot
```

2. **Create virtual environment**
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

5. **Add your API keys to .env**
```
TELEGRAM_BOT_TOKEN=your_bot_token_here
GEMINI_API_KEY=your_gemini_api_key_here
```

6. **Run the bot**
```bash
python bot.py
```

---

## 📖 Available Commands

### **Basic Commands**
| Command | Description |
|---------|-------------|
| `/start` | Start the bot and see welcome message |
| `/help` | View all available commands |
| `/subjects` | Browse all study subjects |
| `/tips` | Get study tips and techniques |
| `/schedule` | Get a sample study schedule |
| `/motivation` | Receive motivational quotes |

### **Subject Commands**
| Command | Description |
|---------|-------------|
| `/math` | Access mathematics resources |
| `/science` | Access science resources |
| `/english` | Access English language resources |
| `/amharic` | Access Amharic resources |
| `/history` | Access history resources |

### **AI Commands (DamaphAI)**
| Command | Description |
|---------|-------------|
| `/ask` | Ask DamaphAI any question |
| `/homework` | Get step-by-step homework help |
| `/explain` | Understand difficult concepts |
| `/essay` | Get essay feedback and improvements |
| `/guide` | Generate comprehensive study guides |

---

## 🎯 How to Use the Bot

1. **Find Your Bot:** Search for your bot name in Telegram
2. **Start:** Send `/start` to begin
3. **Explore:** Use `/help` to see all commands
4. **Learn:** Use AI commands to get homework help and study assistance
5. **Browse:** Use `/subjects` to explore study materials

### **Example: Getting Homework Help**
1. Send `/homework`
2. Send your math problem
3. DamaphAI solves it step-by-step! ✅

### **Example: Understanding a Concept**
1. Send `/explain`
2. Send "Photosynthesis"
3. Get detailed explanation! 💡

---

## 📁 Project Structure

```
Telagram_bot/
├── bot.py              # Main bot application
├── damaph_ai.py        # DamaphAI module (AI features)
├── requirements.txt    # Python dependencies
├── .env.example        # Environment configuration template
├── .gitignore          # Git ignore rules
├── Procfile            # Railway deployment configuration
└── README.md           # This file
```

---

## 📦 Dependencies

- **python-telegram-bot** (v20.7) - Telegram Bot API
- **google-generativeai** (v0.3.0) - Google Gemini AI
- **python-dotenv** (v1.0.0) - Environment variables
- **requests** (v2.31.0) - HTTP requests

---

## 🔧 Configuration

### **Environment Variables (.env)**

```env
TELEGRAM_BOT_TOKEN=your_bot_token_here
GEMINI_API_KEY=your_gemini_api_key_here
```

**How to get tokens:**

1. **Telegram Bot Token:**
   - Chat with @BotFather on Telegram
   - Send `/newbot`
   - Follow instructions
   - Copy the token

2. **Google Gemini API Key:**
   - Go to https://ai.google.dev
   - Click "Get API Key"
   - Sign in with Google
   - Create new API key

---

## 🔐 Security

⚠️ **IMPORTANT:**
- Never commit `.env` file to GitHub
- Never share bot token or API keys
- Keep credentials private and secure
- `.gitignore` already protects `.env`

---

## 🌐 Deployment Options

### **Railway (Recommended - FREE)** ⭐
- Sign up: https://railway.app
- No credit card needed
- 24/7 uptime
- Very beginner-friendly
- Perfect for mobile users!

### **Other Options**
- **Render** - https://render.com
- **Heroku** (paid now, but other free alternatives exist)
- **AWS** - Free tier available
- **Google Cloud** - Free tier available

---

## 🐛 Troubleshooting

### **Bot not responding?**
- Check bot token is correct
- Check internet connection
- Verify bot is still running

### **AI features not working?**
- Check Gemini API key is correct
- Check API quota not exceeded
- Verify internet connection

### **Railway deployment failed?**
- Check all variables are added
- Check GitHub repo is public
- Verify Procfile exists
- Try restarting the deployment

---

## 📞 Support

**For issues:**
1. Check `/help` command in bot
2. Review this README
3. Verify API keys are correct
4. Check internet connection
5. Restart the bot

---

## 💡 Tips for Best Results

- Run bot on Railway for 24/7 availability
- Customize study tips for your curriculum
- Add more subjects as needed
- Share bot with other Ethiopian students!
- Keep API keys private and secure
- Monitor Gemini API usage to avoid surprises

---

## 🚀 Future Enhancements

- [ ] Database for tracking user progress
- [ ] Quiz and assessment features
- [ ] Scheduled reminders
- [ ] File sharing (PDFs, notes)
- [ ] Integration with educational websites
- [ ] User profiles and statistics
- [ ] Advanced Q&A system
- [ ] Exam preparation guides
- [ ] Multiple language support

---

## 📄 License

This project is open source and free to use.

---

## 🙏 About

Created with ❤️ for Ethiopian students by **Damaph-sketch**

**DamaphAcademy** - *Education for Everyone* 🎓

ትምህርት ለሁሉም ሰው (Education for All)

---

## 📱 **Mobile Users: Your 24/7 Bot Awaits!**

1. Go to: **https://railway.app**
2. Sign up (2 minutes)
3. Connect GitHub repo (1 minute)
4. Add API keys (2 minutes)
5. **Your bot runs forever!** 🎉

**Total: 5 minutes to 24/7 bot!** ⚡

Happy studying! 🎓✨
