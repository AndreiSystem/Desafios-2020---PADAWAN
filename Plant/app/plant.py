class Plant:
    def __init__(self, upSpeed: int, downSpeed: int, desiredHeight: int):
        self._height = 0
        self.up_speed = upSpeed
        self.down_speed = downSpeed
        self.desired_height = desiredHeight

    @property
    def up_speed(self) -> int:
        return self._up_speed

    @up_speed.setter
    def up_speed(self, up_speed: int):
        if up_speed < 5 or up_speed > 100:
            raise ValueError('Up Speed Invalid! Acima de 5 ou abaixo de 100')
        self._up_speed = up_speed

    def grow_up(self):
        self._height += self.up_speed

    def grow_down(self):
        self._height -= self.down_speed

    @property
    def down_speed(self) -> int:
        return self._down_speed

    @down_speed.setter
    def down_speed(self, down_speed: int):
        if down_speed < 2 or down_speed > self.up_speed:
            raise ValueError('Down Speed Invalid! Acima de 2 ou abaixo do Up Speed!')
        self._down_speed = down_speed

    @property
    def desired_height(self) -> int:
        return self._desired_height

    @desired_height.setter
    def desired_height(self, desired_height: int):
        if desired_height < 4 or desired_height > 1000:
            raise ValueError('Desired Height Invalid! Acima de 4 ou abaixo de 1000 apenas!')
        self._desired_height = desired_height

    def is_arraived_in_desired_height(self):
        return True if self._height >= self.desired_height else False









