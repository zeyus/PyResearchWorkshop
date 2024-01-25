# Stimuli and Responses in PsychoPy

In this section we will cover some of the different types of stimuli and responses that we can use in PsychoPy. For more details about the different stimuli and responses, you can check out the [PsychoPy Documentation](https://psychopy.org/api/index.html).

## Stimuli

All of the following stimuli can be used as part of an experiment, and of course you can control completely when and how they are presented. Most of them support various options such as the size, position, and colour of the stimulus.

### Text

The [`TextStim`](https://psychopy.org/api/visual/textstim.html#psychopy.visual.TextStim) class can be used to present text on the screen. You can use this to present instructions, or to present a question to the participant.

```python
# Create a text stimulus
text_stim = visual.TextStim(win, text="Hello World!")

# Draw the text stimulus
text_stim.draw()

# Flip the window to display the stimulus
win.flip()
```

### Images

The [`ImageStim`](https://psychopy.org/api/visual/imagestim.html#psychopy.visual.ImageStim) class can be used to present images on the screen. You can use this to present images that you have created, or to present images that you have loaded from a file.

```python
# Create an image stimulus
image_stim = visual.ImageStim(win, image="path/to/image.png")

# Draw the image stimulus
image_stim.draw()

# Flip the window to display the stimulus
win.flip()
```

### Shapes

The [`ShapeStim`](https://psychopy.org/api/visual/shapestim.html#psychopy.visual.ShapeStim) class can be used to present shapes on the screen. You can use this to present shapes that you have created, or to present shapes that you have loaded from a file.

```python
# Create a shape stimulus
shape_stim = visual.ShapeStim(win, vertices=[(-0.5, -0.5), (0.5, -0.5), (0, 0.5)])

# Draw the shape stimulus
shape_stim.draw()

# Flip the window to display the stimulus
win.flip()
```

Of course, often we may want to use simple shapes such as rectangles, circles, and polygons. For this, we can use the [`Rect`](https://psychopy.org/api/visual/rect.html#psychopy.visual.Rect), [`Circle`](https://psychopy.org/api/visual/circle.html#psychopy.visual.Circle), and [`Polygon`](https://psychopy.org/api/visual/polygon.html#psychopy.visual.Polygon), [`Line`](https://psychopy.org/api/visual/line.html#psychopy.visual.Line) and [`pie`](https://psychopy.org/api/visual/pie.html#psychopy.visual.Pie) classes.

```python
# Create a rectangle stimulus
rect_stim = visual.Rect(win, width=0.5, height=0.5)

# create a circle stimulus
circle_stim = visual.Circle(win, radius=0.5)

# create a polygon stimulus
polygon_stim = visual.Polygon(win, edges=3)

# create a line stimulus
line_stim = visual.Line(win, start=(-0.5, -0.5), end=(0.5, 0.5))

# create a pie stimulus
pie_stim = visual.Pie(win, edges=3, radius=0.5, startAngle=0, endAngle=90)
```

### Sounds

The [`Sound`](https://psychopy.org/api/sound/playback.html#soundclasses) class can be used to present sounds. You can use this to present sounds that you have created, or to present sounds that you have loaded from a file.

```python
# Create a sound stimulus
sound_stim = sound.Sound("A") # Play the note A (440 Hz)

# Play the sound stimulus
sound_stim.play()

# The sound can also be a file
sound_stim = sound.Sound("path/to/sound.wav")

# Play the sound stimulus
sound_stim.play()

# playing sounds have various propertis we can check
print(sound_stim.isPlaying) # True if the sound is currently playing
print(sound_stim.isFinished) # True if the sound has finished playing

# We can also stop the sound
sound_stim.stop()
```

### Movies

Movies can be presented using the `MovieStim` class. You can use this to present movies that you have created, or to present movies that you have loaded from a file.

```python
# Create a movie stimulus
movie_stim = visual.MovieStim(win, "path/to/movie.mp4")

# Play the movie stimulus
movie_stim.play()
```

## Responses

You're able to capture a broad range of responses from participants using PsychoPy. We will cover some of the most common response types here.

### Keyboard

The [`Keyboard`](https://psychopy.org/api/hardware/keyboard.html#psychopy.hardware.keyboard.Keyboard) class can be used to capture keyboard responses. You can use this to capture responses from the participant, such as their answer to a question.

```python
# Create a keyboard
keyboard = keyboard.Keyboard()

# Wait for a response, this blocks everything else until a response is received
response = keyboard.waitKeys()

# Check if the response was correct
if response[0].name == "space":
    print("Correct!")
else:
    print("Incorrect!")

# We can also check if a key is currently pressed
if keyboard.isPressed("space"):
    print("Space is pressed!")

```

Alternatively, as used in the template, you can use the [`event.getKeys`](https://psychopy.org/api/event.html) method to check for responses without blocking the rest of the experiment.

```python
# Check for responses
response = event.getKeys()

# Check if the response was correct
if response[0].name == "space":
    print("Correct!")
else:
    print("Incorrect!")

```

### Mouse

Mouse responses can be captured using [`event.Mouse`](https://psychopy.org/api/event.html). You can use this to capture responses from the participant, such as their answer to a question.

```python
mouse = event.Mouse(win=win)

# Wait for a response, this blocks everything else until a response is received
while True:
    pressed = mouse.getPressed()
    if pressed[0]: # Check if the left mouse button is pressed, middle and right are 1 and 2 respectively
        break
```

You can also get the mouse position at any time using `mouse.getPos()`.

```python
# Get the mouse position
mouse_pos = mouse.getPos()
```


### Rating Scale

The [`RatingScale`](https://psychopy.org/api/visual/ratingscale.html#psychopy.visual.RatingScale) class can be used to get a rating from the participant.

```python
# Create a rating scale
rating_scale = visual.RatingScale(win, choices=["1", "2", "3", "4", "5"], markerStart=3)

# Draw the rating scale
rating_scale.draw()

while rating_scale.noResponse: # Wait for a response
    # other stimuli etc
    # ...
    ratingScale.draw()
    win.flip()

# Get the response
response = rating_scale.getRating()
reaction_time = rating_scale.getRT()
history = rating_scale.getHistory()
```


### Slider

The [`Slider`](https://psychopy.org/api/visual/slider.html#psychopy.visual.Slider) class can be used to get a rating from the participant.

```python
# Create a slider
slider = visual.Slider(win, ticks=(1, 2, 3, 4, 5), granularity=0.01, marker="triangle", markerStart=3)

# Draw the slider
slider.draw()

while slider.noResponse: # Wait for a response
    # other stimuli etc
    # ...
    slider.draw()
    win.flip()

# Get the response
response = slider.getRating()
reaction_time = slider.getRT()
history = slider.getHistory()
```


## Other I/O

Psychopy also has some other useful I/O features that we can use in our experiments. We will not cover these in detail, but you can read more about them in the [PsychoPy Documentation](https://psychopy.org/api/iohub/index.html). These include:

* Eye tracking
* EEG
* Parallel port
* Serial port
* Microphone
* LSL

And more...