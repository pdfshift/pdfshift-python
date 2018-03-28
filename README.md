PDFShift Python Package
=======================

This Python package provides a simplified way to interact with the [PDFShift](https://pdfshift.io) API.

## Documentation

See the full documentation on [PDFShift's documentation](https://pdfshift.io/documentation).

## Installation

You should not require this code directly. Instead, just run:

    pip install --upgrade pdfshift

or

    easy_install --upgrade pdfshift


### Requirements

* Python 2.6+
* [Requests](http://docs.python-requests.org/en/master/)

## Usage

This library needs to be configured with your `api_key` received when creating an account.
Setting it is easy as:

```python
import pdfshift
pdfshift.api_key = '120d8e8a86d2....................'
```

### Basic example

#### With an URL

```python
import pdfshift
pdfshift.api_key = '120d8e8a86d2....................'

binary_file = pdfshift.convert('https://www.example.com')

with open('result.pdf', 'wb') as output:
    output.write(binary_file)
```

#### With inline HTML data:

```python
import pdfshift
pdfshift.api_key = '120d8e8a86d2....................'

document = open('page.html', 'r')
document_content = document.read()
document.close()

binary_file = pdfshift.convert(document_content)
with open('result.pdf', 'wb') as output:
    output.write(binary_file)
```

### Custom CSS

#### Loading CSS from an URL:

```python
import pdfshift
pdfshift.api_key = '120d8e8a86d2....................'

binary_file = pdfshift.convert(
    'https://www.example.com',
    css="https://www.example.com/public/css/print.css"
)

with open('result.pdf', 'wb') as output:
    output.write(binary_file)
```

#### Loading CSS from a string:

```python
import pdfshift
pdfshift.api_key = '120d8e8a86d2....................'

binary_file = pdfshift.convert(
    'https://www.example.com',
    css="a {text-decoration: underline; color: blue}"
)

with open('result.pdf', 'wb') as output:
    output.write(binary_file)
```

### Custom HTTP Headers

```python
import pdfshift
pdfshift.api_key = '120d8e8a86d2....................'

binary_file = pdfshift.convert(
    'https://httpbin.org/headers',
    headers={
        'X-Original-Header': 'Awesome value',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
    }
)

with open('result.pdf', 'wb') as output:
    output.write(binary_file)
```

### Accessing secured pages

```python
import pdfshift
pdfshift.api_key = '120d8e8a86d2....................'

binary_file = pdfshift.convert('https://httpbin.org/basic-auth/user/passwd', auth=('user', 'passwd'))

with open('result.pdf', 'wb') as output:
    output.write(binary_file)
```

### Using cookies

```python
import pdfshift
pdfshift.api_key = '120d8e8a86d2....................'

binary_file = pdfshift.convert(
    'https://httpbin.org/cookies',
    cookies=[
        {'name': 'session', 'value': '4cb496a8-a3eb-4a7e-a704-f993cb6a4dac'}
    ]
)

with open('result.pdf', 'wb') as output:
    output.write(binary_file)
```

### Adding Watermark (Oh hi Mark!)

```python
import pdfshift
pdfshift.api_key = '120d8e8a86d2....................'

binary_file = pdfshift.convert(
    'https://www.example.com',
    watermark={
        'source': 'https://pdfshift.io/static/static/img/logo.png',
        'offset_x': 50,
        'offset_y': '100',
        'rotate': 45
    }
)

with open('result.pdf', 'wb') as output:
    output.write(binary_file)
```

### Custom Header (or Footer)

```python
import pdfshift
pdfshift.api_key = '120d8e8a86d2....................'

binary_file = pdfshift.convert(
    'https://www.example.com',
    footer={
        'source': '<div>Page {{page}} of {{total}}</div>',
        'spacing': '50px'
    }
)

with open('result.pdf', 'wb') as output:
    output.write(binary_file)
```

### Protecting the generated PDF

```python
import pdfshift
pdfshift.api_key = '120d8e8a86d2....................'

binary_file = pdfshift.convert(
    'https://www.example.com',
    protection={
        'encrypt': 128,
        'user_password': 'user',
        'owner_password': 'owner',
        'no_print': True
    }
)

with open('result.pdf', 'wb') as output:
    output.write(binary_file)
```
