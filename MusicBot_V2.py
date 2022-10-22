import asyncio
from pprint import pprint
import yt_dlp
import validators
import time
import discord
from discord.ext import commands
from youtube_search import YoutubeSearch 
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = commands.Bot(command_prefix="$", intents=intents)
ydl_opts = {'format': 'bestaudio/best'}
ffmpeg_options = {'options': '-vn',
                  'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5'}

# TODO Volume mixing (All sounds have the same respective volume)
# TODO Error handling 
# TODO Youtube Playlists 
# TODO Spotify & Sounds cloud Integeration 
# TODO Clean up code 


# [[song_url], [song_name]]
guilds = {}


@client.event
async def on_ready():
    pass


@commands.is_owner()
@client.command()
async def nsfw(ctx,*,song):
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        song_info = ydl.extract_info(song, download=False) 
    voice.play(discord.FFmpegPCMAudio(song_info["url"], **ffmpeg_options))

    
def song_infooooo(songname):  
    valid = validators.url(songname)
    results = YoutubeSearch(str(songname), max_results=1).to_dict()
    if valid:
        results[0]["url_suffix"] = songname 
        return results[0]
    else:
        results[0]["url_suffix"] = "https://www.youtube.com" + results[0]["url_suffix"]
        return results[0]
    

def embed_music(ctx, song, song_state, embed_colour):
    song_information = song_infooooo(song)
    song_name = song_information["title"]
    song_duration = song_information["duration"]
    song_url = song_information["url_suffix"]
    song_thumbnail = song_information["thumbnails"][0]
    music_embed = discord.Embed(
    title = song_state,
    description = f"[{song_name} [{song_duration}]]({song_url})",
    colour= embed_colour
    )
    music_embed.set_footer(text = f"Added by {ctx.author}", icon_url= ctx.author.avatar)
    music_embed.set_thumbnail(url= str(song_thumbnail))
    return music_embed


swap = False
@client.command()
async def play(ctx, *, song):
    if (ctx.guild.id) not in guilds:
        guilds[ctx.guild.id] = [[], []]
    global swap
    if len(guilds[(ctx.guild.id)][0]) != 0 & swap is False:
        guilds[(ctx.guild.id)][0].pop(0)
        guilds[(ctx.guild.id)][1].pop(0)
        swap = True
    song_information = song_infooooo(song)
    song_url = song_information["url_suffix"]
    song_name = song_information["title"]
    channel = ctx.message.author.voice.channel
    if ctx.author.voice:
        if ctx.voice_client:
            voice_status = discord.utils.get(client.voice_clients, guild=ctx.guild)
            if voice_status.is_playing() or voice_status.is_paused():
                guilds[(ctx.guild.id)][0].append([song_url, ctx])
                guilds[(ctx.guild.id)][1].append(song_name)
                await ctx.send(embed = embed_music(ctx, guilds[(ctx.guild.id)][0][-1][0], "Added to Queue", discord.Colour.red()))
            else:
                guilds[(ctx.guild.id)][0].append([song_url, ctx])
                guilds[(ctx.guild.id)][1].append(song_name)
                voice = ctx.voice_client
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    song_info = ydl.extract_info(guilds[(ctx.guild.id)][0][0][0], download=False)
                await ctx.send(embed = embed_music(guilds[(ctx.guild.id)][0][0][1], guilds[(ctx.guild.id)][0][0][0], "Now Playing", discord.Colour.blue()))
                voice.play(discord.FFmpegPCMAudio(song_info["url"], **ffmpeg_options),after=lambda x=None: song_seq(ctx))
        else:
            guilds[(ctx.guild.id)][0].append([song_url, ctx])
            guilds[(ctx.guild.id)][1].append(song_name)
            voice = await channel.connect()
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                song_info = ydl.extract_info(guilds[(ctx.guild.id)][0][0][0], download=False)
            await ctx.send(embed = embed_music(guilds[(ctx.guild.id)][0][0][1], guilds[(ctx.guild.id)][0][0][0], "Now Playing", discord.Colour.blue()))
            voice.play(discord.FFmpegPCMAudio(song_info["url"], **ffmpeg_options),after=lambda x=None: song_seq(ctx))
    else:
        await ctx.send("```Must be in a voice channel to use this command```")
                
            
def song_seq(ctx):
    global swap
    swap = True
    if len(guilds[(ctx.guild.id)][0]) != 0:
        guilds[(ctx.guild.id)][0].pop(0)
        guilds[(ctx.guild.id)][1].pop(0)
        if (len(guilds[(ctx.guild.id)][0])) != 0:
            voice = ctx.voice_client
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                song_info = ydl.extract_info(guilds[(ctx.guild.id)][0][0][0], download=False)
            channel = client.get_channel(ctx.channel.id)
            client.loop.create_task(channel.send(embed = embed_music(guilds[(ctx.guild.id)][0][0][1], guilds[(ctx.guild.id)][0][0][0], "Now Playing", discord.Colour.blue()))) 
            voice.play(discord.FFmpegPCMAudio(song_info["url"], **ffmpeg_options),after=lambda x=None: song_seq(ctx))
        else:
            client.loop.create_task(dc(ctx, 2))
            pass


@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
        client.loop.create_task(dc(ctx, 5))
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
    guilds[(ctx.guild.id)] = [[], []]
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if ctx.voice_client:
        voice.stop()
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send("```Bot is not currently not in a voice channel.```")


@client.command()
async def skip(ctx):
    if len(guilds[(ctx.guild.id)][0]) <= 1:
        await ctx.send("```No song is next in queue for skip command to be used```")
    else:
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        voice.stop()
        play(guilds[(ctx.guild.id)][0][0])


@client.command()                                                                                                                      
async def queue(ctx):
    song = ""
    for i in range(len(guilds[((ctx.guild.id))][0])):
        song_url = guilds[(ctx.guild.id)][0][i][0]
        song_name = guilds[(ctx.guild.id)][1][i]
        print(guilds[(ctx.guild.id)][0][0])
        print(song_url)
        if i == 0:
            song += f"Now Playing :headphones:: \n"
            song += f"[{song_name}]({song_url}) \n\n"
        elif i == 1:
            song += f"Up Next :track_next::\n"
            song += f"{i}: [{song_name}]({song_url}) \n"
        else:
            song += f"{i}: [{song_name}]({song_url}) \n"
    music_embed = discord.Embed(
    title = f"Song Queue ({len(guilds[((ctx.guild.id))][0])})",
    description = song,
    colour = discord.Color.blurple()
    )
    music_embed.set_footer(text = f"Requested by {ctx.author}", icon_url= ctx.author.avatar)
    await ctx.send(embed = music_embed)
    
async def dc(ctx, time):
    time *= 60
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    counter = 0
    while not voice.is_playing():
        counter += 1
        await asyncio.sleep(1)
        if counter == time:
            await ctx.guild.voice_client.disconnect()
            return
        

client.run('ODk1NTUwNjM2NTEzNDU2MTQ4.YV6Mhg.kLla92IQKftCFBCKnShmf2Cmey8')

