import sys
import logging

# Configure logging
logging.basicConfig(
    filename="error.log",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

def error_message_details(error, error_detail: sys):
    '''
    This function generates a detailed error message including
    the file name, line number, and the error message.
    '''
    _, _, exc_tb = error_detail.exc_info()  # Correctly unpack the traceback info
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        '''
        Custom exception class that formats detailed error messages.
        '''
        super().__init__(error_message)  # Correct usage of super().__init__()
        self.error_message = error_message_details(error_message, error_detail)

    def __str__(self):
        '''
        Override the string representation of the exception.
        '''
        return self.error_message

'''
if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Devide by Zero error")  # Log a generic info message
        logging.error(str(CustomException(e, sys)))  # Log the detailed custom exception
        raise CustomException(e, sys)  # Raise the custom exception
'''