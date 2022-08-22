from __future__ import annotations
from multiprocessing import Event

from typing import TYPE_CHECKING

from common import util
from common.event import EventType, GameEvent
from common.types import COLLECTABLE_TYPES, EntityType
from src.config import GameConfig
if TYPE_CHECKING:
    from worlds.world import World

logger = util.get_logger(__name__)

def event_handler(world: World) -> None:
    needed_items_count = 20
    if world.player.rect.bottom >= GameConfig.HEIGHT:
        GameEvent(EventType.RESTART_LEVEL).post()
    for entity in world.get_entities(EntityType.SHADOW_TYPE_B):
        if world.player.collide(entity):
            GameEvent(EventType.RESTART_LEVEL).post()
    for entity in world.get_entities(EntityType.FALLING_FLOOR):
        if entity.rect.colliderect(world.player.rect.left, world.player.rect.top, world.player.rect.width, world.player.rect.height + 20):
            entity.falling()