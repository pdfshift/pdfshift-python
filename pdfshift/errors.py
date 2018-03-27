# -*- coding: utf-8 -*-

import time

codes = {
    'A401': 'InvalidApiKeyException',
    'A403': 'NoCreditsException',
    'S001': 'ServerException'
}


class PDFShiftException(Exception):
    """
    Root exception class, useful if you want a "catch-all" except block.
    """
    def __init__(self, message=None, code=None):
        super(PDFShiftException, self).__init__(message, code)
        self.message = message
        self.code = code

    def __str__(self):
        return u'{0} - {1}'.format(self.code, self.message)


# Already filled exception classes

class InvalidApiKeyException(PDFShiftException):
    def __init__(self):
        super(InvalidApiKeyException, self).__init__(
            'Please indicate a valid API Key.',
            'A401'
        )


class NoCreditsException(PDFShiftException):
    def __init__(self):
        super(NoCreditsException, self).__init__(
            'No remaining credits left.',
            'A403'
        )


class ServerException(PDFShiftException):
    def __init__(self):
        super(ServerException, self).__init__(
            'A fatal error occured.',
            'S001'
        )


# Custom exception classes

class RateLimitException(PDFShiftException):
    def __init__(self, response):
        super(RateLimitException, self).__init__(
            'You have been rate limited.',
            'R429'
        )

        self.reset = int(response.headers.get('X-RateLimit-Reset')) - time.time()

    def wait(self):
        time.sleep(self.reset)


class InvalidRequestException(PDFShiftException):
    def __init__(self, message=None):
        self.errors = None
        if isinstance(message, dict):
            self.errors = message
            items = ['\n']
            for k in message:
                if isinstance(message[k], list):
                    items.append('  * {0}: {1}'.format(k, ', '.join(message[k])))
                else:
                    items.append('  * {0}: {1}'.format(k, message[k]))
            message = '\n'.join(items)

        super(InvalidRequestException, self).__init__(message, 'R400')

    def get_errors(self):
        return self.errors
