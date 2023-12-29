import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"


def unknown():
    response = ["Could you please re-phrase that? ",
                "I'm sorry, but I am not sure what you are asking. Can you please rephrase your question?...",
                "I'm sorry, but I am not sure what you are asking. Can you please rephrase your question?",
                "What does that mean?"][
        random.randrange(4)]
    return response
