from __future__ import annotations

from typing import TYPE_CHECKING

from common import util
from common.event import EventType, GameEvent
from common.types import COLLECTABLE_TYPES

if TYPE_CHECKING:
    from worlds.world import World

logger = util.get_logger(__name__)

def event_handler(world: World):
    pass
