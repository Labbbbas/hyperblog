# -*- coding: utf-8 -*-

DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
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
        'name': 'Isabella',
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

def main():
    # Hacerlo con high order functions
    all_python_devs = list(filter(lambda worker: worker["language"]=="python", DATA))
    all_python_devs = list(map(lambda worker: worker["name"], all_python_devs))

    # Hacerlo con high order functions
    all_platzi_workers = list(filter(lambda worker: worker["organization"]=="Platzi", DATA))
    all_platzi_workers = list(map(lambda worker: worker["name"], all_platzi_workers))

    # Hacerlo con list comprehension
    adults = [worker["name"] for worker in DATA if worker["age"]>=18]

    # Hacerlo con list comprehension
    # old_people = [worker["old"] for worker in DATA if worker["age"]>70]
    old_people = [{**worker, **{'old': worker['age'] > 70}} for worker in DATA]
    
    for worker in old_people:
        print(worker)

if __name__ == '__main__':
    main()