from anuncio import Video, Display, Social




class LargoExcedidoException(Exception):
    pass

class Campaña:
    def __init__(self, nombre, anuncios):
        self.nombre = nombre
        self.anuncios = anuncios

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if len(value) <= 250:
            self._nombre = value
        else:
            raise LargoExcedidoException("El nombre supera los 250 caracteres")

    @property
    def anuncios(self):
        return self._anuncios

    @anuncios.setter
    def anuncios(self, value):
        self._anuncios = value

    def __str__(self):
        video_count = sum(isinstance(anuncio, Video) for anuncio in self.anuncios)
        display_count = sum(isinstance(anuncio, Display) for anuncio in self.anuncios)
        social_count = sum(isinstance(anuncio, Social) for anuncio in self.anuncios)
        return f"Nombre de la campaña: {self.nombre}\nAnuncios: {video_count} Video, {display_count} Display, {social_count} Social"