import os
import random

import discord
from dotenv import load_dotenv


async def ball8(message: discord.Message):
    responses = ['Outlook good', 'Better not tell you now', 'Most likely',
                 'Dont count on it', 'It is decidedly so',
                 'Yes, definitely', 'Concentrate and ask again',
                 'Signs point to yes', 'Reply hazy', 'My reply is no',
                 'try again', 'As I see it, yes',
                 'Failure is another form of Success', 'Yikes']

    await message.reply(f'{random.choice(responses)}')


async def milestone(message: discord.Message):
    response = 'Your environment is working as intended.'

    await message.author.send(response)


async def feedback(message: discord.Message):
    response = ("sparker told me that your last 4 premile attempts weren't a "
                "100, you aren't ready for a feedback session.")

    await message.author.send(response)


async def friday(message: discord.Message):
    responses = ['https://youtu.be/kfVsfOSbJY0',
                 'https://youtu.be/1TewCPi92ro']

    await message.reply(random.choice(responses))


async def help_message(message: discord.Message):
    response = ('#milestone: You are actively taking a milestone exam.\n'
                '#exam: You are actively taking a module exam.\n'
                '#feedback: You want to schedule a feedback session OR you '
                'have finished an exam and want to ask questions about it.\n')

    await message.reply(response)


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message: discord.Message):
        # Return if self
        if message.author == self.user:
            return
        # Check for prefix
        if message.content[0] != '#':
            return

        if '8ball' in message.content:
            await ball8(message)

        if 'milestone' in message.content or 'exam' in message.content:
            await milestone(message)

        if 'feedback' in message.content:
            await feedback(message)

        if 'friday' in message.content:
            await friday(message)

        if 'jesus' in message.content:
            await message.reply('https://www.youtube.com/watch?v=FT5bBRjLgR8')

        if 'help' in message.content:
            await help_message(message)


intents = discord.Intents.default()
intents.message_content = True


def main():
    load_dotenv()

    TOKEN = os.getenv("DISCORD_TOKEN")

    client = MyClient(intents=intents)
    client.run(TOKEN)


if __name__ == '__main__':
    main()
