name = 'Anastasiia'
surname = 'Gordiievych'


def task_05_2(name: str, surname: str) -> str:
    return ('concatenated name + surname = ',
            ' '.join([name, surname]))


# return ('%s %s' % (name, surname))

if __name__ == '__main__':
    print(task_05_2(name, surname))
