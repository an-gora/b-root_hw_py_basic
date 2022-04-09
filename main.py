import pickle
import random
import uuid


class Equipment:
    rate = 0.01
    rate_of_crash = 0.1
    luck = 0

    def __init__(self, basic_price):
        self.basic_price = basic_price
        self.id = uuid.uuid4()
        self.current_price = self.basic_price
        self.base = 0

    def __str__(self):
        return f'{self.__class__.__name__} - {self.basic_price}$/{self.current_price}$'

    __repr__ = __str__

    def is_it_luck(self):
        probability_of_crash = random.randint(1, 100)
        flag = probability_of_crash > self.luck
        print('ok' if flag else 'crash')
        return flag

    def price_of_current_roll(self):
        return self.basic_price * (self.rate if self.is_it_luck() else self.rate_of_crash)

    def roll(self):
        self.current_price = max(self.current_price - self.price_of_current_roll(), 0)


class Ski(Equipment):
    luck = 8


class Board(Equipment):
    luck = 13


class Sleigh(Equipment):
    luck = 2


class Helmet(Equipment):
    rate = 0
    rate_of_crash = 0


class Human:

    def __init__(self, name):
        self.name = name
        self.id = uuid.uuid4()
        self.list_of_current_equipment = []

    def take_equipment(self, equipment):
        self.list_of_current_equipment.append(equipment)

    def return_equipment(self, base):
        temp_list = [equipment for equipment in self.list_of_current_equipment if equipment.base == base]
        for eqp in temp_list:
            self.list_of_current_equipment.remove(eqp)
        return temp_list


class Lift:
    allowed_set = ((Sleigh.__name__,), (Ski.__name__, Helmet.__name__), (Board.__name__, Helmet.__name__))

    def __init__(self):
        pass

    def is_client_valid(self, person):
        checking_set = set(equipment.__class__.__name__ for equipment in person.list_of_current_equipment)
        for allowed_eqp in self.allowed_set:
            if set(allowed_eqp).issubset(checking_set):
                print(f'{person.name} gooo')
                return True
        return False

    def ride(self, person):
        if self.is_client_valid(person):
            for equipment in person.list_of_current_equipment:
                equipment.roll()


class SkiBase:

    def __init__(self, name):
        self.name = name
        self.id = uuid.uuid4()
        self.equipment_list = []
        self.clients_list = []

    def buy(self, equipment):
        equipment.base = self
        self.equipment_list.append(equipment)

    def give_equipment(self, person):
        if not self.equipment_list:
            return
        random.shuffle(self.equipment_list)
        self.clients_list.append(person)
        given_item = self.equipment_list.pop()
        person.take_equipment(given_item)
        return given_item

    def take_back(self, person):
        for equipment in person.return_equipment(self):
            if equipment.base == self:
                self.equipment_list.append(equipment)
        self.clients_list.remove(person)

    def store(self):
        file = open(f'{self.name}.bin', 'wb')
        pickle.dump(self, file)
        file.close()

    @classmethod
    def restore(cls, name):
        try:
            file = open(f'{name}.bin', 'rb')
            l2 = pickle.load(file)
            file.close()
            return l2
        except FileNotFoundError:
            return cls(name)


if __name__ == '__main__':
    petro = Human('Petro')
    # petro.take_equipment(Ski(1000))
    # petro.take_equipment(Helmet(2000))
    # petro.take_equipment(Board(2000))
    # petro.take_equipment(Sleigh(3000))
    # print(petro.list_of_current_equipment)
    this_lift = Lift()
    new_base = SkiBase.restore('Veselka')
    print(new_base.equipment_list)
    # new_base.buy(Ski(1000))
    # new_base.buy(Helmet(1000))
    # new_base.buy(Board(1000))
    # new_base.buy(Sleigh(1000))
    # ski_2 = Ski(2000)
    # board_1 = Board(100)
    # sleigh_1 = Sleigh(500)
    # helmet = Helmet(10)
    # temp_eqp = [ski_1, ski_2, board_1, sleigh_1, helmet]
    # for eqp in temp_eqp:
    #     new_base.buy(eqp)
    # print(new_base.equipment_list)
    new_base.give_equipment(petro)
    new_base.give_equipment(petro)
    print(petro.list_of_current_equipment)
    print(this_lift.ride(petro))
    print(petro.list_of_current_equipment)
    new_base.take_back(petro)
    print(new_base.equipment_list)
    print(petro.list_of_current_equipment)
    new_base.store()

