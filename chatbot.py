# ============================================================
# CODEORBIT AI CHATBOT - VERSION 3
# Author : Raveena Deshmukh
# Language : Python
# ============================================================

import os
import random
import time
from datetime import datetime, date

try:
    from colorama import init, Fore, Style
    init(autoreset=True)
except:
    class Dummy:
        def __getattr__(self, name):
            return ""
    Fore = Dummy()
    Style = Dummy()

HISTORY_FILE = "history.txt"
REPORT_FILE = "report.txt"

total_questions = 0
chat_sessions = 0

greetings = [
    "Hello!",
    "Hi there!",
    "Welcome!",
    "Nice to meet you!",
    "Greetings!"
]

motivations = [
    "Believe in yourself.",
    "Every expert was once a beginner.",
    "Never stop learning.",
    "Consistency beats talent.",
    "Success starts with discipline."
]

jokes = [
    "Why do programmers love Python? Because it's easy to understand!",
    "Debugging is like being a detective in your own mystery.",
    "A SQL query walks into a bar and asks: Can I JOIN you?",
    "Why was the computer cold? It left Windows open.",
    "There are 10 types of people: those who understand binary and those who don't."
]


def logo():
    print(Fore.CYAN + "=" * 50)
    print(Fore.YELLOW + "      🤖 CODEORBIT AI CHATBOT 🤖")
    print(Fore.CYAN + "=" * 50)


def typing():
    print(Fore.GREEN + "\nBot is typing...", end="")
    time.sleep(1)
    print("\r" + " " * 30, end="\r")


def save_history(user, bot):
    with open(HISTORY_FILE, "a", encoding="utf-8") as file:
        file.write(f"You : {user}\n")
        file.write(f"Bot : {bot}\n\n")


def view_history():

    logo()

    if not os.path.exists(HISTORY_FILE):
        print("No history found.")
        return

    with open(HISTORY_FILE, "r", encoding="utf-8") as file:
        print(file.read())


def clear_history():

    open(HISTORY_FILE, "w").close()

    print(Fore.RED + "\nHistory Cleared Successfully.")


def export_report():

    if not os.path.exists(HISTORY_FILE):
        print("No history available.")
        return

    with open(HISTORY_FILE, "r", encoding="utf-8") as h:
        data = h.read()

    with open(REPORT_FILE, "w", encoding="utf-8") as r:
        r.write("CODEORBIT AI CHATBOT REPORT\n")
        r.write("=" * 40 + "\n\n")
        r.write(data)

    print(Fore.GREEN + "\nReport Exported Successfully.")
    print("Saved as report.txt")


def statistics():

    logo()

    print(Fore.YELLOW + "CHAT STATISTICS\n")

    print("Questions Asked :", total_questions)
    print("Chat Sessions   :", chat_sessions)

    if os.path.exists(HISTORY_FILE):

        size = os.path.getsize(HISTORY_FILE)

        print("History Size    :", size, "bytes")

    else:

        print("History Size    : 0 bytes")


def about():

    logo()

    print("Project      : Rule-Based Chatbot")
    print("Version      : 3.0")
    print("Language     : Python")
    print("Internship   : CodeOrbit AI")
    print("Author       : Raveena Deshmukh")
    print("Platform     : Samsung Tablet + Pydroid 3")
    
    # ============================================================
# CHATBOT RESPONSE ENGINE
# ============================================================

