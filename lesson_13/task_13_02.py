# square_nums (takes a list of integers and returns the list of squares)
# remove_positives (takes a list of integers and returns it without positive numbers
# filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'


class Mathematician:

    def square_nums(self,list_of_int:list):
        list_of_square = []
        for this_int in list_of_int:
            list_of_square.append(this_int ** 2)
        return list_of_square

    def remove_positives(self, list_of_int:list):
        list_without_positive = []
        for this_int in list_of_int:
            if this_int < 0:
                list_without_positive.append(this_int)
        return list_without_positive

    def filter_leaps(self, list_of_years:list):
        list_of_not_leap_years = []
        for this_int in list_of_years:
            if this_int % 4==0:
                list_of_not_leap_years.append(this_int)
        return list_of_not_leap_years

m = Mathematician()
result1 = m.square_nums([7, 11, 5, 4])
result2 = m.remove_positives([26, -11, -8, 13, -90])
result3 = m.filter_leaps([2001, 1884, 1995, 2003, 2020])
print(result3)



