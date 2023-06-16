#!/usr/bin/env python

from enum import auto, Enum


class Level(str, Enum):
    PANIC = 'panic'
    FATAL = 'fatal'
    ERROR = 'error'
    WARNING = 'warning'
    INFO = 'info'
    DEBUG = 'debug'
    TRACE = 'trace'

    def __str__(self):
        return self.value


# Create an object.
level = Level('fatal')

if level == Level.FATAL:
    print(f'Level: {level}')

level = Level('error')
print(f'Level is now: {level}')

# If we create an enum with an invalid input, we get an exception.
try:
    level = Level('bad')
except ValueError as err:
    print('Cannot create level with bad')

# Attributes
print(Level.WARNING.name)  # Prints 'WARNING'
print(Level.WARNING.value)  # Prints 'warning'


class State(Enum):
    QUEUED = auto()
    PROCESSING = auto()
    SUCCEEDED = auto()
    FAILED = auto()
    COMPLETED = SUCCEEDED | FAILED

    def __str__(self):
        return self.value


# Iterate through the members.
states = [s.name for s in State]
print(states)

values = [s.value for s in State]
print(values)


# CREDIT: https://docs.python.org/3/howto/enum.html#planet
class Planet(Enum):
    MERCURY = (3.303e+23, 2.4397e6)
    VENUS = (4.869e+24, 6.0518e6)
    EARTH = (5.976e+24, 6.37814e6)
    MARS = (6.421e+23, 3.3972e6)
    JUPITER = (1.9e+27, 7.1492e7)
    SATURN = (5.688e+26, 6.0268e7)
    URANUS = (8.686e+25, 2.5559e7)
    NEPTUNE = (1.024e+26, 2.4746e7)

    def __init__(self, mass, radius):
        self.mass = mass  # in kilograms
        self.radius = radius  # in meters

    @property
    def surface_gravity(self):
        # universal gravitational constant  (m3 kg-1 s-2)
        G = 6.67300E-11
        return G * self.mass / (self.radius * self.radius)


print(Planet.EARTH.value)
print(Planet.EARTH.surface_gravity)
