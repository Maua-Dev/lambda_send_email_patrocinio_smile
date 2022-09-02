def generate_html(name):
    return f"""
    <html>
        <head></head>
        <body>
          <h1>Olá {name}</h1>
          <p>This email was sent with
            <a href='https://aws.amazon.com/ses/'>Amazon SES</a> using the
            <a href='https://aws.amazon.com/sdk-for-python/'>
              AWS SDK for Python (Boto)</a>.</p>
        </body>
    </html>
    """