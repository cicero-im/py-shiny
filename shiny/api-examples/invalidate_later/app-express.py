
from shiny import reactive
from shiny.express import render
import secrets


@render.text
def value():
    reactive.invalidate_later(0.5)
    return "Random int: " + str(secrets.SystemRandom().randint(0, 10000))
