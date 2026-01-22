Questions = [
    {
        "question": "Who is known as the Father of the Nation in India?",
        "options": ["A. Mahatma Gandhi", "B. Jawaharlal Nehru", "C. Sardar Patel", "D. Bhagat Singh"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Venus", "D. Jupiter"],
        "answer": "B"
    },
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Which is the largest ocean in the world?",
        "options": ["A. Indian Ocean", "B. Arctic Ocean", "C. Atlantic Ocean", "D. Pacific Ocean"],
        "answer": "D"
    },
    {
        "question": "Who wrote 'Ramayana'?",
        "options": ["A. Ved Vyas", "B. Valmiki", "C. Tulsidas", "D. Kalidas"],
        "answer": "B"
    },
    {
        "question": "Which gas do plants absorb from the atmosphere?",
        "options": ["A. Oxygen", "B. Carbon monoxide", "C. Nitrogen", "D. Carbon dioxide"],
        "answer": "D"
    },
    {
        "question": "Who invented the telephone?",
        "options": ["A. Thomas Edison", "B. Alexander Graham Bell", "C. Nikola Tesla", "D. James Watt"],
        "answer": "B"
    },
    {
        "question": "What is the national animal of India?",
        "options": ["A. Peacock", "B. Tiger", "C. Elephant", "D. Lion"],
        "answer": "B"
    },
    {
        "question": "Which festival is known as the Festival of Lights?",
        "options": ["A. Holi", "B. Eid", "C. Diwali", "D. Christmas"],
        "answer": "C"
    },
    {
        "question": "How many players are there in a cricket team?",
        "options": ["A. 9", "B. 10", "C. 11", "D. 12"],
        "answer": "C"
    },
    {
        "question": "Which currency is used in Japan?",
        "options": ["A. Yuan", "B. Dollar", "C. Yen", "D. Euro"],
        "answer": "C"
    },
    {
        "question": "Which vitamin do we get from sunlight?",
        "options": ["A. Vitamin A", "B. Vitamin C", "C. Vitamin D", "D. Vitamin B"],
        "answer": "C"
    },
    {
        "question": "Which is the smallest continent in the world?",
        "options": ["A. Australia", "B. Africa", "C. Europe", "D. Asia"],
        "answer": "A"
    },
    {
        "question": "Who discovered gravity?",
        "options": ["A. Albert Einstein", "B. Isaac Newton", "C. Galileo", "D. Maxwell"],
        "answer": "B"
    },
    {
        "question": "Which animal is known as the Ship of the Desert?",
        "options": ["A. Camel", "B. Horse", "C. Dog", "D. Cow"],
        "answer": "A"
    }
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]

total_amount = 0
print("Welcome to the KBC Quiz Game!\n")

for i in range(len(Questions)):
    Question= Questions[i]

    print(f"\n\nQuestion for Rs.{levels[i]}")

    print(f"{Question['question']}")
    for option in Question['options']:
        print(option)
    Answer = input("Enter your answer (A/B/C/D) or E to Quit : ").strip().upper()
    if (Answer == 'E'):
        total_amount= levels[i-1] 
        break
    if(Answer == Question['answer']):
        print(f"Correct Answer ! you Won Rs.{levels[i]}\n") 
        total_amount += levels[i]   
    elif Answer == 'E':
        print(f"You chose to quit! You are taking home Rs.{total_amount}\n")
        break
    else:
        print(f"Wrong Answer! The correct answer is {Question['answer']}.")
        print("Game Over!\n")
        break


