# -*- coding: utf-8 -*-

import csv 
import os

class Contact:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


class ContactBook:

    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self._save()
        
    def show_all(self):
        if self._contacts == []:
            self._empty()
        else:
            for contact in self._contacts:
                self._print_contact(contact)

    def delete(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name == name:
                del self._contacts[idx]
                self._save()
                break

    def search(self, name):
        for contact in self._contacts:
            if contact.name == name:
                self._print_contact(contact)
                break
        else:
            self._not_found()

    def _save(self):
        with open('contacts.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(('name', 'phone', 'email'))
            
            for contact in self._contacts:
                writer.writerow((contact.name, contact.phone, contact.email))

    def update(self, name):
        for i, contact in enumerate(self._contacts):
            if contact.name == name:
                print("\n\n")
                print('Ingrese el nuevo nombre:'.center(80))
                contact.name = str(input(''.center(36))).upper()
                print("\n\n")
                print('Ingrese el nuevo número de teléfono:'.center(80))
                contact.phone = str(input(''.center(34))).replace(' ', '')
                print("\n\n")
                print('Ingrese el nuevo email:'.center(80))
                contact.email = str(input(''.center(29))).lower()
                self._contacts[i] = contact
                self._save()
                print("\n\n")
                print('El contacto fue actualizado en tu lista de contactos'.center(77))
                break
        else:
            self._not_found()

    def _print_contact(self, contact):
        print(''.center(80,'-'))
        print("\n")
        print('Nombre: {}'.center(80).format(contact.name))
        print('Teléfono: {}'.center(75).format(contact.phone))
        print('Email: {}'.center(65).format(contact.email))
        print('\n')
        print(''.center(80,'-'))

    def _not_found(self):
        print("\n\n")
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!'.center(81))
        print("!!Contacto no encontrado!!".center(81))
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!'.center(81))

    def _empty(self):
        print("\n\n")
        print("Tu lista está vacía".center(83))


def run():

    #os.system('clear')

    contact_book = ContactBook()

    with open('contacts.csv', 'r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue
            
            contact_book.add(row[0], row[1], row[2])

    while True:
        print('''

                                ¿Qué deseas hacer?


                              [a]ñadir     contacto

                              [ac]tualizar contacto

                              [b]uscar     contacto

                              [e]liminar   contacto

                              [l]istar    contactos

                              [s]alir

        ''')
        command = str(input("".center(40))).lower()

        os.system('clear')

        if command == 'a' or command == 'añadir':
            print("\n")
            print("Escribe el nombre del contacto: ".center(80))
            name = str(input("".center(36))).upper()
            print("\n")
            print("Ingrese el teléfono de {}:".center(75).format(name))
            phone = str(input("".center(36))).replace(' ', '')
            print("\n")
            print("Teclee el email de {}:".center(75).format(name))
            email = str(input("".center(36))).lower()
            os.system('clear')
            print('\n')
            print('{} fue añadid@ a tu lista de contactos'.center(80).format(name))
            contact_book.add(name, phone, email)

        elif command == 'ac' or command == 'actualizar':
            print("\n")
            print("Escribe el nombre del contacto: ".center(81))
            name = str(input("".center(37))).upper()
            
            contact_book.update(name)

        elif command == 'b' or command == 'buscar':
            print("\n")
            print("Escribe el nombre del contacto: ".center(85))
            name = str(input("".center(38))).upper()
            print('\n')

            contact_book.search(name)

        elif command == 'e' or command == 'eliminar':
            print("\n")
            print("Escribe el nombre del contacto: ".center(82))
            name = str(input("".center(38))).upper()
            print("\n\n")
            print('Se eliminó a {} de tu lista de contactos'.center(80).format(name))
            contact_book.delete(name)

        elif command == 'l' or command == 'listar':
            contact_book.show_all()

        elif command == 's' or command == 'salir':
            break

        else:
            print("\n")
            print('Comando no encontrado :P'.center(83))


if __name__ == '__main__':
    os.system('clear')
    print("\n")
    print(" B I E N V E N I D @  A  T U  A G E N D A :) ".center(80, "-"))
    run()