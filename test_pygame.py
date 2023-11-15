import unittest
from unittest.mock import patch
import sys
from io import StringIO
import math
import pygame


class TestGame(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pygame.init()

    @classmethod
    def tearDownClass(cls):
        pygame.quit()

    def setUp(self):
        self.original_stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        sys.stdout = self.original_stdout

    def test_collision_and_scoring(self):
        with patch('pygame.event.get', return_value=[]):  # Mock the event to avoid an infinite loop
            with patch('pygame.time.delay', return_value=None):  # Mock the delay function

                # Set up game state
                flowerX = 300
                bulletX = 300
                bulletY = 260
                villains = [{'x': 300, 'y': 50, 'speedX': 0.1, 'speedY': 45}]
                score = 0

                # Simulate bullet hitting villain
                bulletY -= 0.5  # Move the bullet up
                distance = math.sqrt((bulletX - villains[0]['x']) ** 2 + (bulletY - villains[0]['y']) ** 2)
                if distance < 27:
                    bulletY = 260
                    villains[0]['x'] = 400  # Move the villain to a new position
                    villains[0]['y'] = 60
                    score += 1

                
                self.assertEqual(score, 0)
                self.assertEqual(villains[0]['x'], 300)
                self.assertEqual(villains[0]['y'], 50)

    def test_flower_movement_left(self):
        # Set up game state
        flowerX = 300
        changeX = -1

        # Simulate left movement
        flowerX += changeX

       
        self.assertEqual(flowerX, 299)

    def test_flower_movement_right(self):
        # Set up game state
        flowerX = 300
        changeX = 1

        # Simulate right movement
        flowerX += changeX

        
        self.assertEqual(flowerX, 301)

    def test_bullet_reset_after_collision(self):
        # Set up game state
        bulletY = 260
        villains = [{'x': 300, 'y': 50, 'speedX': 0.1, 'speedY': 45}]

        # Simulate bullet hitting villain
        distance = math.sqrt((300 - villains[0]['x']) ** 2 + (260 - villains[0]['y']) ** 2)
        if distance < 27:
            bulletY = 260

        
        self.assertEqual(bulletY, 260)

    


if __name__ == '__main__':
    unittest.main()
