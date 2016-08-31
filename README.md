# BotCraft
BotCraft is a Kik bot which retrieves Minecraft crafting recipes based on user input. Although I haven't played the game in years, I do remember what a hassle it was to constantly look up crafting recipes. To try out the bot, add "BotCraft" on Kik. If you notice a problem with the bot's performance, please send me an email via the address on my GitHub page.

The bot runs on the Flask framework and is hosted on OpenShift (https://www.openshift.com/). All crafting images are © Mojang and used in accordance with the Minecraft End User License Agreement (https://account.mojang.com/documents/minecraft_eula).

## Usage
To use the bot, send a message to BotCraft with the name of the item you wish to craft. BotCraft will then send back an image, GIF, list of suggestions, or error. Alternatively, the bot can be mentioned in a conversation to invoke the same response (e.g. @botcraft wood slabs).