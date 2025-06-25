import os

from dotenv import load_dotenv
from inmydata.ConversationalData import ConversationalDataDriver
import asyncio

load_dotenv()

# get_answer is an async function, so we need to run it in an event loop
async def main():
    driver = ConversationalDataDriver(os.environ['INMYDATA_TENANT'])

    # Register a callback to handle AI question updates
    def on_ai_question_update(caller, message):  
        print(message)

    # Register the callback handler for AI question updates
    driver.on("ai_question_update", on_ai_question_update) 

    question = "Give me the top 10 stores this year"
    answer = await driver.get_answer(question)
    
    print("=================================================================")
    print(f"The answer was: {answer.answer}")
    print(f"The subject used to generate the answer was: {answer.subject}")


asyncio.run(main())
