import requests
import html

# Fetch live questions from server (15 questions)
url = "https://opentdb.com/api.php?amount=15&type=multiple"
response = requests.get(url).json()

Questions = []

for q in response["results"]:
    correct = html.unescape(q["correct_answer"])
    incorrect = [html.unescape(x) for x in q["incorrect_answers"]]

    options = incorrect + [correct]
    # shuffle options for randomness
    import random
    random.shuffle(options)

    # Convert A-D format
    mapped_options = [
        f"A. {options[0]}",
        f"B. {options[1]}",
        f"C. {options[2]}",
        f"D. {options[3]}",
    ]

    # Store in your structure
    Questions.append({
        "question": html.unescape(q["question"]),
        "options": mapped_options,
        "answer": ["A", "B", "C", "D"][options.index(correct)]
    })


levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000,
          320000, 640000, 1250000, 2500000, 5000000, 10000000]

total_amount = 0
print("\nWelcome to KBC (Live Edition!)\n")

for i in range(len(Questions)):
    q = Questions[i]
    
    print(f"\nQuestion for Rs {levels[i]}:")
    print(q["question"])
    
    for opt in q["options"]:
        print(opt)
        
    ans = input("\nEnter your answer (A/B/C/D) or E to Quit: ").strip().upper()
    
    if ans == q["answer"]:
        print(f"Correct! You won Rs {levels[i]}")
        total_amount = levels[i]
    elif ans == "E":
        print(f"You quit! You take home Rs {total_amount}")
        break
    else:
        print("Wrong answer!")
        print(f"Correct answer was: {q['answer']}")
        print(f"You take home Rs {total_amount}")
        break