from unittest import TestCase, main
from re import compile
import Tabuada
import Gerador_de_senhas
from Morse_Decoder import decodeMorse


class MyTestCase_Tabuada(TestCase):
    def test_entrada_número_saída_multiplo_de_número(self):
        entrada = 'número'
        saida_esperada = 'multiplo_de_número'

        self.assertEqual(5 * 7, 35)


class MyTestCase_Gerador_de_senhas(TestCase):
    def test_all_characters_numerics_and_special_characters(self):
        regex = compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[ -\/:-@\[-`{-~]).+$')

        # for i in range(100):
        # with self.subTest(i=i):
        self.assertRegex(Gerador_de_senhas.gerar_senha(16), regex)


class MyTestCase_Morse_Decoder(TestCase):
    def text_decode_of_morse_codes(self):
        self.assertEqual("---   .-.  .-  -  ---   .-.  ---  .  ..-   .-   .-.  ---  ..-  .--.  .-   -..  ---   .-.  . "
                         " ..   -..  .   .-.  ---  --  .-", "O RATO ROEU A ROUPA DO REI DE ROMA")
        self.assertEqual(".... -.. ....- ---.. ...-- --...", "HD4837")


if __name__ == '__main__':
    main(verbosity=2)
