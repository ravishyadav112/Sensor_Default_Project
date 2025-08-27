import sys 

def error_message_detail(error, error_details:sys):
    _,_,exc_tb = error_details.exc_info()  #exc_info() returns 3 things: type, value, traceback. Traceback is key to knowing which file and line caused the error. Here we only need traceback (exc_tb) to know where the error occurred.That's why we left the first two spaces
    file_name = exc_tb.tb_frame.f_code.co_filename #It gives the name of the Python file where the error occurred
    error_message = "Error occured python Scripts name [{0}] line number [{1}] error_message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error) #exc_tb.tb_lineno gets the line number where the error happened.
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error_message , error_details:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(
            error_message,error_details = error_details
        )
    def __str__(self):    #__str__ ensures that when you print this exception, it shows your detailed message instead of default error.
        return self.error_message
    







    