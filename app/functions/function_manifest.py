from .chat import functions, function, property, PropertyType

def function_manifest(user):
    manifest = functions()

    # Hmmm -  Not sure about this one - hopefully others might have thoughts. Let ChatGPT ask itself questions.  I'm not sure it can do that unless prompted by a user.  
    # One thing I've noticed is that it may be beneficial to pass the main oai's "messages" into this so it has context...
    f = function(name="askChatGPT", description="Use a Large Language Model (LLM) to perform analysis, summarization, or classification of text using ChatGPT.")
    f.properties.add(property("temperature", PropertyType.integer, "The temperature associated with the request: 0 for factual, up to 2 for very creative.", True))
    f.properties.add(property("question", PropertyType.string, "What are you requesting be done with the text?", True))
    f.properties.add(property("text", PropertyType.string, "The text to be analyzed", True))
    manifest[f.name] = f
    
    # If you've used SQLCLient or OracleClient, this is similar.  You create your function, and add parameters.
    # Then you add your function to the "functions" dictionary object (a dictionary is used to allow subsequent function lookup)
    # Note: "default" on properties is not specified, however, it seems to help chatcompletion.
    f = function(name="getNews", description="News API function")
    f.properties.add(property("q", PropertyType.string, "Query to return news stories", True))
    f.properties.add(property("language", PropertyType.string, "Language of News", True, ["en", "es"], default="en"))
    f.properties.add(property("pageSize", PropertyType.integer, "Page Size", True, None, default=5))
    f.properties.add(property("from", PropertyType.string, "Optional Date of oldest article.", False))
    f.properties.add(property("to", PropertyType.string, "Optional Date of newest article.", False))
    manifest[f.name] = f

    # Weather API (current weather - can be improved to include forecast)
    f = function(name="getCurrentWeather", description="Weather API function for current weather")
    f.properties.add(property("q", PropertyType.string, "Name of city to get weather", True))
    manifest[f.name] = f

    # Weather API (3-day forecast with air quality index data and weather alert data)
    f = function(name="getThreeDayForecast", description="Retrieves the weather forcast for the next 3 days for a specific city.")
    f.properties.add(property("q", PropertyType.string, "Name of city to get weather forecast", True))
    manifest[f.name] = f

    
    if user.groups.filter(name='Production').exists():
        f = function(name="query_production_and_manufacturing_data", description="Information on the production and manufacturing of products including bills of material, product costs, inventory and work orders.")
        f.properties.add(property("question", PropertyType.string, "The question being asked to you.", True))
        manifest[f.name] = f


    if user.groups.filter(name='Sales').exists():
        f = function(name="query_sales_data", description="Information on company sales including revenue, sales representatives, stores, customers and sales orders.")
        f.properties.add(property("question", PropertyType.string, "The question being asked to you.", True))
        manifest[f.name] = f

    if user.groups.filter(name='Purchasing').exists():
        f = function(name="query_purchasing_data", description="Information on vendors and purchase orders.")
        f.properties.add(property("question", PropertyType.string, "The question being asked to you.", True))
        manifest[f.name] = f

    if user.groups.filter(name='Human Resources').exists():
        f = function(name="query_human_resource_data", description="Information about employees, their positions, their roles, their salaries and pay, managers, and departments.")
        f.properties.add(property("question", PropertyType.string, "The question being asked to you.", True))
        manifest[f.name] = f

    # Pinecone vector database API (contains demo "company HR data" from Northwinds)
    # comment out if you are not using Pinecone.
    f = function(name="get_benefits_information", description="Information about the company's health care plans, company policies, and employee roles.")
    f.properties.add(property("prompt", PropertyType.string, "The prompt to be used to query the vector database.  This must be in the form of a concise sentence.", True))
    f.properties.add(property("top", PropertyType.integer, "Records to be returned.", True, None, default=5))
    manifest[f.name] = f

    # Send Email
    # comment out if you are not using SendGrid.
    f = function(name="sendEmail", description="Send an email. Must include to_email, subject, and body properties. Do not use placeholders like [Your Name].")
    f.properties.add(property("to_email", PropertyType.string, "The email recipient address in email format.", True))
    f.properties.add(property("subject", PropertyType.string, "The subject of the email.", True))
    f.properties.add(property("body", PropertyType.string, "The body of the email.", True))
    manifest[f.name] = f

    # Generate an image using Stable Diffusion
    # f = function(name="generateImage", description="Generate an image from a text description.")
    # f.properties.add(property("prompt", PropertyType.string, "Description of the image to generate.", True))
    # manifest[f.name] = f

    # returns the datetime in GMT
    f = function(name="getCurrentUTCDateTime", description="Obtain the current UTC datetime.")
    manifest[f.name] = f


    return manifest

