from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet


class ActionDimKPIAdject(Action):
	def name(self):
		return "action_dim.kpi.adject"

	def run(self, dispatcher, tracker, domain):
		# cuisine = tracker.get_slot('cuisine')
		# q = "select * from restaurants where cuisine='{0}' limit 1".format(cuisine)

		return [SlotSet("matches", ['action_dim.kpi.adject'])]


class ActionFactKPIDimFilter(Action):
	def name(self):
		return "action_fact.kpi.dim.filter"

	def run(self, dispatcher, tracker, domain):
		# cuisine = tracker.get_slot('cuisine')
		# q = "select * from restaurants where cuisine='{0}' limit 1".format(cuisine)

		return [SlotSet("matches", ['action_fact.kpi.dim.filter'])]


class ActionFactKPISingle(Action):
	def name(self):
		return "action_fact.kpi.single"

	def run(self, dispatcher, tracker, domain):
		# cuisine = tracker.get_slot('cuisine')
		# q = "select * from restaurants where cuisine='{0}' limit 1".format(cuisine)

		return [SlotSet("matches", ["action_fact.kpi.single"])]


class ActionFactTableGroup(Action):
	def name(self):
		return "action_fact.table.group"

	def run(self, dispatcher, tracker, domain):
		# cuisine = tracker.get_slot('cuisine')
		# q = "select * from restaurants where cuisine='{0}' limit 1".format(cuisine)

		return [SlotSet("matches", ["action_fact.table.group"])]
