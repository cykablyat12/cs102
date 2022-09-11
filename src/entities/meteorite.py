from entities.movable_entity import MovableEntity


class Meteorite(MovableEntity):
    def __init__(self, damage, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.damage = damage
    def _update_dx_dy_based_on_obstacles(self, obstacles):
        pass
