import art
import table
import random
print(art.logo)




def select(data):
    random_question = random.choice(data)
    return random_question
    

game_over = False
score = 0
data = table.data
while not game_over:
    question = select(data)
    print(f"Compare A: {question['name']}, a {question['description']}, from {question['country']}.")
    print(art.vs)
    question2 = select(data)
    if question2 == question:
        question2 = select(data)
    print(f"Against B: {question2['name']}, a {question2['description']}, from {question2['country']}.")
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    if answer == "a" and question["follower_count"] > question2["follower_count"]:
        score += 1
        print(f"You're right! Current score: {score}")
    elif answer == "b" and question["follower_count"] < question2["follower_count"]:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_over = True

