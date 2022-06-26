# Using RestApi to create two API endpoints (urls)
## API path: /date ['GET']
- This returns the current date for today. Example response : { "date" : "Today is 2022-06-06 !" }

### API path : /random ['POST']
- This api needs a min , max JSON object, and based on it, it will generate a random number between the minimum and maximum value.
- If the minimum value is less than 0, then return a response that it is not supported. 
- else return the random number.     

Example Request JSON: 
     {"min" : 5, "max" : 200}
     
     
Example Response JSON:
       {"random" : 26}

Example Response if min number less than 0:
    {"msg", "Not Allowed. Please provide a min that is bigger than 0"}
    

