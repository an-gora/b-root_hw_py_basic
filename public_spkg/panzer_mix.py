from abc import ABC
from random import random


class Gun:
    def __init__(self, caliber: int, barrel_lenght: int):
        self.__caliber = caliber
        self.__barrel_lenght = barrel_lenght
    def get_calliber(self):
        ...
    def is_on_target(self, dice):
        ...


class Ammo(ABC):
    def __init__(self, ammo_type:str, gun):
        ...
    def get_damage(self):
        ...
        # return self.gun.ger_calliber() * 3

    def get_penetration(self):
        ...
        # return self.gun.ger_calliber(self)
    def to_string(self):
        return (f'снаряд {self.ammo_type} к пушке калибра {self.gun.get_calliber}')

class HeCartridge(Ammo):
    # def __init__(self, ammo_type = 'фугасный'):
    def __new__(self, ammo_type='фугасный'):
        self.ammo_type = ammo_type
    def get_penetration(self):
        return self.gun.get_calliber(self)
    def get_damage(self):
        return self.gun.get_calliber() * 3

class HeatCartridge(Ammo):
    # def __init__(self, ammo_type = 'кумулятивный'):
    def __new__(self, ammo_type='кумулятивный'):
        self.ammo_type = ammo_type
    def get_damage(self):
        return self.gun.get_calliber() * 0.5
    def get_penetration(self):
        return self.gun.get_calliber(self)

class ApCartridge(Ammo):
    # def __init__(self, ammo_type = 'подкалиберный'):
    def __new__(self, ammo_type = 'подкалиберный'):
        self.ammo_type = ammo_type
    def get_damage(self):
        return self.gun.get_calliber() * 0.3
    def get_penetration(self):
        return self.gun.get_calliber(self)

class Armour(ABC):
    def __init__(self, thickness: int, type:str):
        self.thickness = thickness
        self.type = type
    def is_penetrated(self):
        return self.Ammo.get_damage()>self.thickness

class HArmour(Armour):
    def __init__(self, thickness:int, armour_type ='гомогенная'):
        self.thickness = thickness
        self.type = armour_type
    def is_penetrated(self):
        if self.Ammo is HeCartridge:
            return self.Ammo.get_penetration()>self.thickness*1.2
        elif self.Ammo is HeatCartridge:
            return self.Ammo.get_penetration()>self.thickness*1
        else:
            return self.Ammo.get_penetration()>self.thickness*0.7

class Panzer:
    def __init__(self, model:str, health:int, Gun, armour_type: str, armour_width: int):
        self.model = model
        self.health = health
        self.gun = Gun
        self.armour = Armour(armour_type, armour_width)
        self.ammos = (HeCartridge, HeatCartridge, ApCartridge)
        self.loaded_ammo = None

    # def load_ammos(self):
    #     ammo_hecartridge = HeCartridge
    #     self.ammo_heatcartridge = HeatCartridge
    #     self.ammo_apcartridge = ApCartridge
    #     for i in range (1,10):
    #         self.ammos.append(ammo_hecartridge)
    #         self.ammos.append(self.ammo_heatcartridge)
    #         self.ammos.append(self.ammo_apcartridge)

    def load_gun(self):
        i = 0
        while i <len(self.ammos):
            if self.ammos[i]:
                self.loaded_ammo = self.ammos[i]
                print('заряжено!')
                i+=1
            else:
                print('сорян, командос,  на нуле')

    def ammo_shoot(self):
        if self.loaded_ammo!=None:
            fired_ammo = self.loaded_ammo
            self.ammos.remove(fired_ammo)
            self.loaded_ammo = None
            # rnd = random()
            dice = random.randint(1,100)
            hit = self.gun.is_on_target(dice)
            if self.gun.is_on_target(dice):
                print ('попадание')
                return fired_ammo
            else:
                print('мимо, лузер')
                return None
        else:
            print('не заряжено')
            return None

    def handle_hit(self):
        if self.armour.is_penetrated():
            self.health -= self.loaded_ammo.get_damege()
        else:
            print('броня не пробита')


first_gun = Gun(caliber = 15, barrel_lenght = 45)
first_panzer = Panzer(model = 'T-34', health = 10, Gun = first_gun, armour_type ='гомогенная', armour_width = 25)
print(first_panzer.load_gun())


















