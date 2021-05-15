from rstr import xeger


class Robot:
    def __init__(self):
        self.name = None
        self.generate_name()

    def generate_name(self):
        previous_name = self.name
        while True:
            generate_name = xeger(r'^[A-Z]{2}\d{3}$')
            if previous_name != generate_name:
                self.name = generate_name
                break

    def reset(self):
        self.generate_name()
