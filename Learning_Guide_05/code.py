#!/usr/bin/env python3
"""
Created by: Justin Lavoie
Created on: Dec 2023
This program is the "Space Aliens" program on the PyBadge
"""


import stage
import ugame
import constants

def game_scene() -> None:
    """
    This function is the main game game_scene.
    """
    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # set the background to image in the image bank and the size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, 10, 8)

    # a sprite that will be updated every frame
    ship = stage.Sprite(
        image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE)
    )

    # create a stage for the background to show up on and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)

    # set the layers of all sprites, items show up in order
    game.layers = [ship] + [background]

    # render all sprites, most likely you will only render the background once per game scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_RIGHT != 0:
            if ship.x < (constants.SCREEN_X - constants.SPRITE_SIZE):
                ship.move((ship.x + constants.SPRITE_MOVEMENT_SPEED), ship.y)
            else:
                ship.move((constants.SCREEN_X - constants.SPRITE_SIZE), ship.y)

        if keys & ugame.K_LEFT != 0:
            if ship.x > 0:
                ship.move((ship.x - constants.SPRITE_MOVEMENT_SPEED), ship.y)
            else:
                ship.move(0, ship.y)

        # update game logic
        # redraw Sprite
        game.render_sprites([ship])
        game.tick()  # wait until refresh rate finishes


if __name__ == "__main__":
    game_scene()
