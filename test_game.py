import pygame
import unittest
from unittest.mock import patch, MagicMock
from TYPINGGAME3 import Game 

class TestGame(unittest.TestCase):
    #creates an instance of the game class
   def setUp(self):
       self.game = Game()

   @patch('pygame.display.set_mode')
   def test_init(self, mock_set_mode):
       mock_set_mode.return_value = MagicMock()
       self.game.__init__()
       mock_set_mode.assert_called_once_with((750, 500))

   @patch('pygame.font.Font')
   def test_draw_text(self, mock_font):
       mock_font.return_value = MagicMock()
       self.game.draw_text(MagicMock(), 'test', 274, 26, (250, 250, 250))
       mock_font.assert_called_once_with(None, 26)

#    def test_get_sentence(self):
#        sentence = self.game.get_sentence()
#        self.assertIsInstance(sentence, str)

   @patch('pygame.display.update')
   def test_show_results(self, mock_update):
       self.game.show_results(MagicMock())
       mock_update.assert_called()

   @patch('pygame.display.update')
   def test_run(self, mock_update):
       self.game.run()
       mock_update.assert_called()

   @patch('pygame.display.update')
   def test_reset_game(self, mock_update):
       self.game.reset_game()
       mock_update.assert_called()

if __name__ == '__main__':
   unittest.main()