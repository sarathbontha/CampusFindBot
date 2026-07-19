from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount


class EchoBot(ActivityHandler):

    async def on_members_added_activity(
        self, members_added: [ChannelAccount], turn_context: TurnContext
    ):
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity(
                    "Welcome to CampusFind Bot! Type 'help' to see what I can do."
                )

    async def on_message_activity(self, turn_context: TurnContext):

        user_message = turn_context.activity.text.lower().strip()

        if user_message in ["hi", "hello", "hey"]:
            response = "Hello! Welcome to CampusFind Bot. How can I help you today?"

        elif user_message == "help":
            response = (
                "I can help you with:\n"
                "- Report lost item\n"
                "- Report found item\n"
                "- Lost laptop\n"
                "- Lost wallet\n"
                "- Lost ID card\n"
                "- Office hours\n"
                "- Contact information\n"
                "- Type 'bye' to exit"
            )

        elif user_message == "report lost item":
            response = (
                "Please tell me the item name, color, and the last place where you saw it."
            )

        elif "laptop" in user_message:
            response = (
                "Please provide the laptop brand, color, and the last known location."
            )

        elif "wallet" in user_message:
            response = (
                "Please provide the wallet color and the last place where you remember using it."
            )

        elif "id card" in user_message:
            response = (
                "Please contact the campus ID office immediately and report the missing ID card."
            )

        elif "found" in user_message:
            response = (
                "Thank you for reporting a found item. Please submit it to the campus security office."
            )

        elif "office hours" in user_message:
            response = (
                "The Lost and Found office is open Monday to Friday from 9:00 AM to 4:00 PM."
            )

        elif "contact" in user_message:
            response = (
                "You can contact the campus security office through the official university directory."
            )

        elif user_message in ["bye", "exit"]:
            response = "Goodbye! I hope you find your item soon."

        else:
            response = (
                "Sorry, I could not understand your request. Please type 'help' to see the available options."
            )

        await turn_context.send_activity(response)