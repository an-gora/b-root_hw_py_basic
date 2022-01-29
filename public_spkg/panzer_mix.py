from abc import ABC, abstractmethod

class Gun:
    def __init__(self, caliber: int, barrel_lenght: int):
        self.__caliber = caliber
        self.__barrel_lenght = barrel_lenght

    def get_calliber(self):
        ...

    def is_on_target(self, dice):
        ...


class Ammo(ABC):
    @abstractmethod
    def __init__(self):
        ...

    def get_damage(self):
        ...

    def get_penetration(self):
        ...


class HeCartridge(Ammo):
    def __init__(self, this_gun, ammo_type='сняряд_тип_1'):
        self.ammo_type = ammo_type
        self.gun = this_gun

    def get_penetration(self):
        ...

    def get_damage(self):
        ...


class HeatCartridge(Ammo):
    def __init__(self, this_gun, ammo_type='сняряд_тип_2'):
        self.ammo_type = ammo_type
        self.gun = this_gun

    def get_damage(self):
        return self.gun.get_calliber() * 0.5

    def get_penetration(self):
        return self.gun.get_calliber(self)


class Armour(ABC):
    @abstractmethod
    def __init__(self):
        ...

    def is_penetrated(self):
        ...


class HArmour(Armour):
    def __init__(self, thickness: int, armour_type='броня_тип_1'):
        self.thickness = thickness
        self.type = armour_type

    def is_penetrated(self):
        if Ammo is HeCartridge:
            return Ammo.get_penetration() > self.thickness * 1.2
        elif Ammo is HeatCartridge:
            return Ammo.get_penetration() > self.thickness * 1
        else:
            return Ammo.get_penetration() > self.thickness * 0.7


class Panzer:
    def __init__(self, model: str, health: int, gun, armour_type: str, armour_width: int):
        self.model = model
        self.health = health
        self.gun = gun
        self.armour = Armour(armour_type, armour_width)
        self.ammos = (HeCartridge, HeatCartridge)
        self.loaded_ammo = None
