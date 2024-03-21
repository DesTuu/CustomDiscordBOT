from discord.ext import commands
import discord
import random
import gifs


class Interactions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        brief=f"nickogólnydiscorda - przytulasz wybranego użytkownika gifem"
    )
    async def hug(self, ctx, user: discord.Member):
        embed = discord.Embed(
            title="",
            description=f"{ctx.author.mention} przytula {user.mention}!",
            color=ctx.author.color
        )

        hug_gif = random.choice(gifs.hug)
        embed.set_image(url=hug_gif)
        await ctx.send(embed=embed)

    @commands.command(
        brief=f"nickogólnydiscorda - całujesz wybranego użytkownika gifem"
    )
    async def kiss(self, ctx, user: discord.Member):
        embed = discord.Embed(
            title="",
            description=f"{ctx.author.mention} całuje {user.mention} prosto w usta!",
            color=ctx.author.color
        )

        kiss_gif = random.choice(gifs.kiss)
        embed.set_image(url=kiss_gif)
        await ctx.send(embed=embed)

    @commands.command(
        brief=f"nickogólnydiscorda - głaszczesz wybranego użytkownika gifem"
    )
    async def pat(ctx, user: discord.Member):
        embed = discord.Embed(
            title="",
            description=f"{ctx.author.mention} głaszcze {user.mention} po głowie ^^!",
            color=ctx.author.color
        )

        pat_gif = random.choice(gifs.pat)
        embed.set_image(url=pat_gif)
        await ctx.send(embed=embed)

    @commands.command(
        brief=f"nickogólnydiscorda - uderzasz wybranego użytkownika gifem"
    )
    async def slap(ctx, user: discord.Member):
        embed = discord.Embed(
            title="",
            description=f"{ctx.author.mention} uderza {user.mention} prosto w twarz!",
            color=ctx.author.color
        )

        slap_gif = random.choice(gifs.slap)
        embed.set_image(url=slap_gif)
        await ctx.send(embed=embed)

    @commands.command(
        brief=f"nickogólnydiscorda - przymilasz się do wybranego użytkownika gifem"
    )
    async def cuddle(self, ctx, user: discord.Member):
        embed = discord.Embed(
            title="",
            description=f"{ctx.author.mention} przymila się do {user.mention}!",
            # mention to oznaczenie/ping
            color=ctx.author.color
        )

        cuddle_gif = random.choice(gifs.cuddle)
        embed.set_image(url=cuddle_gif)
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Interactions(bot))
