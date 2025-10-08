

quiz = [
    {"question": "What is the capital of France?",
     "options": ["Berlin", "Paris", "Madrid", "Rome"],
     "answer": "Paris"},
    
    {"question": "Which language is used for AI?",
     "options": ["Python", "HTML", "CSS", "SQL"],
     "answer": "Python"},
    
    {"question": "2 + 2 = ?",
     "options": ["3", "4", "5"],
     "answer": "4"}
]

score = 0
results = []

for q in quiz:
    print("\n" + q["question"])
    for i, opt in enumerate(q["options"], 1):
        print(f"{i}. {opt}")
    
    choice = input("Enter option number: ")
    
    if choice.isdigit() and 1 <= int(choice) <= len(q["options"]):
        user_answer = q["options"][int(choice) - 1]
        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
            results.append((q["question"], "Correct"))
        else:
            print(" Wrong!")
            results.append((q["question"], f"Wrong (Ans: {q['answer']})"))
    else:
        print("Invalid choice! Skipped.")

# Final feedback
print("\n--- Quiz Completed ---")
print(f"Your Score: {score}/{len(quiz)}\n")

for r in results:
    print(f"{r[0]} → {r[1]}")
