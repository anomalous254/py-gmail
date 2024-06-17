[![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](https://opensource.org/licenses/MIT)


# pygmail

### Description

This is an unofficial python module providing convenient way of sending emails using gmail smtp services

It has been tested with Python  3 >

### Setup and Installation

```Bash
pip install pygmail
```

### Usage

``` python
from pygmail.send_email import Pygmail

pygmail = Pygmail(
        smtp_username="your_email@gmail.com",
        app_password="your gmail app password"
    )

# Email details
    sender_email = "your_email@gmail.com"
    receiver_email = "receiver_email@example.com"
    subject = "Welcome to Our Service"
    template_path = "email_template.html path"
    context = {
        "name": "John Doe",
        "action_url": "https://example.com/get-started"
    }

# Send the email
result = pygmail.send_email(sender_email, receiver_email, subject, template_path, context)
print(result) # "email sent successfully." || 'email not sent!'


```

### Dependencies






