""""""

from Drivers import JSONFileDriver, PickleDriver, JSONStringDriver


class SDBuilder:
    def build(self):
        return None

    def __str__(self):
        return self.__class__.__name__


class JSONFileBuilder(SDBuilder):
    def build(self):
        filename = input('Enter filename: **filename.json: ')
        return JSONFileDriver(filename)


class JSONStringBuilder(SDBuilder):
    def build(self):
        return JSONStringDriver()


class PickleBuilder(SDBuilder):
    def build(self):
        filename = input('Enter filename: **filename.bin: ')
        return PickleDriver(filename)


class SDFabric:
    @staticmethod
    def get_sd_driver(driver_name):
        builder = {
            'json': JSONFileBuilder,
            'pickle': PickleBuilder,
            'json_string': JSONStringBuilder
        }

        if driver_name in builder:
            return builder[driver_name]()
        else:
            raise Exception("Неверные данные")


# Fabrica(name) -> Builder(build) -> nameSDBuilder - > return Driver(filename)








