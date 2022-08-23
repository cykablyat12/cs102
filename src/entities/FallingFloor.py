from __future__ import annotations

import logging
import random
from collections.abc import Sequence
from typing import TYPE_CHECKING

from common.types import EntityType, HMovingDirection

from common.event import GameEvent

from entities.base_entity import BaseEntity
from config import GameConfig

if TYPE_CHECKING:
    from worlds.world import World
    

logger = logging.getLogger(__name__)

class FallingFloor(BaseEntity):
    def __init__(
        self,
        speed: int = 0,
        init_dy: int = 0,
        jump_vertical_speed: int = 0,
        gravity: int = 0.6,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.speed = speed
        self.falling_spd = 0.2
        self.falling = False
        self.gravity = gravity
    def update(self, events: Sequence[GameEvent], world: World):

        """ Completely override original update() method from BaseEntity"""
        if self.rect.colliderect(world.player.rect.left, world.player.rect.top, world.player.rect.width, world.player.rect.height + 15):
            self.fall()
        
        if self.falling:
            self.falling_spd += self.gravity
            self.rect.y += self.falling_spd
        # Step 3: update current position by the deltas
            self.rect.y += self.falling_spd
    def fall(self):
        self.falling = True