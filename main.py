def on_button_pressed_a():
    basic.show_icon(IconNames.SMALL_SQUARE)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_leds("""
        # # # # #
        . . # . .
        . . # . .
        . . # . .
        # # # # #
        """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_icon(IconNames.HEART)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    basic.show_number(input.temperature())
    if input.temperature() > 31:
        basic.show_string("hot")
    else:
        basic.show_string("cold")
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
