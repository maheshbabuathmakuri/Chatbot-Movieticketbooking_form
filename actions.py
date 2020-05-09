# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from rasa_sdk.forms import FormAction
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List
from rasa_sdk.events import SlotSet, Form
import logging

logger = logging.getLogger(__name__)

REQUESTED_SLOT = "requested_slot"


class TicketBookingForm(FormAction):
    """Collects sales information and adds it to the spreadsheet"""

    def name(self):
        return "ticket_booking_form"
    @staticmethod
    def required_slots(tracker):
        return [
            "language", "movie_name", "planned_date", "theater_name", "planned_time", "no_of_tickets"
            ]
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message("Thanks for getting in touch, we’ll contact you soon")
        return []
    
    # noinspection PyUnusedLocal
    def request_next_slot(
        self,
        dispatcher,  # type: CollectingDispatcher
        tracker,  # type: Tracker
        domain,  # type: Dict[Text, Any]
    ):
        # type: (...) -> Optional[List[Dict]]
        """Request the next slot and utter template if needed,
            else return None"""

        for slot in self.required_slots(tracker):
            if self._should_request_slot(tracker, slot):
                logger.debug("Request next slot '{}'".format(slot))
                if slot == "planned_time":
                    dispatcher.utter_message("customixed slot but you can enter planned date.")
                    return [SlotSet(REQUESTED_SLOT, slot)]
                else:
                    dispatcher.utter_template(
                        "utter_ask_{}".format(slot),
                        tracker,
                        silent_fail=False,
                        **tracker.slots
                    )
                    return [SlotSet(REQUESTED_SLOT, slot)]

        # no more required slots to fill
        return None