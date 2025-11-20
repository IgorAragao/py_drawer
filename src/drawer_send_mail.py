import random
import smtplib
from email.message import EmailMessage
from user_map import people # mapping of names and emails
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def conn_email():
    try:
        email_server = smtplib.SMTP('smtp.gmail.com', 587)
        email_server.starttls()
        email_server.login('add_sender_email', 'add_password') # add mail gmail
        return email_server
    except Exception as err:
        print(f"[ERROR] ❌ {err}")
        return None


def conn_close(conn):
    if conn is None:
        print("[ERROR] ❌ Email connection not established!")
    else:
        print("[INFO] Emails sent and connection closed!")
        conn.quit()


def send_mail(email_server, dest, name):
    msg = MIMEMultipart()
    msg['From'] = 'add_sender_email'
    msg['To'] = dest
    msg['Subject'] = 'add_subject'

    # message body -- add your messagem below, between <body> and </body>
    html = """ 
    <html>
    <body>

    Add your message here!!
    <br>
    <br>
    Your secret friend is: <b>"""+name+"""</b>

    </body>
    </html>
    """
    
    msg_html = MIMEText(html, 'html')
    msg.attach(msg_html)

    email_server.sendmail(msg['From'], dest, msg.as_string())


def sort_names():
    p = people
    random.shuffle(p)

    return p


def drawer():
    conn = conn_email()

    try:

        if conn != None:
            people_sort = sort_names()

            i = 0
            while i < len(people_sort):
                if i == len(people_sort) - 1 :
                    send_mail(conn, people_sort[i]["email"], people_sort[0]["name"])
                else:
                    send_mail(conn, people_sort[i]["email"], people_sort[i+1]["name"])
                i = i + 1
        else:
            exit()

    except Exception as err:
        print(f"[ERROR] ❌ Failed to send email: {err}")

    finally:
        conn_close(conn)


def main():
    drawer()


if __name__ == "__main__":
    main()