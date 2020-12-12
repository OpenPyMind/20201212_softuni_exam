from exam_testing.project.spaceship.spaceship import Spaceship
import unittest


class SpaceshipTests(unittest.TestCase):
    def setUp(self):
        self.ss = Spaceship("space", 2)

    def test_initialization_attributes(self):
        self.assertEqual(self.ss.name, "space")
        self.assertEqual(self.ss.capacity, 2)
        self.assertEqual(self.ss.astronauts, [])
        self.assertEqual(self.ss.ZERO_CAPACITY, 0)

    def test_add_astronaut_below_capacity(self):
        astroname = "Pavel"
        expected_msg = "Added astronaut {}".format(astroname)
        actual_msg = self.ss.add(astroname)
        self.assertEqual(expected_msg, actual_msg)

    def test_add_astronaut_already_in_ship(self):
        astroname = "Pavel"
        self.ss.add(astroname)
        with self.assertRaises(ValueError) as exc:
            self.ss.add(astroname)
        expected_msg = "Astronaut {} Exists".format(astroname)
        actual_msg = str(exc.exception)
        self.assertEqual(expected_msg, actual_msg)

    def test_add_astronaut_at_capacity(self):
        a1, a2, a3 = "Pavel", "Georgi", "Petko"
        self.ss.add(a1)
        self.ss.add(a2)
        self.assertEqual(len(self.ss.astronauts), 2)
        self.assertEqual(self.ss.astronauts, ["Pavel", "Georgi"])
        with self.assertRaises(ValueError) as exc:
            self.ss.add(a3)
        expected_msg = "Spaceship is full"
        actual_msg = str(exc.exception)
        self.assertEqual(expected_msg, actual_msg)

    def test_remove_astronaut_not_in_spaceship(self):
        a1, a2 = "Pavel", "Georgi"
        with self.assertRaises(ValueError) as exc:
            self.ss.remove(a1)
        expected_msg = "Astronaut Not Found".format(a1)
        actual_msg = str(exc.exception)
        self.assertEqual(expected_msg, actual_msg)

    def test_remove_astronaut_from_spaceship(self):
        a1 = "Pavel"
        self.ss.add(a1)
        expected_msg = "Removed Pavel"
        actual_msg = self.ss.remove(a1)
        self.assertEqual(actual_msg, expected_msg)



if __name__ == "__main__":
    unittest.main()
