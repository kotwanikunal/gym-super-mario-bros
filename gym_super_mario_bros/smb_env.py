"""An OpenAI Gym environment for Super Mario Bros. and Lost Levels."""
import os
from nes_py import NESEnv


class SuperMarioBrosEnv(NESEnv):
    """An environment for playing Super Mario Bros with OpenAI Gym."""

    # the custom reward range defined by the environment
    reward_range = (-15, 15)

    # the list of discrete actions
    actions = [
        '',    # NOP
        'L',   # Left
        'R',   # Right
        'LA',  # Left + A
        'LB',  # Left + B
        'LAB', # Left + A + B
        'RA',  # Right + A
        'RB',  # Right + B
        'RAB', # Right + A + B
    ]

    def __init__(self,
        rom_mode=None,
        target_world=None,
        target_level=None,
        lost_levels=False,
    ) -> None:
        """
        Initialize a new Super Mario Bros environment.

        Args:
            rom_mode (str): the ROM mode to use when loading ROMs from disk.
                valid options are:
                -  None: the standard ROM with no modifications
                - 'downsample': down-sampled ROM with static artifacts removed
                - 'pixel': a simpler pixelated version of graphics
                - 'rectangle': an even simpler rectangular version of graphics
            target_world (int): the world to target in the ROM
            target_level (int): the level to target in the given world
            lost_levels (bool): whether to load the ROM with lost levels.
                False will load the original Super Mario Bros. game.
                True will  load the Japanese Super Mario Bros. 2 (commonly
                known as Lost Levels)

        Returns:
            None

        """
        # load the package directory of this class
        package_directory = os.path.dirname(os.path.abspath(__file__))
        # setup the path to the game ROM
        if lost_levels:
            if rom_mode is None:
                rom_name = 'roms/super-mario-bros-2.nes'
            elif rom_mode == 'pixel':
                raise ValueError('pixel_rom not supported for Lost Levels')
            elif rom_mode == 'rectangle':
                raise ValueError('rectangle_rom not supported for Lost Levels')
            elif rom_mode == 'downsample':
                rom_name = 'roms/super-mario-bros-2-downsampled.nes'
            else:
                raise ValueError('invalid rom_mode: {}'.format(repr(rom_mode)))
        else:
            if rom_mode is None:
                rom_name = 'roms/super-mario-bros.nes'
            elif rom_mode == 'pixel':
                rom_name = 'roms/super-mario-bros-pixel.nes'
            elif rom_mode == 'rectangle':
                rom_name = 'roms/super-mario-bros-rect.nes'
            elif rom_mode == 'downsample':
                rom_name = 'roms/super-mario-bros-downsampled.nes'
            else:
                raise ValueError('invalid rom_mode: {}'.format(repr(rom_mode)))
        # convert the path to an absolute path
        self.rom_file_path = os.path.join(package_directory, rom_name)
        super().__init__(self.rom_file_path)






    def get_keys_to_action(self):
        """Return the dictionary of keyboard keys to actions."""
        # Mapping of buttons on the NES joy-pad to keyboard keys
        up =    ord('w')
        down =  ord('s')
        left =  ord('a')
        right = ord('d')
        A =     ord('o')
        B =     ord('p')
        # a list of keyboard keys with indexes matching the discrete actions
        # in self.actions
        keys = [
            (),
            (left, ),
            (right, ),
            tuple(sorted((left, A, ))),
            tuple(sorted((left, B, ))),
            tuple(sorted((left, A, B, ))),
            tuple(sorted((right, A, ))),
            tuple(sorted((right, B, ))),
            tuple(sorted((right, A, B, ))),
        ]
        # A mapping of pressed key combinations to discrete actions in action
        # space
        keys_to_action = {key: index for index, key in enumerate(keys)}

        return keys_to_action


# explicitly define the outward facing API of this module
__all__ = [SuperMarioBrosEnv.__name__]
