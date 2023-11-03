from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    question_text = self.ask_question.text
    input_text = self.input_text.text
    #call the function from jupyter
    res = anvil.server.call('answer_question',question_text, input_text)
    self.answer.content = res
    self.answer.format ='markdown'


  
  
    
    
