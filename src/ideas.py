config = {
    "idealist": "742718894690795550"
}

# Import function
def setup_ideas(bot):

    @bot.command()
    async def idealist(ctx, chanid = ''):

        # Return current idea-list channel
        if chanid == '':
            chanid = config["idealist"]
            return await ctx.send(
                f'Current `idea-list` channel is <#{chanid}>!'
            )

        # get rid of '<#...>'
        chanid = int(chanid[2:-1])

        # Get the channel with id 'chanid'
        chans = filter(
            lambda x: x.id == chanid,
            bot.get_all_channels()
        )
        chans = list(chans)
        chan = chans[0]

        # Set it as write channel
        config["idealist"] = str(chan.id)
        await ctx.send(f'`idea-list` channel is now <#{chan.id}>!')


    # Listen ideas emoji reactions
    @bot.event
    async def on_raw_reaction_add(reaction):
        channel = bot.get_channel(reaction.channel_id)

        message = None
        try:
            message = await channel.fetch_message(reaction.message_id)
        except e:
            return

        # Check stuff
        if str(channel) != 'ideas':
            return
        elif message.author == bot.user:
            return

        # Remove stuff
        if reaction.emoji.name != '👍':
            await message.remove_reaction(reaction.emoji, reaction.member)
            await channel.send(
                content='You can\'t use that! Please use 👍 only!',
                delete_after=10.0
            )


    # Purging ideas
    @bot.command('purge')
    async def purge(message):
        if str(message.channel) == 'ideas':
            await message.channel.purge()