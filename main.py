from random import randint


def attack(char_name, char_class):
    damage = 5 + randint(-3, -1)
    if char_class == 'warrior':
        return f'{char_name} нанёс урон противнику равный {damage}'
    elif char_class == 'mage':
        return f'{char_name} нанёс урон противнику равный {damage}'
    elif char_class == 'healer':
        return f'{char_name} нанёс урон противнику равный {damage}'
    else:
        return f'{char_name} нанёс урон противнику равный {damage}'


def special(char_name, char_class):
    endurance = 80 + 25
    attack_power = 5 + 40
    protection = 10 + 30
    if char_class == 'warrior':
        return f'''{char_name} применил специальное умение
        «Выносливость {endurance}»'''
    elif char_class == 'mage':
        return f'''{char_name} применил специальное умение
        «Атака {attack_power}»'''
    elif char_class == 'healer':
        return f'''{char_name} применил специальное умение
        «Защита {protection}»'''


def start_training(char_name, char_class):
    if char_class == 'warrior':
        print
        f'{char_name}, ты Воитель — отличный боец ближнего боя.'
    if char_class == 'mage':
        print
        f'{char_name}, ты Маг — превосходный укротитель стихий.'
        print
        f'{char_name}, ты Лекарь — чародей, способный исцелять раны.'
    print('Потренируйся управлять своими навыками.')
    print('''Введи одну из команд: attack — чтобы атаковать противника,
        defence — чтобы блокировать атаку противника или special
        — чтобы использовать свою суперсилу.''')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = ''
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(special(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class():
    approve_choice = None
    char_class = None
    while approve_choice != 'y':
        char_class = input('''Введи название персонажа,
            за которого хочешь играть:
            Воитель — warrior,
            Маг — mage,
            Лекарь — healer: ''')
        if char_class == 'warrior':
            print('''Воитель — дерзкий воин ближнего боя.
                  Сильный, выносливый и отважный.''')
        if char_class == 'mage':
            print('''Маг — находчивый воин дальнего боя.
                  Обладает высоким интеллектом.''')
        if char_class == 'healer':
            print('''Лекарь — могущественный заклинатель.
                  Черпает силы из природы, веры и духов.''')
        approve_choice = input(
            '''Нажми (Y), чтобы подтвердить выбор,
            или любую другую кнопку,
            чтобы выбрать другого персонажа ''').lower()
    return char_class


def main():
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class = choice_char_class()
    print(start_training(char_name, char_class))


main()
