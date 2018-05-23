import json
import pygame
import sys
# from figures import *
from data_manager import DataManager

screen = None

def load_init(argv):
    global screen
    # otworzenie plkiku
    with open(argv[0]) as json_file:
        # stworzenie obiektu json i przypisanie do zmiennej data
        data = json.load(json_file)
   
    DataManager.set_json_data(data)
    
    # Inicjalizacja silnika PyGame
    pygame.init()

    # Ustaw wysokość i szerokość okna
    size = [DataManager.get_width(), DataManager.get_height()]
    screen = pygame.display.set_mode(size)

    # Ustaw tytuł okna
    pygame.display.set_caption("Rysowanie figur z pliku JSON.")

def main_loop():
    # Zapętlaj dopóki użytkownik nie zamknie okna i narysuj tylko raz
    done = False
    drown = False
    while not done:

        # Wykrywanie zdarzeń
        for event in pygame.event.get():
            # Wykrywanie czy użytkownik zamknął okno
            if event.type == pygame.QUIT:
                # Zmień flagę na True co pozwoli na wyjście z pętli
                done = True

        # Wyczyść cały ekran i wypełnij go kolorem tła
        screen.fill(DataManager.get_bg_color())

        # Rysuj wszystkie figury
        for figure in DataManager.get_figures():
            figure.draw(screen)

        # Pokaż gotową klatkę obrazu
        # W pętli wszystkie działąnia wykonują się na klatce, która nie jest aktualnie wyświetlana,
        # dopiero po wygenerowaniu całej klatki obrazu, zostaje ona wyświetlona
        if not drown:
            pygame.display.flip()
            drown = True

def save_quit(argv):
    # zapisz do pliku jeśli podano parametr "-o" lub "--output"
    if len(argv) > 2 and (argv[1] == '-o' or argv[1] == '--output'):
        pygame.image.save(screen, argv[2])

    pygame.quit()

def main(argv):
    load_init(argv)

    main_loop()

    save_quit(argv)

if __name__ == '__main__':
    main(sys.argv[1:])
