import re


class ResultReporter:
    """
    Every test report class is a sub class of ResultReporter
    """

    def __init__(self, coala_json):
        self.coala_json = coala_json

    @staticmethod
    def sanitize(error_message):
        """
        Remove escape characters from the error message

        :param: string that contains escape characters
        :return: string with replaced escape characters
        """
        mapping = {'&': '&amp;', '\"': '&quot;',
                   '<': '&lt;', '>': '&gt;'}
        for k, v in mapping.items():
            error_message = error_message.replace(k, v)
        return error_message

    @staticmethod
    def extract_error_code(error_message):
        """
        Return error code from error message or the message itself if
        no error code is found
        """
        try:
            return re.search('[A-Z][0-9]{3,4}', error_message).group()
        except AttributeError:
            return error_message
