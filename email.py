#!/usr/bin/python3
import smtplib

s=smtplib.SMTP('smtp.gmail.com',587)

s.starttls()

s.login("patharetanmay1018@gmail.com","***********")

subject1 = 'Important'

message1 = "Your code has been failed, please debug it asap."

s.sendmail("patharetanmay1018@gmail.com",message1)

s.quit()
