# Unittesting

# Teile des Programms auf Fehler testen
# Erwartetes Verhalten im Test ausprogrammieren und dann regelmäßig Tests laufen lassen

import unittest as u

from M013b import Rechner


class TestClass(u.TestCase):
	def testeAddiere(self):
		# Arrange
		r = Rechner()
		expected = 7

		# Act
		actual = r.addiere(3, 4)

		# Assert
		self.assertEqual(actual, expected)

	def testeSubtrahiere(self):
		# Arrange
		r = Rechner()
		expected = 10

		# Act
		actual = r.subtrahiere(20, 10)

		# Assert
		self.assertEqual(expected, actual)

class TestClass2(u.TestCase):
	def testeMultipliziere(self):
		r = Rechner()
		self.assertEqual(r.multipliziere(3, 4), 12)

if __name__ == "__main__":
	u.main()