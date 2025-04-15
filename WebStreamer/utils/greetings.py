import random

GREETINGS = [
    "✨ Konichiwa", 
    "🌞 Today is a great day to share files!", 
    "👋 Hey hey", 
    "📬 You've got vibes!", 
    "🌀 What's poppin'", 
    "🌟 Heya superstar", 
    "🎉 Let's make something awesome today", 
    "🌈 Yo!", 
    "🚀 Ready to stream?", 
    "💡 Light up the file world!",
    "📂 Time to send something cool",
    "🧊 Dropping files like a pro",
]

def greeting():
    return random.choice(GREETINGS)
