import PySimpleGUI as sg

# here we'll create 3 functions, each displaying a different 
# screen and after that use them.

# the first 2 functions will return a boolean value to 
# indicate if the next screen should be shown
def show_first_window():

    # first window

    # creating a simple layout
    layout = [
        [sg.Text("Title")],
        [sg.Button("Sign Up"), sg.Button("Cancel")],
    ]

    # creating the window
    window = sg.Window("Sign Up", layout)
    
    # the window loop
    while True:

        # displaying the window and reading its current
        # event and values
        event, values = window.read()

        # if the user pressed cancel or the "X" button 
        # then close the current window and return a False
        # value from the function
        if event == "Cancel" or event == sg.WIN_CLOSED:

            # closing the window
            window.close()
            
            # return a False value
            return False

        elif event == "Sign Up":

            # closing the window
            window.close()

            # retrun a True value
            return True


def show_second_window():

    # second window 
    # the explanation here is the same as the first window 
    layout = [
        [sg.Text("Title")],
        [sg.Button("Login"), sg.Button("Cancel")],
    ]


    window = sg.Window("Login", layout)


    while True:
        event, values = window.read()

        if event == "Cancel" or event == sg.WIN_CLOSED:
            window.close()
            return False
        elif event == "Login":
            window.close()
            return True


def show_alert_window(text):

    # alert window
    layout = [
        [sg.Text(text)],
        [sg.Button("Ok")],
    ]


    window = sg.Window("Login", layout)

    while True:
        event, values = window.read()

        if event == "Ok" or event == sg.WIN_CLOSED:
            break
    



#------------------------------------------------------------
#  the program starts from here!!!

# show the first window and waiting for the function to return
# a boolean value that indicates if we should show the second 
# screen
show_second = show_first_window()

# checking if we should show the second screen
if show_second == True:

    # same process we did for the first screen
    show_alert = show_second_window()

    # checking if we should show the alert
    if show_alert == True:
        # showing the alert and inserting a text of our choice
        # to display
        show_alert_window("Success!")