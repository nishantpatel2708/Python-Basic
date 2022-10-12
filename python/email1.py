import smtplib
conn=smtplib.SMTP('smtp.gmail.com',587)
conn.ehlo()
conn.starttls()
conn.login('vrajgandhi13112000@gmail.com','vraj@1311')
conn.sendmail('vrajgandhi13112000@gmail.com','vrajgandhi13112000@gmail.com','this is testing')
conn.quit()