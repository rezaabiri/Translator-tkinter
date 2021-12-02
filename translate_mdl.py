#REZA ABIRI

from deep_translator import *


class Translator :

    def translate(self, text, source, target):
        to_translate = text
        translate = GoogleTranslator(source=source, target=target).translate(to_translate)
        return translate


