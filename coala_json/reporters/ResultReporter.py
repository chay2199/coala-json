import re

from coala_json.loader.coalaJsonLoader import coalaJsonLoader


class ResultReporter:
    """
    Every test report class is a sub class of ResultReporter
    """

    def __init__(self, loader: coalaJsonLoader, coala_json):
        self.loader = loader
        self.coala_json = coala_json

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
