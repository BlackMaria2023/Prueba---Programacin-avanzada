from abc import ABC, abstractmethod

class SubTipoInvalidoException(Exception):
    pass

class Anuncio(ABC):
    FORMATOS_SUBTIPOS = {
        "FORMATO 1": ["Subtipo 1", "Subtipo 2"],
    }

    def __init__(self, alto=1, ancho=1, sub_tipo=None):
        self.alto = alto
        self.ancho = ancho
        self.sub_tipo = sub_tipo
        self._url_archivo = None
        self._url_clic = None

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, value):
        self._alto = value if value > 0 else 1

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, value):
        self._ancho = value if value > 0 else 1

    @property
    def sub_tipo(self):
        return self._sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, value):
        if value in self.__class__.SUB_TIPOS:
            self._sub_tipo = value
        else:
            raise SubTipoInvalidoException("Subtipo inválido")

    @staticmethod
    def mostrar_formatos():
        for formato, subtipos in Anuncio.FORMATOS_SUBTIPOS.items():
            print(f"{formato}:")
            print("=" * len(formato))
            for subtipo in subtipos:
                print(f"- {subtipo}")

    @property
    def url_archivo(self):
        return self._url_archivo

    @url_archivo.setter
    def url_archivo(self, value):
        self._url_archivo = value

    @property
    def url_clic(self):
        return self._url_clic

    @url_clic.setter
    def url_clic(self, value):
        self._url_clic = value

    @abstractmethod
    def comprimir_anuncio(self):
        pass

    @abstractmethod
    def redimensionar_anuncio(self):
        pass


class Video(Anuncio):
    def __init__(self, duracion=5, sub_tipo=None):
        super().__init__(alto=1, ancho=1, sub_tipo=sub_tipo)
        self.duracion = duracion

    @property
    def duracion(self):
        return self._duracion

    @duracion.setter
    def duracion(self, value):
        self._duracion = value if value > 0 else 5

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")


class Display(Anuncio):
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")


class Social(Anuncio):
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")

