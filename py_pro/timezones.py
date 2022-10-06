from datetime import datetime
import pytz


def timezones(clave: str, nombre: str):
    time_zone = pytz.timezone(clave)
    date = datetime.now(time_zone)
    return nombre + ' ' + date.strftime('%d/%m/%Y, %H:%M:%S')


if __name__ == '__main__':
    print(timezones('America/Bogota', 'Bogotá'))
    print(timezones('America/Mexico_City', 'México'))
    print(timezones('America/Caracas', 'Caracas'))