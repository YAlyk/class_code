import platform


class CarClass:
    """Наш класс"""

    def __init__(self, color, make, model, year):
        """Constructor"""
        self.color = color
        self.make = make
        self.model = model
        self.year = year

        if "Windows" in platform.platform():
            print("You're using Windows!")

        self.weight = self.get_weight()
        self.model = self.new_model("suzuki")

    def get_weight(self):
        """получить значения веса"""
        self.weight = "2000 lbs"
        return self.weight

    def new_model(self, mod):
        """обновление модели"""
        self.model = mod
        return self.model
