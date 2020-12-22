class Seat:
	def __init__(self):
		"""
		Class holding init status of seat (empty)
		Ability to set and fetch new states with functions
		"""
		self._state = 'Empty'

	def set_empty(self):
		"""
		method sets the seat state to EMPTY
		"""
		self._state = 'Empty'

	def set_filled(self):
		"""
		method sets the seat state to FILLED
		"""
		self._state = 'Filled'

	def is_filled(self):
		"""
		method checks if the seat is FILLED
		returns True if it is filled, False is not
		"""
		if self._state == 'Filled':
			return True
		return False

	def get_print_character(self):
		"""
		method returning a state character
		of L if empty or # if occupied
		"""
		if self.is_filled():
			return '#'
		return 'L'