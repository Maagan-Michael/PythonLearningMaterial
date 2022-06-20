import PySimpleGUI as sg

#creating the layout
layout = [
    # title
    [sg.Text('My Window')],
    # Multiline element:

    # 1. with a size of (width=50, height=15),

    # 2. with a key that equals to '-multi-'
    
    # 3.the named parameter 'reroute_cprint' means that all calls of 'sg.cprint' (as shown below)
    # will be rerouted and outputed to this multiline.

    [sg.Multiline('', size=(50, 15), reroute_cprint=True, key='-multi-')],

    #buttons
    [sg.Button('left' ),sg.Button('center') ,sg.Button('right'), sg.Button('Exit')]
]

#creating the window
window = sg.Window('Window Title', layout) 

# window loop
while True:
    # displaying the window and reading the current event and values
    event, values = window.read()

    # closing the window
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    
    # how to use sg.cprint():
    # 1. put any number of strings with a comma(,) between them. 
    #   all of the strings will be displayed with a space between them by default
    
    # 2. use the any or none of the named parameters. a list of all of them can
    #    be view by clicking on cprint while pressing ctrl.

    # for example the named parameter "justification" can set the alignment of the text.
    # justification='l' sets the text aligment to the left
    # justification='c' sets the text aligment to the center
    # justification='r' sets the text aligment to the right



    # calling cprint which will be rerouted to the multiline element beacause 'reroute_cprint=True' was called
    #
    elif event == 'left':
        sg.cprint('Dan: ', 'hey there', 'how are you?', justification='l')

    elif event == 'center':
        sg.cprint(':D', justification='c')

    elif event == 'right':
        sg.cprint('hey there', ' :Nadav', justification='r')
