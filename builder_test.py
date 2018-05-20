#!/usr/bin/python3

from datastore import *
from testing import *

class Datastore_Test(Testing):
	def it_can_store_a_value(self):
		ds = Datastore({"test": "testing"})
		return ds.items()['test'] == 'testing'

	def it_can_retrieve_a_value(self):
		ds = Datastore({"test": "testing"})
		return ds.get('test') == 'testing'

	def it_can_delete_a_value(self):
		ds = Datastore({"test": "testing"})
		ds = ds.delete('test')
		return not ds.contains('test')

	def it_can_check_for_a_key(self):
		ds = Datastore({"test": "testing"})
		return ds.contains('test')

	def it_can_set_a_value(self):
		ds = Datastore({"test": "testing"})
		ds = ds.set('test', 'different')
		return ds.get('test') == 'different'

	def it_returns_empty_string_when_key_not_exist(self):
		ds = Datastore({"test": "testing"})
		return ds.get('does-not-exist') == ''

	def run(self):
		super().run(self)

Datastore_Test().run()
