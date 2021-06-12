# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionCheck(Action):

    def name(self) -> Text:
        return "action_check"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        for dbname in tracker.latest_message['entities']:
            print(tracker.latest_message)
            if dbname['entity'] == 'database_name':
                name = dbname['value'].lower()
                if name == 'h':
                    dispatcher.utter_message(text=f"Yes, {name} is a SQL")

                elif name == 'nosql':
                    dispatcher.utter_message(text=f"OK, {name} is a NoSQL")

                else:
                    dispatcher.utter_message(
                        text=f"I do not recognize {name}, are you sure it is correctly spelled?")
        return []