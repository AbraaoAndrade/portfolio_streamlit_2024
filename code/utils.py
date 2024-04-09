
def send_email(sender, password, receiver, smtp_server, smtp_port, email_message, subject, attachment=None):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.header import Header
    from email.mime.application import MIMEApplication

    message = MIMEMultipart()
    message['To'] = Header(receiver)
    message['From']  = Header(sender)
    message['Subject'] = Header(subject)
    message.attach(MIMEText(email_message,'plain', 'utf-8'))
    if attachment:
        att = MIMEApplication(attachment.read(), _subtype="txt")
        att.add_header('Content-Disposition', 'attachment', filename=attachment.name)
        message.attach(att)

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.ehlo()
    server.login(sender, password)
    text = message.as_string()
    server.sendmail(sender, receiver, text)
    server.quit()

    return True

def nav_to(url):
    # import streamlit as st
    
    # nav_script = """
    #     <meta http-equiv="refresh" content="0; url='%s'">
    # """ % (url)
    
    # st.write(nav_script, unsafe_allow_html=True)

    import webbrowser
    webbrowser.open(url) 

def trigger_download(data, filename) -> str:
    import base64
    b64 = base64.b64encode(data).decode()
    dl_link = f"""
                <html>
                <head>
                <script src="http://code.jquery.com/jquery-3.2.1.min.js"></script>
                <script>
                $('<a href="data:application/octet-stream;base64,{b64}" download="{filename}">')[0].click()
                </script>
                </head>
                </html>"""
    return dl_link

def download_cv() -> None:
    import streamlit.components.v1 as components

    with open("./data/CV_abraao_andrade_2024.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    trigger = trigger_download(PDFbyte, "abraao_andrade_cv_2024.pdf")
    components.html(html=trigger, height=0, width=0)
    return
