import discord
import json
import random as rnd
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio


class MyClient(discord.Client):
    bot = commands.Bot(command_prefix='!', description='Hi')
    @bot.event
    async def on_ready(self):
        activity = discord.Game(name="dbr!help || Para mas info")
        await client.change_presence(status=discord.Status.idle, activity=activity)
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        canal = message.channel
        pr = '!'
        
        async def gifs(tt, img, hex):
        	embed = discord.Embed(color=hex)
        	embed.title='{0}'.format(tt)
        	embed.set_image(url=img)
        	await message.channel.send(embed=embed)
        
        Llorar=['https://media1.tenor.com/images/95dfdbe52b9199f1e4df0d3748b3e3a4/tenor.gif?itemid=12248925', 'https://i.pinimg.com/originals/6c/82/d7/6c82d7e71bf807b6ff35f5051077f69e.gif']
        Pegar=['']
        Adios=['https://media.tenor.com/images/e30c134e12153943c0f829302c7173cd/tenor.gif']
        Besar=['https://i.pinimg.com/originals/aa/64/8f/aa648fa14f1b305d677b9bca073f275a.gif', 'https://media1.tenor.com/images/8a47f33179692c1a3e3cf8a12324b93b/tenor.gif?itemid=5047638']
        Enfadado=['https://thumbs.gfycat.com/NewUntidyAntbear-size_restricted.gif']
        Reir=['https://media1.tenor.com/images/2f2139a6705e396fc1cc3c3a3bbcaa81/tenor.gif?itemid=13164713','https://media.tenor.com/images/665f6e56ff454aba36e1e8e922835de5/tenor.gif']
        Kamehameha=['https://static.vix.com/es/sites/default/files/u/ultra-instinto-dragon-ball.gif','https://media.tenor.com/images/750f392fa23577ae8bafec2c49c9934c/tenor.gif']
        Cargar_Genkidama=['https://i.pinimg.com/originals/da/c9/51/dac951cdf125995d0860b4d89af8422f.gif']
        Dar_Energia_Genkidama=['https://media1.tenor.com/images/57bfcd575a507b7d53ab5de7d5112497/tenor.gif?itemid=14084570']
        Lanzar_Genkidama=['https://thumbs.gfycat.com/DearestMasculineDeinonychus-size_restricted.gif']
        Omega_Crush_Cannon=['https://i.pinimg.com/originals/a0/7c/2c/a07c2caa7cad810fce3484db7522311d.gif']
        Ki_Sword=['https://steamuserimages-a.akamaihd.net/ugc/859488250480753616/D63C7E0708F860208927B888B611B1FB9CFE2041/']
        Ki_Charge=['https://24.media.tumblr.com/tumblr_mcf0jn7LYc1rjb7v5o1_500.gif']
        Bolas_Tierra=['https://media.tenor.com/images/33568ff26a1ee0b33b6ac5a84fc70b49/tenor.gif']
        Bolas_Namek=['https://pa1.narvii.com/6271/14675cf6454d1bb095197bc1e75b90a02aa1294a_hq.gif']
        SDB=['https://pa1.narvii.com/6248/d0c0e26c87176ea9c085b535dfddb45072c04925_hq.gif']
        Radar=['https://thumbs.gfycat.com/MagnificentFreshHamadryad-small.gif']
        FKamehameha=['https://media.tenor.com/images/29402f2e78feab81245d7a692d4527af/tenor.gif']
        Fusion_Meta=['https://media.tenor.com/images/7d3d538ff1e150ede9e2e01f035dce50/tenor.gif']
        Fusion_Potara=['https://media.tenor.com/images/a0abb8c69ca6e3baebe0215b9fd0809c/tenor.gif']
        chistes=['Dragon ball segun las madres....\n\nKrillin->El kokun pelon\nYamcha->El kokun que no sirve para nada\nVegeta->El kokun rabioso\nRaditz->El kokun con pelo largo\nGoku->El bicho de pelos parados\n\nTrue story', 'Piccolo: Oye vegeta, ¿Alguna vez has derrotado a goku?\nVegeta: Claro que si\nPiccolo: ¿Como?\nVegeta: Siendo buen padre\nPiccolo: Jaja yo tambien', 'La gente gorda no existe, solo es una mala fusion', '~Papa, soy lesbiana\n+¡¿Que?!\n*Yo tambien\n+¡Mierda! ¿Acaso a nadie de esta casa le gustan los hombres?\n#¡¡A mi!!\n+Tu callate, Trunks','Vegeta enseñandole hablar a Trunks\n\nVegeta: Trunks, di papa\nTrunks: Mama!\nVegeta: No Trunks, di papa\nTrunks:Mama!\nVegeta: Mierda! Solo di papa!\nTrunks: Mierda!\nVegeta: ¡¿QUE?!\nTrunks: Mierda!\nBulma: Cariño, ya llegue\nTrunks: Mierda!\nBulma: !¿DE QUIEN APREBDISTE ESO?!\nTrunks: Papa!\nVegeta: Asi me gusta hijo!', 'Vegeta: Oye Piccolo!\nPiccolo: ¿Que quieres?\nVegeta: Soy mas fuerte que tu insecto\nPiccolo: Puede ser, pero hice algo que tu no. Mate a Goku\nVegeta: Arj! Maldito insecto verde!', 'Goku: Vegeta, ¿Cual es la altura de la estupidez?\nVegeta: No se...¿Cuanto mides?', 'Logica de DBZ: Seras mas poderoso cuando te crezca el pelo\n Pobrecito krillin', 'En una entrevista de trabajo....\n\n¿Nivel de ingles?\nAlto\nTraduzca congelador\nFreezer\nUselo en una oracion\nGOKU MATO A FREEZER!!\n¡CONTRATADO!', 'No entiendo como es que a shenron no le molesta que a cada rato le toquen las bolas']
        
        
        
        
        if message.content== pr+'ssj':
        	await canal.send('https://media3.giphy.com/media/ul1omlrGG6kpO/giphy.gif')
        elif message.content==pr+'ssj2':
        	await canal.send('https://i.pinimg.com/originals/ac/08/0c/ac080c5f261dd1a8f17fdbc5161a844b.gif')
        elif message.content==pr+'ssj3':
        	await canal.send('https://media1.tenor.com/images/ca7e2ccc2a1fe6ac0433a7bc77292327/tenor.gif?itemid=9285424')
        elif message.content==pr+'ssj4':
        	await canal.send('https://i.pinimg.com/originals/ea/39/cf/ea39cf119f0e9030a5a088485d3dbc5f.gif')
        elif message.content==pr+'ssg':
        	await canal.send('https://media1.tenor.com/images/189b1a69c31896b344f786b1a2a21c10/tenor.gif?itemid=13930578 ')
        elif message.content==pr+'ssgss':
        	await canal.send('https://i.imgur.com/671cJE4.gif')
        elif message.content==pr+'ssgsse':
        	await canal.send('https://media1.tenor.com/images/3f4b6fbb2845a839cdcd49aac09e20e9/tenor.gif?itemid=14096231')
        elif message.content==pr+'ssgsskk':
        	await canal.send('https://media1.tenor.com/images/476cf941c244eecada94b2cb49b0d9ad/tenor.gif?itemid=14667162')
        elif message.content==pr+'mng':
        	await canal.send('{0.author.mention} se ha convertido en ultra instinto\nhttps://media1.tenor.com/images/f06657ea7a56f1b397a340a2c789a19f/tenor.gif?itemid=11395844'.format(message))
        elif message.content==pr+'ozaru':
          await canal.send('https://pa1.narvii.com/6826/23c718e1d186a7e5d87c7acf6246ea3192d8ab81_hq.gif')
        elif message.content==pr+'g-ozaru':
          await canal.send('https://pa1.narvii.com/6794/03fe921af1d760edf1088d49622d693787cb1fd2_hq.gif')
        elif message.content==pr+'reir':
          await canal.send(rnd.choice(Reir))
        elif message.content==pr+'omegacc':
        	await canal.send(rnd.choice(Omega_Crush_Cannon))
        elif message.content==pr+'kiswrd':
        	await canal.send(rnd.choice(Ki_Sword))
        elif message.content==pr+'kicharge':
        	await canal.send(rnd.choice(Ki_Charge))
        elif message.content==pr+'llorar':
        	await gifs('**'+str(message.author.name)+'** se ha puesto a llorar', rnd.choice(Llorar), 0xFF000)
        elif message.content==pr+'adios':
        	msg = '{0.author.mention} se ha teletransportado, hasta la proxima'.format(message)+'\n'+rnd.choice(Adios)
        	
        	await canal.send(msg)
        elif message.content=='dbr'+pr+'invite':
        	await canal.send('https://discord.com/oauth2/authorize?client_id=739522516988723290&scope=bot&permissions=8')
        elif message.content==pr+'creator':
        	await canal.send('Mi creador es: <@591987380853145610>')
        elif message.content==pr+'chiste':
        	await canal.send(rnd.choice(chistes))
        elif message.content=='dbr!'+'help':
        	await canal.send("__**LISTA DE COMANDOS**__\n!ssj->Gif super saiyan\n!ssj2->Gif super saiyan 2\n!ssj3->Gif super saiyan 3\n!ssg->Gif super saiyan god\n!ssgss->Gif super saiyan blue\n!ssgsse->Gif super saiyan blue evolution\n!ssgsskk->Gif super saiyan blue kaioken\n!mng->Gif ultra instinto\n!ozaru->Gif ozaru\n!g-ozaru->Gif ozaru dorado\n!ssrose->Gif super saiyan rose\n!reir->Gif reir\n!chiste->Te cuento un chiste\n!kiswrd->Gif espada de ki\n!kicharge->Gif carga de ki\n!omegacc->Gif omega crush cannon\n\ndbr!invite->Link para invitarme a tu server :)")
          


client = MyClient()

client.run('NzM5NTIyNTE2OTg4NzIzMjkw.XybsAw.hjIe-yPPzdDaep8muw_aDVvEXcA')