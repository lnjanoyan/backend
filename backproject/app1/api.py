#

import os
import django
import requests

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backproject.settings')
django.setup()

from app1.models import Books1, Characters583


def get_books():
    try:
        response = requests.get("https://www.anapioficeandfire.com/api/books/")
        return response.json()
    except:
        print("Error with books")
        return []


def get_characters(char_url):
    try:
        response = requests.get(char_url)
        return response.json()
    except:
        print("Error with characters")
        return {}


def save_books_and_characters():
    books_data = get_books()

    for book_data in books_data:
        book = Books1.objects.create(
            url=book_data['url'],
            name=book_data['name'],
            isbn=book_data['isbn'],
            authors=', '.join(book_data['authors']),
            numberOfPages=book_data['numberOfPages'],
            publisher=book_data['publisher'],
            country=book_data['country'],
            mediaType=book_data['mediaType'],
            released=book_data['released']
        )

        for character_url in book_data['characters']:
            character_data = get_characters(character_url)
            character, created = Characters583.objects.get_or_create(
                url=character_data['url'],
                defaults={
                    'name': character_data['name'],
                    'gender': character_data['gender'],
                    'culture': character_data['culture'],
                    'born': character_data['born'],
                    'died': character_data['died'],
                    'titles': ', '.join(character_data['titles']) if character_data['titles'] else '',
                    'aliases': ', '.join(character_data['aliases']) if character_data['aliases'] else '',
                    'father': character_data['father'],
                    'mother': character_data['mother'],
                    'spouse': character_data['spouse'],
                    'allegiances': ', '.join(character_data['allegiances']) if character_data['allegiances'] else '',
                    'tvSeries': ', '.join(character_data['tvSeries']) if character_data['tvSeries'] else '',
                    'playedBy': ', '.join(character_data['playedBy']) if character_data['playedBy'] else ''
                }
            )

            book.characters.add(character)

        for pov_character_url in book_data['povCharacters']:
            pov_character_data = get_characters(pov_character_url)
            pov_character, created = Characters583.objects.get_or_create(
                url=pov_character_data['url'],
                defaults={
                    'name': pov_character_data['name'],
                    'gender': pov_character_data['gender'],
                    'culture': pov_character_data['culture'],
                    'born': pov_character_data['born'],
                    'died': pov_character_data['died'],
                    'titles': ', '.join(pov_character_data['titles']) if pov_character_data['titles'] else '',
                    'aliases': ', '.join(pov_character_data['aliases']) if pov_character_data['aliases'] else '',
                    'father': pov_character_data['father'],
                    'mother': pov_character_data['mother'],
                    'spouse': pov_character_data['spouse'],
                    'allegiances': ', '.join(pov_character_data['allegiances']) if pov_character_data[
                        'allegiances'] else '',
                    'tvSeries': ', '.join(pov_character_data['tvSeries']) if pov_character_data['tvSeries'] else '',
                    'playedBy': ', '.join(pov_character_data['playedBy']) if pov_character_data['playedBy'] else ''
                }
            )

            book.povCharacters.add(pov_character)

        book.save()


if __name__ == "__main__":
    save_books_and_characters()
