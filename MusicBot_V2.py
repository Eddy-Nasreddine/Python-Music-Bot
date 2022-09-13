import string
import yt_dlp
import validators
import discord
from discord.ext import commands
from youtube_search import YoutubeSearch 
from math import fabs
from traceback import print_tb
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = commands.Bot(command_prefix="!", intents=intents)
song_queue = []
accepted_guilds = ["ABES MOM"]
ydl_opts = {'format': 'bestaudio/best'}
ffmpeg_options = {'options': '-vn',
                  'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5'}


@client.event
async def on_ready():
    pass


def valid_url(songname):
    valid = validators.url(songname)
    if valid:
        return songname
    else:
        results = YoutubeSearch(str(songname), max_results=1).to_dict()
        prefix = "https://www.youtube.com" + results[0]["url_suffix"]
        return prefix
    
    
def song_name(songname):
    result = YoutubeSearch(str(songname), max_results=1).to_dict()
    return result[0]["title"]


def song_duration(songname):
    result = YoutubeSearch(str(songname), max_results=1).to_dict()
    return result[0]["duration"]

    
    
swap = False
@client.command()
async def play(ctx, *, song):
    global swap
    if len(song_queue) != 0 & swap is False:
        song_queue.pop(0)
        swap = True
    channel = ctx.message.author.voice.channel
    if ctx.author.voice:
        if ctx.voice_client:
            voice_status = discord.utils.get(client.voice_clients, guild=ctx.guild)
            if voice_status.is_playing() or voice_status.is_paused():
                song_queue.append(valid_url(song))
            else:
                song_queue.append(valid_url(song))
                voice = ctx.voice_client
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    song_info = ydl.extract_info(valid_url(song_queue[0]), download=False)
                voice.play(discord.FFmpegPCMAudio(song_info["url"], **ffmpeg_options),after=lambda x=None: song_seq(ctx))
                await ctx.send(f"```Now playing {song_name(song_queue[0])} [{song_duration(song_name)}]```")
        else:
            song_queue.append(valid_url(song))
            voice = await channel.connect()
            print(voice)
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                song_info = ydl.extract_info(valid_url(song_queue[0]), download=False)
            voice.play(discord.FFmpegPCMAudio(song_info["url"], **ffmpeg_options),after=lambda x=None: song_seq(ctx))
            await ctx.send(f"```Now playing {song_name(song_queue[0])} [{song_duration(song_name)}]```")
    else:
        await ctx.send("```Must be in a voice channel to use this command```")


def song_seq(ctx):
    global swap
    if len(song_queue) != 0:
        song_queue.pop(0)
    voice = ctx.voice_client
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        song_info = ydl.extract_info(valid_url(song_queue[0]), download=False)
    if swap is True:
        swap = False
    voice.play(discord.FFmpegPCMAudio(song_info["url"], **ffmpeg_options),after=lambda x=None: song_seq(ctx))
    ctx.send(f"```Now playing {song_name(song_queue[0])} [{song_duration(song_name)}]```")


@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    elif voice.is_paused():
        await ctx.send("```Audio is already paused.```")
    else:
        await ctx.send("```No audio is currently playing.```")


@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    elif voice.is_playing():
        await ctx.send("```Audio is already playing.```")
    else:
        await ctx.send("```No audio is currently playing.```")
    

@client.command()
async def stop(ctx):
    song_queue = 0
    if ctx.voice_client:
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send("```Bot is not currently not in a voice channel.```")


@client.command()
async def skip(ctx):
    if len(song_queue) <= 1:
        await ctx.send("```No song is next in queue for skip command to be used```")
    else:
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        voice.stop()
        await play(song_queue[0])


@client.command()
async def queue(ctx): 
    song = " "*14 + "Song Queue" + "\n" + "-"*40
    for songs in song_queue:
        song += "\n"
        song += song_name(songs)
    await ctx.send(f"```{song}```")
        

client.run('ODk1NTUwNjM2NTEzNDU2MTQ4.YV6Mhg.kLla92IQKftCFBCKnShmf2Cmey8')
