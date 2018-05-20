#!/usr/bin/python3

import time

class Timer:
	def __init__(self):
		self.start = self.now()

	def now(self):
		return time.time() * 1000.0

	def elapsed(self):
		return self.now() - self.start

class Testing:
	class TestFailException(Exception):
		pass

	def reporting(self, total, failed, elapsed):
		def makePlural(word, amount):
			return word + ("s" if amount > 1 else "")

		print("[?] " + str(total) + " " + makePlural("test", total)  + " in \'" + str('%.4f' % elapsed) + "\' seconds")

		if failed > 0:
			print("[!] " + str(failed) + " " + makePlural("test", failed) + " did not pass. =(")
		else:
			print("[$] All tests passed!")


	def test_method(self, name, expression):
		if not expression:
			raise self.TestFailException("[*] Test \"" + name + "\" failed.")

	def run(self, cls):
		timer = Timer()
		methods = tuple([x for x in dir(cls) if x[0] == 'i' and x[1] == 't'])
		classname = cls.__class__.__name__
		failed = 0

		print("")
		print("[@] Running [" + classname + "] tests...")

		for method in methods:
			try:
				self.test_method(classname + "." + method, getattr(cls, method)())
			except (self.TestFailException, Exception) as e:
				failed += 1
				print(e)

		self.reporting(len(methods), failed, timer.elapsed())
