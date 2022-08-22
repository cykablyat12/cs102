from __future__ import annotations

from typing import TYPE_CHECKING

from common import util
from common.event import EventType, GameEvent
from common.types import COLLECTABLE_TYPES, EntityType

if TYPE_CHECKING:
    from worlds.world import World

logger = util.get_logger(__name__)

def event_handler(world: World) -> None:
    needed_items_count = 20
    for entity in world.get_entities(EntityType.SHADOW_TYPE_B):
        if world.player.collide(entity):
            GameEvent(EventType.RESTART_LEVEL).post()