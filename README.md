PDFShift Python Package
=======================

*Convert HTML documents to PDF using the PDFShift.io API.*

Usage:

    >>> import pdfshift
    >>> pdfshift.api_key = '120d8e8a86d24c6daa604a9c14fd7c7f'
    >>> binary_file = pdfshift.convert('https://www.example.com')
    >>> with open('result.pdf', 'wb') as output:
    >>>     output.write(binary_file)

`convert` function allows for many parameters.
You can check a description of each of them on the documentation at:
https://pdfshift.io/documentation
