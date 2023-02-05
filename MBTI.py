# Myers-Briggs Type Indicator questions
questions = {
    "E/I": "Do you prefer to spend time with others or alone?\n(E)xtrovert or (I)ntrovert",
    "S/N": "Do you focus on facts and details or abstract possibilities?\n(S)ensing or (N)on-sensing",
    "T/F": "Do you make decisions based on logic and analysis or values and emotions?\n(T)hinking or (F)eeling",
    "J/P": "Do you prefer a structured, planned approach or a flexible, spontaneous approach?\n(J)udging or (P)erceiving",
    "P/J": "When you have an important project due, do you prefer to have a deadline or have more flexibility?\n(P)lanning or (J)ust in time",
    "F/T": "When in a conflict, do you focus more on preserving the relationship or finding a solution?\n(F)eeling or (T)hinking",
    "N/S": "Do you enjoy experiencing new things or do you prefer familiar and predictable environments?\n(N)ew experiences or (S)tability",
    "I/E": "Do you feel energized after spending time with a large group of people or do you prefer quiet solitude?\n(I)ntrovert or (E)xtrovert"
}

# Character types based on Myers-Briggs
character_types = {
    "ISTJ": "Introverted, Sensing, Thinking, Judging",
    "ISFJ": "Introverted, Sensing, Feeling, Judging",
    "INFJ": "Introverted, Intuitive, Feeling, Judging",
    "INTJ": "Introverted, Intuitive, Thinking, Judging",
    "ISTp": "Introverted, Sensing, Thinking, Perceiving",
    "ISFp": "Introverted, Sensing, Feeling, Perceiving",
    "INFp": "Introverted, Intuitive, Feeling, Perceiving",
    "INTP": "Introverted, Intuitive, Thinking, Perceiving",
    "ESTJ": "Extraverted, Sensing, Thinking, Judging",
    "ESFJ": "Extraverted, Sensing, Feeling, Judging",
    "ENFJ": "Extraverted, Intuitive, Feeling, Judging",
    "ENTJ": "Extraverted, Intuitive, Thinking, Judging",
    "ESTP": "Extraverted, Sensing, Thinking, Perceiving",
    "ESFP": "Extraverted, Sensing, Feeling, Perceiving",
    "ENFP": "Extraverted, Intuitive, Feeling, Perceiving",
    "ENTP": "Extraverted, Intuitive, Thinking, Perceiving"
}

# Function to ask a question and get the answer
def get_answer(question):
    while True:
        answer = input(question + ": ").upper()
        if answer in ['E', 'I', 'S', 'N', 'T', 'F', 'J', 'P']:
            return answer
        else:
            print("Invalid answer. Please enter either 'E', 'I', 'S', 'N', 'T', 'F', 'J', or 'P'.")

# Function to analyze the answers and determine the character type
def get_result(answers):
    ei = answers["E/I"]
    sn = answers["S/N"]
    tf = answers["T/F"]
    jp = answers["J/P"]

    if ei == "E":
        if sn == "S":
            if tf == "T":
                if jp == "J":
                    result = "ESTJ"
                else:
                    result = "ESTP"
            else:
                if jp == "J":
                    result = "ESFJ"
                else:
                    result = "ESFP"
        else:
            if tf == "T":
                if jp == "J":
                    result = "ENTJ"
                else:
                    result = "ENTP"
            else:
                if jp == "J":
                    result = "ENFJ"
                else:
                    result = "ENFP"
    else:
        if sn == "S":
            if tf == "T":
                if jp == "J":
                    result = "ISTJ"
                else:
                    result = "ISTp"
            else:
                if jp == "J":
                    result = "ISFJ"
                else:
                    result = "ISFp"
        else:
            if tf == "T":
                if jp == "J":
                    result = "INTJ"
                else:
                    result = "INTP"
            else:
                if jp == "J":
                    result = "INFJ"
                else:
                    result = "INFp"

    return result

# Main program
answers = {}
for question in questions:
    answers[question] = get_answer(questions[question])

result = get_result(answers)

print("\nYour Myers-Briggs type is: " + result)
print("Description: " + character_types[result])
