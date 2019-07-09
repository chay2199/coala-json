from coala_json.loader.JsonLoader import JsonLoader


class coalaJsonLoader(JsonLoader):
    """
    Contains method to extract data from coala-json
    """

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
    def extract_message(problem):
        return coalaJsonLoader.sanitize(problem['message'])

    @staticmethod
    def extract_raw_message(problem):
        return problem['message']

    @staticmethod
    def extract_affected_line(problem):
        if problem['affected_code']:
            return problem['affected_code'][0]['end']['line']

    @staticmethod
    def extract_affected_column(problem):
        if problem['affected_code']:
            return problem['affected_code'][0]['end']['column']

    @staticmethod
    def extract_file(problem):
        if problem['affected_code']:
            return problem['affected_code'][0]['file']

    @staticmethod
    def extract_origin(problem):
        return problem['origin'].split(" ")[0]

    @staticmethod
    def extract_severity(problem):
        return problem['severity']

    @staticmethod
    def extract_errors(problems):
        return len(problems)
