from __future__ import annotations

import logging
import random
from collections.abc import Sequence
from typing import TYPE_CHECKING

from common.types import HMovingDirection

from common.event import GameEvent

from entities.base_entity import BaseEntity
from config import GameConfig

if TYPE_CHECKING:
    from worlds.world import World
    

logger = logging.getLogger(__name__)

class ShadowTypeB(BaseEntity):
    def __init__(
        self,
        speed: int = 0,
        init_dy: int = 0,
        jump_vertical_speed: int = 0,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.speed = speed
        self.dy = init_dy
        self.jump_vertical_speed = jump_vertical_speed
        self.direction = random.choice((HMovingDirection.UP, HMovingDirection.DOWN))
    def update(self, events: Sequence[GameEvent], world: World):

        """ Completely override original update() method from BaseEntity"""
        if self.rect.y <= -200 + self.rect.height:
            self.direction = HMovingDirection.DOWN
        elif self.rect.bottom >= GameConfig.HEIGHT:
            self.direction = HMovingDirection.UP

        if self.direction == HMovingDirection.DOWN:
            self.dy = self.jump_vertical_speed
        elif self.direction == HMovingDirection.UP:
            self.dy = -self.jump_vertical_speed

        # Step 3: update current position by the deltas
        self.rect.y += self.dy