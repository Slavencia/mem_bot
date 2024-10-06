import discord
import requests
from discord.ext import commands
import os
import random
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='?',  intents=intents)
print(os.listdir('picture')) 


@bot.command()
async def mem(ctx):
    list_images = os.listdir("images")  
    randomlist_images = random.choice(list_images)

    with open(f'images/{randomlist_images}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

@bot.command()
async def rofl(ctx):
    list_picture = os.listdir("picture")  
    randomlist_picture = random.choice(list_picture)

    with open(f'picture/{randomlist_picture}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)





def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)



def get_dog_image_url():
    url = "https://random.dog/woof.json"
    res = requests.get(url)
    data = res.json()
    return data["url"]

@bot.command("dog")
async def dog(ctx):
     
    image_url = get_dog_image_url()
    await ctx.send(image_url)     

def get_fox_image_link():
    link = "https://randomfox.ca/floof/"
    res = requests.get(link)
    data = res.json()
    return data["link"]

@bot.command("fox")
async def fox(ctx):
     
    image_link = get_fox_image_link()
    await ctx.send(image_link)  

def get_random_pokemon_image_link():
    # Получаем случайного покемона
    pokemon_index = random.randint(1, 898)  # PokeAPI имеет 898 покемонов
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_index}/"
    res = requests.get(url)
    data = res.json()

    # Получаем имя и изображение покемона
    pokemon_name = data['name']
    pokemon_image_url = data['sprites']['front_default']

    return pokemon_name, pokemon_image_url

@bot.command("pokemon")
async def pokemon(ctx):
    pokemon_name, image_link = get_random_pokemon_image_link()
    await ctx.send(f"{pokemon_name.capitalize()}:\\n{image_link}")


bot.run('') 
  
