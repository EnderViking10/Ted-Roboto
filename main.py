from asyncio import TimeoutError
import random

import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='#', intents=intents)


@bot.hybrid_command(name="8ball", description="Shake the 8 ball")
async def ball_8(ctx):
    responses = ['Outlook good', 'Better not tell you now', 'Most likely',
                 'Dont count on it', 'It is decidedly so',
                 'Yes, definitely', 'Concentrate and ask again',
                 'Signs point to yes', 'Reply hazy', 'My reply is no',
                 'try again', 'As I see it, yes',
                 'Failure is another form of Success', 'Yikes']

    await ctx.send(f'{random.choice(responses)}')


@bot.hybrid_command(name="milestone", description="You are actively taking a milestone exam.")
async def milestone(ctx):
    response = 'Your environment is working as intended.'

    await ctx.defer()
    await ctx.message.author.send(response)


@bot.hybrid_command(name="feedback", description="You are actively taking a module exam.")
async def feedback(ctx):
    response = ("sparker told me that your last 4 premile attempts weren't a "
                "100, you aren't ready for a feedback session.")

    await ctx.defer()
    await ctx.message.author.send(response)


@bot.hybrid_command(name="friday")
async def friday(ctx):
    responses = ['https://youtu.be/kfVsfOSbJY0',
                 'https://youtu.be/1TewCPi92ro']

    await ctx.send(random.choice(responses))


@bot.hybrid_command(name="shame")
async def shame(ctx, user: discord.User = None, message_number: int = 1):
    if user is None:
        return await ctx.message.reply('You must specify a user')

    message_number = 10 if message_number > 10 else message_number

    await ctx.defer()
    for i in range(message_number):
        await ctx.message.channel.send(
            f'{user.mention}: Log into chat!! https://tenor.com/view/cat-disapear-cat-snow-cat-jump-fail-cat-fun-jump-cats-gif-7283381407501919931\n'
            f'Send "Echo Im in" when you haved logged into chat!')

    def check(message):
        return message.author == user and "im in" in message.content.lower()

    try:
        await bot.wait_for('message', check=check, timeout=60)
        await ctx.send("Thank you for confirming!")
    except TimeoutError:
        await ctx.send(f"{user.mention} did not confirm in time.")


@bot.command(name="sync", description="Sync Commands")
async def sync(ctx):
    synced = await ctx.bot.tree.sync()

    await ctx.send(f"Synced {len(synced)} commands globally")


def main():
    bot.run('')


if __name__ == "__main__":
    main()
