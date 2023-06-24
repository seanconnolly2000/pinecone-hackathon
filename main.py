import os
import json

from dotenv import load_dotenv
from functions.openaif import openaif
from functions.chat import functions, function, property, PropertyType
from functions.samples import getCurrentWeather, getThreeDayForecast, getNews, getCurrentUTCDateTime


def main():
    load_dotenv()
    # You'll need to create a ".env" file with your credentials in the format:
    # OPENAI_APIKEY=sk-xxxxxxx
    # OTHER_ITEMS=xxxyyy

    functions_available_to_chatGPT = functions()

    # Hmmm -  Not sure about this one - hopefully others might have thoughts. Let ChatGPT ask itself questions.  I'm not sure it can do that unless prompted by a user.  
    # One thing I've noticed is that it may be beneficial to pass the main oai's "messages" into this so it has context...
    f = function(name="askChatGPT", description="Use a Large Language Model (LLM) to perform analysis, summarization, or classification of text using ChatGPT.")
    f.properties.add(property("temperature", PropertyType.integer, "The temperature associated with the request: 0 for factual, up to 2 for very creative.", True))
    f.properties.add(property("question", PropertyType.string, "What are you requesting be done with the text?", True))
    f.properties.add(property("text", PropertyType.string, "The text to be analyzed", True))
    functions_available_to_chatGPT[f.name] = f
    
    # If you've used SQLCLient or OracleClient, this is similar.  You create your function, and add parameters.
    # Then you add your function to the "functions" dictionary object (a dictionary is used to allow subsequent function lookup)
    # Note: "default" on properties is not specified, however, it seems to help chatcompletion.
    f = function(name="getNews", description="News API function")
    f.properties.add(property("q", PropertyType.string, "Query to return news stories", True))
    f.properties.add(property("language", PropertyType.string, "Language of News", True, ["en", "es"], default="en"))
    f.properties.add(property("pageSize", PropertyType.integer, "Page Size", True, None, default=5))
    f.properties.add(property("from", PropertyType.string, "Optional Date of oldest article.", False))
    f.properties.add(property("to", PropertyType.string, "Optional Date of newest article.", False))
    functions_available_to_chatGPT[f.name] = f

    # Weather API (current weather - can be improved to include forecast)
    f = function(name="getCurrentWeather", description="Weather API function for current weather")
    f.properties.add(property("q", PropertyType.string, "Name of city to get weather", True))
    functions_available_to_chatGPT[f.name] = f

    # Weather API (3-day forecast with air quality index data and weather alert data)
    f = function(name="getThreeDayForecast", description="Retrieves the weather forcast for the next 3 days for a specific city.")
    f.properties.add(property("q", PropertyType.string, "Name of city to get weather forecast", True))
    functions_available_to_chatGPT[f.name] = f

    
    # SQL database call - 
    # comment out if you are not using SQL.
    #f = function(name="querySQL", description="Query the Adventureworks database.")
    #f.properties.add(property("sql", PropertyType.string, "The sql code to execute against the Adventureworks database.", True))
    #functions_available_to_chatGPT[f.name] = f

    f = function(name="query_corporate_data", description="Query the corporate database that contains sales, finance, and product data.")
    f.properties.add(property("question", PropertyType.string, "The question being asked to you.", True))
    functions_available_to_chatGPT[f.name] = f


    # Pinecone vector database API (contains demo "company HR data" from Northwinds)
    # comment out if you are not using Pinecone.
    f = function(name="getPineconeData", description="Company data pertaining only to health care plans, company policies, and employee roles.")
    f.properties.add(property("prompt", PropertyType.string, "The prompt to be used to query the vector database.  This must be in the form of a concise sentence.", True))
    f.properties.add(property("top", PropertyType.integer, "Records to be returned.", True, None, default=5))
    functions_available_to_chatGPT[f.name] = f

    # Send Email
    # comment out if you are not using SendGrid.
    f = function(name="sendEmail", description="Send an email. Must include to_email, subject, and body properties. Do not use placeholders like [Your Name].")
    f.properties.add(property("to_email", PropertyType.string, "The email recipient address in email format.", True))
    f.properties.add(property("subject", PropertyType.string, "The subject of the email.", True))
    f.properties.add(property("body", PropertyType.string, "The body of the email.", True))
    functions_available_to_chatGPT[f.name] = f

    # Generate an image using Stable Diffusion
    # f = function(name="generateImage", description="Generate an image from a text description.")
    # f.properties.add(property("prompt", PropertyType.string, "Description of the image to generate.", True))
    # functions_available_to_chatGPT[f.name] = f

    # returns the datetime in GMT
    f = function(name="getCurrentUTCDateTime", description="Obtain the current UTC datetime.")
    functions_available_to_chatGPT[f.name] = f

    # returns a random dog's name
    f = function(name="getDogName", description="Obtain the dog's name")
    functions_available_to_chatGPT[f.name] = f

    # instantiate the llm with the functions in list format (.to_json())
    openai_key = os.environ.get("OPENAI_APIKEY")
    oai = openaif(openai_key, functions_available_to_chatGPT)

    #TODO: 

    #login = input('Login: ')
    #password = input('Password: ')


    # Feel free to experiment with the system role below.  In my experiments, this seems to cause problematic output including ignoring user
    # instruction to convert to PST, and sending content through in the same responses that also request a function_call.
    oai.set_chat_context("The current user's name is Sean Connolly. His timezone is Pacific so please adjust times appropriately. Only include data from function calls in your responses. If you don't know something, say 'I don't know.'")

    # FUN CHALLENGE: make 4 calls: getDogName, getCurrentDateTime (and switch it to Pacific - not always accurate), getWeather, and get some news stories
    # Since I am asking it to get a little creative with sightseeing tips for London, I'm setting the temperature below to 1.
    oai.temperature = .5
    
    # The prompt below shows how it is possible to chain together many function calls.  This is crazy cool:
    # prompt = "What is my dog's name, tell me what time is it in PST, what is the weather like in London, and what sightseeing activities would you recommend for London this time of year?  Also please give me 5 articles on the US Economy from the last week.  Also are hearing aids included in my Northwinds Standard Healthcare Plan? Also email bob@xxxyyy.com and tell him I am running late for lunch."

    #Contributor John was cool enough to add the recursive question input.
    while True:
        prompt = input("Enter your question ('cls' to reset chat, 'quit' to quit): ")
        if prompt.lower() == 'quit':
            break
        if prompt.lower() == 'cls':
            oai.clear_chat_session()
        else:
            res = oai.user_request(prompt)
             # Replace the degree symbol
            res = res.replace('\u00b0F', ' degrees Fahrenheit').replace('\u00b0C',' degrees Celcius')
            print(res)

if __name__ == "__main__":
    main()