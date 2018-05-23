import figures as f

class DataManager:

    __width = None
    __height = None
    __fg_color = None
    __bg_color = None

    __palette = {}

    __figures = []

    __FACTORY_MAP = {
        "point": f.Point,
        "polygon": f.Polygon,
        "rectangle": f.Rectangle,
        "square": f.Square,
        "circle": f.Circle
    }

    @classmethod
    def set_json_data(cls, json_data):
        cls.__width = json_data["Screen"]["width"]
        cls.__height = json_data["Screen"]["height"]
        cls.__set_palette(json_data["Palette"])
        cls.__bg_color = cls.__color2RGB(json_data["Screen"]["bg_color"])
        cls.__fg_color = cls.__color2RGB(json_data["Screen"]["fg_color"])

        
        
        for figure in json_data["Figures"]:
            cls.__insert_figure(figure)

    # __set_palette, która przyjmie palette, który będzie json_data["Palette"]
    @classmethod
    def __set_palette(cls, palette):
        for color in palette:
            cls.__palette[color] = cls.__color2RGB(palette[color])

    @classmethod
    def __color2RGB(cls, color):
        if color[0] == '(' and color[len(color) - 1] == ')':
            # usuń z ciągu '('
            color = color.replace('(', '')
            # usuń z ciągu ')'
            color = color.replace(')', '')
            # rozdziel ciąg na tablicę - ',' jako separator
            split_color = color.split(',')
            # przypisz wartości r, g i b z rozdzielonego ciągu
            r = int(split_color[0])
            g = int(split_color[1])
            b = int(split_color[2])
            # zwróć kolor w postaci (r, g, b)
            return (r, g, b)

        # Jeżli jest w formacie '#rrggbb'
        if len(color) == 7 and color[0] == '#':
            r = color[1] + color[2]
            g = color[3] + color[4]
            b = color[5] + color[6]
            # zamień wartości zapisane w systemie 16-tkowym
            # na liczby dziesiętne i
            # zwróć kolor w postaci (r, g, b)
            return int(r, 16), int(g, 16), int(b, 16)

        # sprawdz czy podany kolor istnieje w palecie kolorów
        for key in cls.__palette.keys():
            if color == key:
                return cls.__palette[color]

        return None

    @classmethod
    def get_width(cls):
        return cls.__width

    @classmethod
    def get_height(cls):
        return cls.__height

    @classmethod
    def get_bg_color(cls):
        return cls.__bg_color

    @classmethod
    def get_fg_color(cls):
        return cls.__fg_color

    @classmethod
    def get_palette_color(cls, color):
        return cls.__palette[color]

    #  __insert_figure, która weźmie jsonową figurę i zmieni ją w obiekt Pythona
    @classmethod
    def __insert_figure(cls, figure):
        # rozpakowywuję słownik i mapuję klucze do zmiennych oprócz type, muszę obsłużyć brak koloru
        if "color" in figure:
            figure["color"] = cls.__color2RGB(figure["color"])
        else:
            figure["color"] = cls.__fg_color

        cls.__figures.append( \
            cls.__FACTORY_MAP[figure["type"]]( \
                **{key: figure[key] for key in figure if key != "type"} \
                ) \
            )

    @classmethod
    def get_figures(cls):
        return cls.__figures

