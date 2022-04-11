from ursina import *

game=Ursina()
block=Entity(model='toilet.obj', scale=0.03, texture="white_cube")
block.rotation_x=16
def update():
    block.rotation_y=block.rotation_y+18
game.run()