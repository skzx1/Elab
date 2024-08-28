'''Write a program to check username and password for accessing computer system with admin account.

The admin account is "Username=admin" and "Password=Ad31n15Tr@t012".

Use constant variable ADMIN_USERNAME and ADMIN_PASSWORD when you check username and password

โปรแกรมที่เขียนต้องเทียบค่ากับตัวแปรที่กำหนดให้ และไม่เปลี่ยนค่าของตัวแปรที่กำหนดให้ไว้แล้ว

Example 1
Username: admin
Password: Ad31n15Tr@t012
Welcome, admin.
Example 2
Username: admin
Password: 123456
You are not admin.
Example 3
Username: Admin
Password: Ad31n15Tr@t012
You are not admin.'''
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'Ad31n15Tr@t012'

username = input("Username: ")
password = input("Password: ")
if ADMIN_USERNAME == username and ADMIN_PASSWORD == password:
    print('Welcome, admin.')
else:
    print('You are not admin.')