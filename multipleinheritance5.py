class Camera:
    def take_photo(self):
        print("Taking photo")


class Phone:
    def make_call(self):
        print("Making phone call")


class Smartphone(Camera, Phone):
    def use_internet(self):
        print("Using internet")


s = Smartphone()

s.take_photo()
s.make_call()
s.use_internet()