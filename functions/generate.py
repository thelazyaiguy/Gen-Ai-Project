import json
import openai
import os

# Set up your OpenAI API key
openai.api_key = "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"

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
