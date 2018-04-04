# -*- coding: utf-8 -*-

# __/\\\\\\\\\\\\\____/\\\\\\\\\\\\_____/\\\\\\\\\\\\\\\___/\\\\\\\\\\\____/\\\______________________/\\\\\______________________
# __\/\\\/////////\\\_\/\\\////////\\\__\/\\\///////////__/\\\/////////\\\_\/\\\____________________/\\\///______________________
# ___\/\\\_______\/\\\_\/\\\______\//\\\_\/\\\____________\//\\\______\///__\/\\\__________/\\\_____/\\\_________/\\\____________
# ____\/\\\\\\\\\\\\\/__\/\\\_______\/\\\_\/\\\\\\\\\\\_____\////\\\_________\/\\\_________\///___/\\\\\\\\\___/\\\\\\\\\\\______
# _____\/\\\/////////____\/\\\_______\/\\\_\/\\\///////_________\////\\\______\/\\\\\\\\\\___/\\\_\////\\\//___\////\\\////______
# ______\/\\\_____________\/\\\_______\/\\\_\/\\\___________________\////\\\___\/\\\/////\\\_\/\\\____\/\\\________\/\\\_________
# _______\/\\\_____________\/\\\_______/\\\__\/\\\____________/\\\______\//\\\__\/\\\___\/\\\_\/\\\____\/\\\________\/\\\_/\\____
# ________\/\\\_____________\/\\\\\\\\\\\\/___\/\\\___________\///\\\\\\\\\\\/___\/\\\___\/\\\_\/\\\____\/\\\________\//\\\\\____
# _________\///______________\////////////_____\///______________\///////////_____\///____\///__\///_____\///__________\/////____

"""
Convert HTML documents to PDF using the PDFShift.io API.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Usage:

    >>> import pdfshift
    >>> pdfshift.api_key = '120d8e8a86d24c6daa604a9c14fd7c7f'
    >>> binary_file = pdfshift.convert('https://www.example.com')
    >>> with open('result.pdf', 'wb') as output:
    >>>     output.write(binary_file)

`convert` function allows for many parameters.

You can check a description of each of them on the documentation at:
https://pdfshift.io/documentation
"""

import requests
from pdfshift import errors


api_key = None
api_base = 'https://api.pdfshift.io/v2'


def _parse_response(response):
    body = None
    try:
        body = response.json()
    except ValueError:
        raise errors.PDFShiftException(
            'Invalid response from the server.',
            500
        )

    if response.status_code == 200:
        return body

    if response.status_code == 429:
        raise errors.RateLimitException(response)

    if body.get('code') == 400:
        if body.get('message', None):
            raise errors.InvalidRequestException(body.get('error'))

        raise errors.InvalidRequestException(body.get('errors'))

    if str(body.get('code')) in errors.codes:
        raise getattr(errors, errors.codes.get(str(body['code'])))()

    raise errors.PDFShiftException('An unknown error occured.', 500)


def convert(source, **kwargs):
    """
    Convert any given HTML element (URL or data) to PDF using PDFShift.io API
    ~
    We rely on the API to let us know if a parameter is not accepted.
    The reason for this is to allow the current code to work even when the
    API get new features :)
    """

    if api_key is None:
        raise errors.InvalidApiKeyException()

    if kwargs is None:
        kwargs = {}

    if 'auth' in kwargs and isinstance(kwargs['auth'], list):
        kwargs['auth'] = {
            'username': kwargs['auth'][0],
            'password': kwargs['auth'][1] if len(kwargs['auth']) > 1 else None
        }

    kwargs['source'] = source
    response = requests.post(
        '{0}/convert/'.format(api_base),
        auth=(api_key, ''),
        json=kwargs
    )

    body = _parse_response(response)
    return body.get('content').decode('base64')


def remaining_credits():
    """
    Returns the number of remaining credist for this account
    """

    if api_key is None:
        raise errors.InvalidApiKeyException()

    response = requests.get(
        '{0}/credits/'.format(api_base),
        auth=(api_key, '')
    )

    body = _parse_response(response)
    return body.get('remaining')
