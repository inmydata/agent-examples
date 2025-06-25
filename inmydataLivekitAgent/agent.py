import asyncio
from prompts import INSTRUCTIONS, ASKING_QUESTION_MESSAGE, DELAY_MESSAGE, INFORM_USER_MESSAGE
from inmydata.ConversationalData import ConversationalDataDriver
from livekit.agents.llm import function_tool
from livekit.agents import Agent

class Assistant(Agent):

    
    def __init__(self) -> None:
        self.delay_task_seconds = 20
        self.driver = ConversationalDataDriver("demo")
        self.driver.on("ai_question_update", self.on_ai_question_update) 
        self.delay_task = None
        self.subject = None
        super().__init__(instructions=INSTRUCTIONS)

    @function_tool
    async def ask_question(self, question: str):
        print(f"ask_question - question: {question}")
        self.session.generate_reply(instructions=ASKING_QUESTION_MESSAGE(question))
        self.delay_message_read = False
        self.start_delay_task()
        result = await self.driver.get_answer(question, subject=self.subject)
        self.cancel_delay_task()
        if result is None:
            await self.session.generate_reply(instructions="Inform the user: Question could not be answered")        
            return
        else:
            self.subject = result.subject
        self._answer = {
            await self.session.generate_reply(instructions="Give the user the following answer :" + result.answer)
        } 

    @function_tool
    async def reset_conversation_context(self):
        self.subject = None

    def on_ai_question_update(self, caller, message):  
        self.session._loop.create_task(self.generate_reply(message))
    
    async def generate_reply(self, message):
        print ("generating reply: " + message)   
        self.cancel_delay_task()
        await self.session.say(message)
        if self.delay_message_read == False: # Only want the delay message once
            self.start_delay_task()
        
    def start_delay_task(self):
        self.cancel_delay_task()
        self.delay_task = asyncio.create_task(self.speak_status_update())
    
    def cancel_delay_task(self):
        if self.delay_task is not None:
            self.delay_task.cancel()
            self.delay_task = None

    async def speak_status_update(self):
        await asyncio.sleep(self.delay_task_seconds)
        self.delay_message_read = True
        await self.session.generate_reply(instructions=DELAY_MESSAGE)