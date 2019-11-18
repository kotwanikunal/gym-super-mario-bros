"""A method to load a ROM path."""
import os


# a dictionary mapping ROM paths first by lost levels, then by ROM hack mode
_ROM_PATHS = {
    'vanilla': 'adventure-island-2.nes'
}


def rom_path(rom_mode):
    """
    Return the ROM filename for a game and ROM mode.

    Args:
        rom_mode (str): the mode of the ROM hack to use as one of:
            - 'vanilla'

    Returns (str):
        the ROM path based on the input parameters

    """
    # Type and value check the lost levels parameter
    # try the unwrap the ROM path from the dictionary
    try:
        rom = _ROM_PATHS[rom_mode]
    except KeyError:
        raise ValueError('rom_mode ({}) not supported!'.format(rom_mode))
    # get the absolute path for the ROM
    rom = os.path.join(os.path.dirname(os.path.abspath(__file__)), rom)

    return rom


# explicitly define the outward facing API of this module
__all__ = [rom_path.__name__]
