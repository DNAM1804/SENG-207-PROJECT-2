#MENSAH DORA NAA AYORKOR
#10984530
#BIOMEDICAL ENGINEERING
import PySimpleGUI as sg
import pyttsx3

layout = [[sg.Text('ENTER TEXT THAT WILL BE SPOKEN: ',text_color='white'), sg.Input(key='-input-')],
          [sg.Column([[sg.Radio('Voice of Male', 'voice', key='-Male-', default=True,background_color='black'), sg.Radio('Voice of Female', 'voice', key='-Female-',background_color='black')]], element_justification='c')],
          [sg.Button('Speak'), sg.Button('Close'),]]

window = sg.Window('TEXT TO SPEECH', layout,background_color='blue')
mytts_engine = pyttsx3.init()

def voice_text(text, diff_voice):
    voices = mytts_engine.getProperty('voices')
    if diff_voice == 'male':
        mytts_engine.setProperty('voice', voices[0].id)
    else:
        mytts_engine.setProperty('voice', voices[1].id)
    mytts_engine.say(text)
    mytts_engine.runAndWait()

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Close'):
        break
    elif event == 'Speak':
        text = values['-input-']
        if values['-Male-']:
            voice_text(text, 'male')
        else:
            voice_text(text, 'female')

window.close()