def chatbot(user):

    global total_questions

    total_questions += 1

    user = user.lower().strip()

    # ---------------- Greetings ----------------

    if any(word in user for word in
           ["hi", "hello", "hey"]):
        return random.choice(greetings)

    elif "good morning" in user:
        return "Good Morning! Have a productive day."

    elif "good afternoon" in user:
        return "Good Afternoon!"

    elif "good evening" in user:
        return "Good Evening!"

    elif "bye" in user:
        return "Goodbye! See you again."

    elif "thank" in user:
        return "You're welcome."

    elif "how are you" in user:
        return "I am doing great. Thanks for asking."

    # ---------------- Personal ----------------

    elif "your name" in user:
        return "My name is CodeOrbit AI Chatbot."

    elif "who created you" in user or "creator" in user:
        return "I was created by Raveena Deshmukh."

    elif "who are you" in user:
        return "I am a Rule-Based Chatbot built using Python."

    elif "help" in user:
        return "You can ask me about AI, Python, SQL, GitHub, Internship, Power BI and much more."

    # ---------------- AI ----------------

    elif "what is ai" in user or "artificial intelligence" in user:
        return "Artificial Intelligence enables machines to perform tasks that normally require human intelligence."

    elif "machine learning" in user:
        return "Machine Learning allows computers to learn from data without explicit programming."

    elif "deep learning" in user:
        return "Deep Learning uses neural networks with many layers."

    elif "nlp" in user:
        return "NLP stands for Natural Language Processing."

    elif "computer vision" in user:
        return "Computer Vision enables computers to understand images."

    elif "generative ai" in user:
        return "Generative AI creates text, images, code and videos."

    elif "chatgpt" in user:
        return "ChatGPT is an AI chatbot developed by OpenAI."

    elif "llm" in user:
        return "LLM means Large Language Model."

    # ---------------- Python ----------------

    elif "python" in user:
        return "Python is one of the best programming languages for AI and Data Science."

    elif "numpy" in user:
        return "NumPy is used for numerical computing."

    elif "pandas" in user:
        return "Pandas is used for data analysis."

    elif "matplotlib" in user:
        return "Matplotlib is used for plotting charts."

    elif "tensorflow" in user:
        return "TensorFlow is a Deep Learning framework."

    elif "opencv" in user:
        return "OpenCV is used for image processing."

    # ---------------- Data ----------------

    elif "sql" in user:
        return "SQL is used for managing databases."

    elif "database" in user:
        return "A database stores organized information."

    elif "power bi" in user:
        return "Power BI is Microsoft's Business Intelligence tool."

    elif "excel" in user:
        return "Excel is widely used for data analysis."

    elif "dashboard" in user:
        return "Dashboards display KPIs and business insights."

    elif "data science" in user:
        return "Data Science combines statistics, programming and business knowledge."

    elif "data analyst" in user:
        return "A Data Analyst converts raw data into meaningful insights."

    # ---------------- Internship ----------------

    elif "internship" in user:
        return "This internship focuses on practical AI projects."

    elif "certificate" in user:
        return "Complete the required tasks to receive your certificate."

    elif "github" in user:
        return "GitHub is used to store and share source code."

    elif "linkedin" in user:
        return "LinkedIn helps showcase your projects professionally."

    elif "project" in user:
        return "Projects strengthen your portfolio."

    elif "resume" in user:
        return "Keep your resume updated with skills and projects."

    # ---------------- Date & Time ----------------

    elif "date" in user:
        return str(date.today())

    elif "time" in user:
        return datetime.now().strftime("%I:%M %p")

    elif "day" in user:
        return datetime.now().strftime("%A")

    # ---------------- Motivation ----------------

    elif "motivate" in user:
        return random.choice(motivations)

    elif "quote" in user:
        return random.choice(motivations)

    elif "joke" in user:
        return random.choice(jokes)

    # ---------------- Maths ----------------

    elif "2+2" in user:
        return "2 + 2 = 4"

    elif "5*5" in user:
        return "5 × 5 = 25"

    # ---------------- Exit ----------------

    elif "exit" == user:
        return "Returning to Main Menu..."

    # ---------------- Default ----------------

    else:
        return ("Sorry! I don't understand that.\n"
                "Please ask another question.")
                
                # ============================================================
# CHAT FUNCTIONS
# ============================================================

def start_chat():

    global chat_sessions

    chat_sessions += 1

    logo()

    print(Fore.GREEN + "\nWelcome to CodeOrbit AI Chatbot")

    name = input(Fore.YELLOW + "\nEnter Your Name : ")

    print(Fore.CYAN + "\nHello", name + "!")
    print("Type 'exit' anytime to return to the Main Menu.\n")

    while True:

        user = input(Fore.YELLOW + "\nYou : ")

        if user.lower() == "exit":

            print(Fore.GREEN + "\nReturning to Main Menu...")
            break

        typing()

        reply = chatbot(user)

        print(Fore.CYAN + "🤖 Bot :", reply)

        save_history(user, reply)


