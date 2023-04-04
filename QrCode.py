#MENSAH DORA NAA AYORKOR
#10984530
#BIOMEDICAL ENGINEERING
import PySimpleGUI as sg
import qrcode
import os

sg.theme('BrownBlue')
sg.theme_background_color('black')
font = ('Corbel',18)


qr_image = [sg.Image('',key='-QrCode-')]

layout= [[sg.Text('ENTER URL OR NAME:')],
         [sg.Input('',key = '-Url-')],
         [sg.Column([qr_image],justification= 'center')],
         [sg.Button('Generate',key='-create-',expand_x= True)]]

window = sg.Window('QR CODE GENERATOR',layout,font=font)

   
while True :
    event,values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == '-create-':
        url = values['-Url-']
        if url :
            image = qrcode.make(url)
            image.save('qr.png')
            try:
             window['-QrCode-'].update('qr.png')
             os.remove("qr.png")
            except qrcode.exceptions.DataOverflowError:
                sg.popup_error("Text too long to generate QR code.")
            except Exception as e:
                sg.popup_error(f"Error generating QR code: {e}")
        elif event == sg.WIN_CLOSED or event == "Exit":
            break



window.close()





