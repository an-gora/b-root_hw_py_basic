# first_channel() - turns on the first channel from the list.
# last_channel() - turns on the last channel from the list.
# turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
# next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
# previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
# current_channel() - returns the name of the current channel.
# is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name'
# exists in the list, or "No" - in the other case.

class TVController:

    def __init__(self, list_of_channels: list):
        self.list_of_channels = list_of_channels
        self.len = len(self.list_of_channels)
        self.fist_channel_by_default = list_of_channels[0]
        self.current = self.fist_channel_by_default

    def first_channel(self):
        self.current = self.list_of_channels[0]
        return self.list_of_channels[0]

    def last_channel(self):
        self.current = self.list_of_channels[self.len - 1]
        return self.list_of_channels[self.len - 1]

    def turn_channel(self, n:int):
        try:
            if n <= self.len:
                self.current = self.list_of_channels[n - 1]
                return self.list_of_channels[n - 1]
            else:
                return f'amount of available channels is less than {n}'
        except: ValueError
        return ('it is not a number')

    def next_channel(self):
        if self.list_of_channels.index(self.current) < self.len - 1:
            self.current = self.list_of_channels[self.list_of_channels.index(self.current) + 1]
            return self.current
        else:
            self.current = self.list_of_channels[0]
            return self.current

    def previous_channel(self):
        if self.list_of_channels.index(self.current) == 0:
            self.current = self.list_of_channels[self.len - 1]
            return self.current
        else:
            self.current = self.list_of_channels[self.list_of_channels.index(self.current) - 1]
            return self.current

    def current_channel(self):
        return self.current

    def is_exist(self, looking_for: int or str):
        if looking_for in range(1, 4) or looking_for in self.list_of_channels:
            return 'yes'
        else:
            return 'no'


def main():
    new_tv_controller = TVController(['BBC', 'Discovery', 'TV1000'])
    print(new_tv_controller.first_channel())
    print(new_tv_controller.last_channel())
    print(new_tv_controller.turn_channel(3))
    print(new_tv_controller.turn_channel('ch'))
    print(new_tv_controller.current_channel())
    print(new_tv_controller.next_channel())
    print(new_tv_controller.previous_channel())
    print(new_tv_controller.current_channel())
    print(new_tv_controller.is_exist(3))
    print(new_tv_controller.is_exist('BBBBS'))


if __name__ == '__main__':
    main()