# ============================================================
# HELP MENU
# ============================================================

def help_menu():

    logo()

    print(Fore.GREEN + "\nYou can ask questions about:\n")

    topics = [

        "Greetings",
        "Artificial Intelligence",
        "Machine Learning",
        "Deep Learning",
        "Python",
        "NumPy",
        "Pandas",
        "SQL",
        "Power BI",
        "Excel",
        "GitHub",
        "LinkedIn",
        "Resume",
        "Internship",
        "Projects",
        "Date",
        "Time",
        "Day",
        "Motivation",
        "Quotes",
        "Jokes"

    ]

    for topic in topics:

        print("•", topic)

    print("\nExample Questions:")
    print("-----------------------------")
    print("Hello")
    print("What is AI?")
    print("What is Machine Learning?")
    print("Tell me about Python")
    print("What is SQL?")
    print("What is Power BI?")
    print("Tell me a joke")
    print("Motivate me")
    print("What is today's date?")
    print("What time is it?")


# ============================================================
# SEARCH QUESTIONS
# ============================================================

def search_topic():

    logo()

    keyword = input("\nEnter Keyword : ").lower()

    available = [

        "ai",
        "machine learning",
        "deep learning",
        "python",
        "numpy",
        "pandas",
        "sql",
        "power bi",
        "excel",
        "github",
        "linkedin",
        "resume",
        "internship",
        "project",
        "date",
        "time",
        "motivate",
        "quote",
        "joke"

    ]

    found = False

    for item in available:

        if keyword in item:

            print(Fore.GREEN + "\nFound Topic :", item.title())
            found = True

    if not found:

        print(Fore.RED + "\nNo matching topic found.")


# ============================================================
# WELCOME SCREEN
# ============================================================

def welcome():

    logo()

    print(Fore.MAGENTA + "\nCode. Create. Succeed.")

    print(Fore.GREEN + "\nProfessional Rule-Based Chatbot")

    print("\nFeatures")

    print("------------------------")

    print("✓ 50+ Questions")

    print("✓ Chat History")

    print("✓ Export Report")

    print("✓ Statistics")

    print("✓ Typing Animation")

    print("✓ AI Information")

    print("✓ Python Information")

    print("✓ Internship Guide")

    print("✓ Motivation & Jokes")

    input("\nPress Enter to Continue...")
    
    # ============================================================
# MAIN MENU
# ============================================================

welcome()

while True:

    logo()

    print(Fore.YELLOW + "\n=========== MAIN MENU ===========")

    print("1. Start Chat")
    print("2. View History")
    print("3. Export Report")
    print("4. Chat Statistics")
    print("5. Help")
    print("6. Search Topics")
    print("7. Clear History")
    print("8. About")
    print("9. Exit")

    print("=" * 33)

    choice = input(Fore.GREEN + "\nEnter Your Choice : ")

    if choice == "1":

        start_chat()

    elif choice == "2":

        view_history()

        input("\nPress Enter to Continue...")

    elif choice == "3":

        export_report()

        input("\nPress Enter to Continue...")

    elif choice == "4":

        statistics()

        input("\nPress Enter to Continue...")

    elif choice == "5":

        help_menu()

        input("\nPress Enter to Continue...")

    elif choice == "6":

        search_topic()

        input("\nPress Enter to Continue...")

    elif choice == "7":

        confirm = input("\nAre you sure? (yes/no): ").lower()

        if confirm == "yes":

            clear_history()

        else:

            print("History not deleted.")

        input("\nPress Enter to Continue...")

    elif choice == "8":

        about()

        input("\nPress Enter to Continue...")

    elif choice == "9":

        logo()

        print(Fore.GREEN + "\nThank you for using CodeOrbit AI Chatbot.")

        print("Goodbye!")

        break

    else:

        print(Fore.RED + "\nInvalid Choice!")

        input("\nPress Enter to Try Again...")
    