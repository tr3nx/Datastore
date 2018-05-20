#!/usr/bin/python3

class Datastore:
	def __init__(self, data={}):
		self.storage = data

	def contains(self, key):
		return key in self.storage

	def items(self):
		return self.storage

	def get(self, key):
		return self.storage[key] if self.contains(key) else ""

	def store(self, data):
		return Datastore({**self.storage, **data})

	def set(self, key, value):
		return Datastore({**self.storage, **{key: value}})

	def delete(self, key):
		return Datastore({k:v for k, v in self.storage.items() if k != key})
