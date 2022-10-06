from datetime import datetime

def simple():
    # my_time = datetime.datetime.utcnow()
    # print(my_time)

    my_day = datetime.today()
    # print(my_day)
    print(f'Year: {my_day.year}')
    print(f'Month: {my_day.month}')
    print(f'Day: {my_day.day}')


def formatos():
    my_datetime = datetime.utcnow()
    print(my_datetime)

    latam = my_datetime.strftime('%d/%m/%Y')
    print(f'Formato LATAM: {latam}')

    usa = my_datetime.strftime('%m/%d/%Y')
    print(f'Formato USA: {usa}')

    otro = my_datetime.strftime('Estamos en el año %Y, en el mes %m, en el día %d')
    print(f'Formato random: {otro}')


if __name__ == '__main__':
    # simple()
    formatos()