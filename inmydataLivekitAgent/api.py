from livekit.agents import llm
import enum
from typing import Annotated
import logging
from inmydataDriver import inmydataDriver
from documentDriver import documentDriver

logger = logging.getLogger("user-data")
logger.setLevel(logging.INFO)

#d = inmydataDriver("demo", "test-inmydata.com")
#dd = documentDriver()

class Answer (enum.Enum):
    Answer = "answer"

class DocumentAnswer (enum.Enum):
    DocumentAnswer= "documentanswer"    
    
class AssistantFnc(llm.FunctionContext):
    def __init__(self, inmydata_driver, document_driver):
        super().__init__()

        self.d = inmydata_driver
        self.dd = document_driver
        
        self._answer = {
            Answer.Answer: ""
        }

        self._documentanswer = {
            DocumentAnswer.DocumentAnswer: ""
        }

    def get_answer_str(self):        
        return self._answer

    def get_document_answer_str(self):        
        return self._documentanswer

    @llm.ai_callable(description="asks a question about the data in a database table and gets an answer")
    def ask_question(self, question: Annotated[str, llm.TypeInfo(description="The question about the data in the database table")]):
        logger.info("ask_question - question: %s", question)
        
        result = self.d.query_for_answer(question)
        if result is None:
            return "Question could not be answered"        
        self._answer = {
            Answer.Answer: result
        }        
        return f"The answer is: {self.get_answer_str}"
    
    @llm.ai_callable(description="gets the answer to the question asked about the data in a database table")
    def get_answer(self):
        logger.info("get_answer")
        return f"The answer is: {self.get_answer_str()}"
    
    def has_answer(self):
        return self._answer[Answer.Answer] != ""

    @llm.ai_callable(description="asks a question about a knowledge document about external factors impacting jewellery sales over the next few months and gets an answer")
    def ask_document_question(self, question: Annotated[str, llm.TypeInfo(description="The question about a knowledge document about external factors impacting jewellery sales over the next few months and gets an answer")]):
        logger.info("ask_document_question - question: %s", question)
        result = self.dd.getDocumentAnswer("demo.txt",question)
        if result is None:
            return "Document question could not be answered"        
        self._documentanswer = {
            DocumentAnswer.DocumentAnswer: result
        }        
        return f"The document answer is: {self.get_document_answer_str}"

    @llm.ai_callable(description="gets the answer to the question asked about the knowledge document about external factors impacting jewellery sales over the next few months")
    def get_document_answer(self):
        logger.info("get_document_answer")
        return f"The answer is: {self.get_document_answer_str()}"
    
    def has_document_answer(self):
        return self._documentanswer[DocumentAnswer.DocumentAnswer] != ""