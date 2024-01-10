import PySimpleGUI as sg
import bcrypt
#from database_handler import
sg.theme('Green')

def hash_password(password):
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

# All the stuff inside your window.
def create_layout_login():
    return [ 
        [sg.Text('Username:'),sg.InputText(key='-USERNAME-')],
        [sg.Text('Password:'), sg.InputText(key='-PASSWORD-')],
        [sg.Button('Login'), sg.Button('Cancel'), sg.Button('Register')]
    ]
def create_layout_logon():
    return [
        [sg.Text('Enter username:'), sg.InputText(key='-NEW_USERNAME-')],
        [sg.Text('Enter email:'), sg.InputText(key='-NEW_EMAIL-')],
        [sg.Text('Enter password'), sg.InputText(key='-NEW_PASSWORD-')],
        [sg.Button('Log on')]
    ]
def create_layout_view():
    return [
        [sg.Text('Add password to storage')],
        [sg.Button('Cancel')]
    ]

layout = create_layout_login()
# Create the Window
window = sg.Window('Password manager', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

    if event == 'Register':
        layout = create_layout_logon()

    if event == 'Login':
        layout = create_layout_view()

    if event == 'Log on':
        layout = create_layout_login()
        #new_username = values['-NEW_USERNAME-']
        #new_email = values['-NEW_EMAIL-']
        #new_password = values['-NEW_PASSWORD-']


    window.close()

    window = sg.Window('Password manager', layout)

    #print('You entered ', values[0] + values[1])

window.close()