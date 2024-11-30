import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def ask_question(question):
    """ Ask the user a question and return their response. """
    print(question)
    response = input() 
    return response

def get_user_preferences():
    """ Gather preferences from the user. """
    print("Hi! Where would you like to go?")
    destination = ask_question("Please provide your destination.")
    
    print("When are you planning to visit?")
    visit_date = ask_question("Please provide the date and time.")
    
    print("What type of places do you like to visit? For example, historical sites, nature, food?")
    interests = ask_question("Enter your preferences.")
    
    print("Do you have a budget in mind for the trip? Please specify.")
    budget = ask_question("Enter your budget.")
    
    print("Where are you starting from? (For example, from your hotel)")
    start_location = ask_question("Enter your starting point.")

    return {
        "destination": destination,
        "visit_date": visit_date,
        "interests": interests.lower().split(", "),  
        "budget": budget,
        "start_location": start_location
    }
