from Plant.app.plant import Plant


class Garden:
    def __init__(self, plant: Plant):
        self.plant = plant
        self.days = 0

    def growing_up(self):
        while True:
            self.plant.grow_up()
            self.days += 1

            if self.plant.is_arraived_in_desired_height():
                break
            else:
                self.plant.grow_down()

        return self.days

p = Plant(10,9,4)
g = Garden(p)
print(g.growing_up())