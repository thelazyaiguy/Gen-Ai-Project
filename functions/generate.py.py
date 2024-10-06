import json
import openai
import os

# Set up your OpenAI API key from an environment variable
openai.api_key = os.getenv("sk-svcacct-OAI6Jicdzf3XOPHHwaXvJeIOFwpB5E3hALWSBRxTUpatnD7GVTUb7mPkri83A6T3BlbkFJz-Ry6AyxT6QdvUAEJL7xNjhmVE0055OvJcnIxX8W2u1w3PzLUGRYfQhDsOdnYA")

def handler(event, context):
    try:
        # Parse the data from the request body
        data = json.loads(event['body'])
        theory = data['theory']

        # Generate a response using OpenAI's API
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Provide a summary of the conspiracy theory: {theory}",
            max_tokens=150
        )

        # Extract the result text from the API response
        result = response.choices[0].text.strip()

        # Return the response to the frontend
        return {
            'statusCode': 200,
            'body': json.dumps({'reply': result})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'reply': f"Error: {str(e)}"})
        }
