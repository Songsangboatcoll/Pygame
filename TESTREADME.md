# Pygame
FIRST: test_init:
  .Patches pygame.display.set_mode to return a MagicMock
  .Verifies set_mode was called once with the expected size
  .This isolates and test the initialization logic
  
SECOND:test_draw_text:
Patches pygame.font.Font to return a MagicMock
Calls draw_text() with sample args
Checks Font was called once with expected args
Verifies the font rendering during draw_text()

THIRD:test_show_results:
Patches pygame.display.update to track calls
Calls show_results()
Checks that update was called, verifying screen refresh

FOURTH:test_run:
Patches pygame.display.update
Calls the run() method to start main game loop
Verifies update was called, checking full loop

FIFTH:test_reset_game:
Patches pygame.display.update
Calls reset_game()
Checks update was called after resetting
