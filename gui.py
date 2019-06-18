# Screen Setup

import turtle

window = turtle.Screen()
window.title("Phone Tones")
window.bgcolor("black")
window.bgpic("background.gif")
window.setup(width = 700, height = 700)
window.tracer(0)

# Title

titleText = turtle.Turtle()
titleText.speed(0)
titleText.color("#00ff00")
titleText.penup()
titleText.hideturtle()
titleText.goto(0,300) # Screen Location
titleText.write("DTMF Signalling",  align = "center", font = ("Courier", 28, "normal"))

# Freq Prinout  

freqText = turtle.Turtle()
freqText.speed(0)
freqText.color("#00ff00")
freqText.penup()
freqText.hideturtle()
freqText.goto(0,250) # Screen Location
freqText.write("Press a key to generate the DTMF signal",  align = "center", font = ("Courier", 28, "normal"))

# Tone Printout 

selectedChar = turtle.Turtle()
selectedChar.speed(0)
selectedChar.penup()
selectedChar.hideturtle()
selectedChar.color('#00ff00')
selectedChar.goto(0,-310) # Screen Location