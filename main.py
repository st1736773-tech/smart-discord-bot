import discord
from discord.ext import commands
import random
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"🚀 {bot.user} is now online!")

# Auto reply chatbot system
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    msg = message.content.lower()

    responses = {
        "hi": ["Hello 😄", "Hi there 👋", "Hey! 😊"],
        "hello": ["Hello! 👋", "Hey there 😄"],
        "hey": ["Hey! What's up? 😎"],
        "how are you": ["I'm doing great 😄", "All good! 💪"],
        "what is your name": ["I'm Shreya's bot 🤖✨"],
        "who are you": ["I'm a Discord chatbot 🤖"],
        "who made you": ["I was made by Shreya 💻🔥"],
        "bye": ["Goodbye 👋", "See you soon 😁"],
        "good morning": ["Good morning ☀️", "Have a great day 😄"],
        "good night": ["Good night 🌙", "Sweet dreams 😴"],
        "thanks": ["You're welcome 😊", "No problem 😄"],
        "thank you": ["Anytime 👍", "Glad to help 😊"],
        "sorry": ["It's okay 😊", "No worries 👍"],
        "help": ["Just type a message and I will reply 😎"],
        "what can you do": ["I can chat and respond to messages 🤖"],
        "ping": ["Pong 🏓"],
        "joke": ["Why did the computer smile? Because it got a byte 😄"],
        "lol": ["😂😂😂"],
        "haha": ["😄😄😄"],
        "i am sad": ["Don't be sad 😔 Everything will be okay ❤️"],
        "i am happy": ["That's great 😄 Stay happy 💖"],
        "motivate me": ["You are strong 💪 Never give up 🔥"],
        "study": ["Focus on your studies 📚 You can do it 💯"],
        "exam": ["Best of luck for your exams 🍀📚"],
        "python": ["Python is an awesome language 🐍🔥"],
        "coding": ["Coding is fun 💻😎"],
        "programming": ["Practice makes you better 💪💻"],
        "discord": ["Discord is a cool platform 😎"],
        "server": ["This is a great server 🔥"],
        "game": ["Which game do you like 🎮"],
        "music": ["Music makes everything better 🎶"],
        "movie": ["I love movies 🎬😄"],
        "food": ["Food is life 😋"],
        "time": ["Time is precious ⏰"],
        "date": ["Today is a great day 😊"],
        "cool": ["You are cooler 😎🔥"],
        "ok": ["Okay 👍"],
        "hmm": ["Hmm 🤔"],
        "yes": ["Alright 👍"],
        "no": ["Okay 😄"],
        "capital of india": ["New Delhi is the capital of India 🇮🇳"],
        "prime minister of india": ["The Prime Minister of India is Narendra Modi"],
        "largest planet": ["Jupiter is the largest planet 🌍"],
        "national animal of india": ["Tiger is the national animal of India 🐅"],
        "national bird of india": ["Peacock is the national bird of India 🦚"],
         "ibm": [
             "IBM stands for International Business Machines 💼",
             "IBM focuses on AI, Cloud, Cybersecurity & Data Science"
         ],
         "what is ai": [
             "AI means Artificial Intelligence 🤖",
             "AI allows machines to think like humans"
         ],
         "what is cloud computing": [
             "Cloud computing means storing data on the internet ☁️"
         ],
         "what is machine learning": [
             "Machine Learning is a part of AI that learns from data 📊"
         ],
        "what is artificial intelligence": [
            "Artificial Intelligence is the simulation of human intelligence in machines 🤖",
            "AI enables machines to think, learn, and make decisions"
        ],
        "types of ai": [
            "Types of AI are: Narrow AI, General AI, and Super AI"
        ],
        "applications of ai": [
            "AI is used in healthcare, education, finance, robotics, and chatbots"
        ],
        "ai examples": [
            "Examples of AI are Siri, Alexa, ChatGPT, and self-driving cars 🚗"
        ],
        "what is machine learning": [
            "Machine Learning is a subset of AI that learns from data 📊",
            "Machine Learning allows systems to improve automatically with experience"
        ],
        "types of machine learning": [
            "Types of ML are: Supervised, Unsupervised, and Reinforcement Learning"
        ],
        "supervised learning": [
            "Supervised learning uses labeled data for training"
        ],
        "unsupervised learning": [
            "Unsupervised learning finds patterns in unlabeled data"
        ],
        "reinforcement learning": [
            "Reinforcement learning learns by rewards and punishments 🎯"
        ],
        "ml examples": [
            "ML examples include spam detection, recommendation systems, and image recognition"
        ],
        "what is ibm": [
            "IBM stands for International Business Machines 💼"
        ],
        "ibm interview questions": [
            "IBM interview focuses on technical skills, problem solving, and communication"
        ],
        "why do you want to join ibm": [
            "IBM is a global leader in AI, cloud computing, and innovation"
        ],
        "ibm technologies": [
            "IBM works on AI, Cloud Computing, Cybersecurity, Blockchain, and Data Science"
        ],
        "cloud computing": [
            "Cloud computing means accessing data and services over the internet ☁️"
        ],
         "how to study ai": [
             "Start with Python, then learn ML basics, and practice projects 📚"
         ],
         "how to learn machine learning": [
             "Learn Python, statistics, algorithms, and practice with datasets"
         ],
         "career in ai": [
             "Career options include AI Engineer, Data Scientist, and ML Engineer"
         ],
         "career in machine learning": [
             "ML Engineers are in high demand across industries 🚀"
         ],
        "i am confused": [
            "Take one step at a time, learning will become easy 😊"
        ],
        "i am stressed": [
            "Relax, stay focused, and believe in yourself 💪"
        ],
        "motivate me": [
            "Hard work beats talent when talent doesn't work hard 🔥"
        ],
        "who is my bf":["prince ji is your bf"]
    }

    for key in responses:
        if key in msg:
            await message.channel.send(random.choice(responses[key]))
            return

    await bot.process_commands(message)

# Commands section
@bot.command()
async def hi(ctx):
    await ctx.send("Hello 😄 you are doing command great!")

@bot.command()
async def about(ctx):
    await ctx.send("🤖 i am discord bot!")

@bot.command()
async def owner(ctx):
    await ctx.send("👑 Owner: shreya tiwari")

@bot.command()
async def ping(ctx):
    await ctx.send(f"🏓 Pong! {round(bot.latency * 1000)}ms")

bot.run(os.getenv("DISCORD_TOKEN"))
