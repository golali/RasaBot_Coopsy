# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from pathlib import Path

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionCheck(Action):
    NoSQL_knowledge = Path("data/NoSQL_database.txt").read_text().split("\n")
    SQL_knowledge = Path("data/SQL_database.txt").read_text().split("\n")

    def name(self) -> Text:
        return "action_check"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        for dbname in tracker.latest_message['entities']:
            print(tracker.latest_message)
            if dbname['entity'] == 'database_name':
                name = dbname['value'].lower()
                if name == 'sql':
                    liste = self.SQL_knowledge
                    dispatcher.utter_message(text=f"Yes, i can give you some good examples. Here is a List of SQL Databases. Look here {liste}")

                elif name == 'nosql':
                    liste = self.NoSQL_knowledge
                    dispatcher.utter_message(text=f"Yes, i can give you some good examples. Here is a List of NoSQL Databases. Look here {liste}")

                else:
                    dispatcher.utter_message(
                        text=f"I do not recognize {name}, are you sure it is correctly spelled?")
        return []


class ActionServerlessList(Action):
    Serverless = Path("data/Serverless.txt").read_text().split("\n")

    def name(self) -> Text:
        return "action_serverless_list"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=f"Here is a List of Serverless framework. Look here {self.Serverless}")
        return []

class ActionNonServerlessList(Action):
    NonServerless = Path("data/Non_Serverless.txt").read_text().split("\n")

    def name(self) -> Text:
        return "action_non_serverless_list"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=f"Here is a List of Serverless framework. Look here {self.NonServerless}")
        return []                       

class ActionCrossplatformList(Action):
    Crossplatform = Path("data/Crossplatform.txt").read_text().split("\n")

    def name(self) -> Text:
        return "action_crossplatform_list"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=f"Here is a List of Crossplatform. Look here {self.Crossplatform}")
        return []             

class ActionBrowserFlavors(Action):
    Browser = Path("data/browser/Flavors.txt").read_text().split("\n")

    def name(self) -> Text:
        return "action_javascript_flavors"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=f"Here is a List of Browser. Look here {self.Browser}")
        return []

class ActionBrowserFrameworks(Action):
    Browser = Path("data/browser/FrontEndFrameworks.txt").read_text().split("\n")

    def name(self) -> Text:
        return "action_front_end_frameworks"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=f"Here is a List of Browser. Look here {self.Browser}")
        return []         

class ActionBrowserDataLayer(Action):
    Browser = Path("data/browser/DataLayer.txt").read_text().split("\n")

    def name(self) -> Text:
        return "action_browser_data_layer"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=f"Here is a List of Browser. Look here {self.Browser}")
        return []          

class ActionBrowserBuildTools(Action):
    Browser = Path("data/browser/BuildTools.txt").read_text().split("\n")

    def name(self) -> Text:
        return "action_browser_build_tools"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=f"Here is a List of Browser. Look here {self.Browser}")
        return []             

class ActionBrowserTesting(Action):
    Browser = Path("data/browser/Testing.txt").read_text().split("\n")

    def name(self) -> Text:
        return "action_browser_testing"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=f"Here is a List of Browser. Look here {self.Browser}")
        return []           