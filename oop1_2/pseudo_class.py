def person_init(name, money):
    '''

    :param name:
    :param money:
    :return: give_money, get_money, show
    '''
    obj = {'name': name, 'money': money}
    obj['give_money'] = Person[1]
    obj['get_money'] = Person[2]
    obj['show'] = Person[3]
    return obj


def give_money(self, other, money):
    self['money'] -= money
    other['get_money'](other, money)


def get_money(self, money):
    self['money'] += money


def show(self):
    print('{} : {}'.format(self['name'], self['money']))

# 함수들을 튜플로 묶고 있다.
Person = person_init, give_money, get_money, show


if __name__ == '__main__':
    g = Person[0]('greg', 5000)
    j = Person[0]('john', 2000)

    # 인자로 자기 자신을 넣어준다.
    g['show'](g)
    j['show'](j)
    print('')

    #메세지 패싱
    g['give_money'](g,j,2000)

    g['show'](g)
    j['show'](j)