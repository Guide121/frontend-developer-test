import csv
from faker import Faker
from random import randint


def create_evaluation():
    fake = Faker()

    return [
        fake.name(),
        f'{fake.city()}, {fake.country()}',
        'https://picsum.photos/50/50',  # random image from Picsum Photos because Faker doesn't provide images
        randint(4, 5),
        fake.text()
    ]


# function to create fake evaluations to simulate an api
def create_evaluations(filename):
    fieldnames = ['name', 'address', 'image', 'evaluation', 'comment']

    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for _ in range(5):
            evaluation = dict(zip(fieldnames, create_evaluation()))

            writer.writerow(evaluation)


# function to get all evaluations from a csv file
def evaluations(filename):
    with open(filename) as f:
        return [evaluation for evaluation in csv.DictReader(f)]
