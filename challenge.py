DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Mentor',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Mariandrea',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():

    all_python_devs = filter(lambda dev: dev['language'] == 'python', DATA)
    all_Platzi_workers =  filter(lambda platzi_worker: platzi_worker['organization'] == 'Platzi', DATA )
    adults = filter(lambda adult: adult['age'] >= 18, DATA)

    def homeless(workers):
        n_worker = dict(workers)
        n_worker['homeless'] = n_worker['organization'] == ''
        return n_worker

    def old (workers):
        n_old = dict(workers)
        n_old['old'] = n_old['age'] >= 30
        return n_old

    workers =  map(homeless, DATA)
    old_people =  map(old, DATA) 

    all_homeless = filter(lambda homeless: homeless['homeless'] == True, workers)
    all_old_people = filter (lambda old: old['old'] == True, old_people)

    print('Python devs: ')
    for dev in all_python_devs:
        print(dev['name'])
    print('\n')

    print('Platzi workers: ')
    for worker in all_Platzi_workers:
        print(worker['name'])
    print('\n')

    print('Adults: ')
    for adult in adults:
        print(adult['name'])
    print('\n')

    print('Homeless: ')
    for homeless in all_homeless:
        print(homeless['name'])
    print('\n')

    print('Old people: ')
    for old_people in all_old_people:
        print(old_people['name'])
    print('\n')

    # Remember: when possible, use lambdas


if __name__ == '__main__':
    run()
