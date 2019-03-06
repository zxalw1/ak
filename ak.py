import asyncio
import discord
import random
import openpyxl
import datetime
import os

client = discord.Client()


token = "NTE0MDUyMDgyMjIzOTM5NTk3.DuKjsA.XZMJJVy_jJuBdH9mw4uZS8gKTUE"


@client.event
async def on_ready():
    print("Logged in as ")
    print(client.user.name)
    print(client.user.id)
    print("===========")
    
    
    await client.change_presence(game=discord.Game(name="부라보해병♬", type=2))


@client.event
async def on_message(message):
    if message.author.bot:
        return None

    id = message.author.id
    channel = message.channel

    if message.content.startswith('윤열아'): 
        await client.send_message(channel, '악!!!') 

    if message.content.startswith('골라'):
        choice = message.content.split(" ")
        choicenumber = random.randint(1, len(choice)-1)
        choiceresult = choice[choicenumber]
        await client.send_message(message.channel, choiceresult)

    if message.content.startswith('뭐먹지'):
        food = "자장면 돈가스 라면 초밥 치킨 피자 오므라이스 소갈비 햄버거 족발 밥이들어가냐? 굶어 털람보 김치찌개 된장찌개 삼겹살 곱창 막창 하혈 참치 찜닭 짬뽕 김밥"
        foodchoice = food.split(" ")
        foodnumber = random.randint(1, len(foodchoice))
        foodresult = foodchoice[foodnumber-1]
        await client.send_message(message.channel, foodresult)

    if message.content.startswith('도감번호'):
        food = "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133  134 135 136 137 138 139 140 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199 200 201 202 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 2262 227 228 229 230 231 232 233 234 235 236 237 238 239 240 241 242 243 244 245 246 247 248 249 250 251"
        foodchoice = food.split(" ")
        foodnumber = random.randint(1, len(foodchoice))
        foodresult = foodchoice[foodnumber-1]
        await client.send_message(message.channel, foodresult)

    if message.content.startswith('사랑의 전우조'):
        await client.send_message(channel, '축하드립니다악!!!')
        team = message.content[8:]
        peopleteam = team.split("/")
        people = peopleteam[0]
        team = peopleteam[1]
        person = people.split(" ")
        teamname = team.split(" ")
        random.shuffle(teamname)
        for i in range(0, len(person)):
            await client.send_message(message.channel, person[i] + "♥" + teamname[i])        
                                  
    if message.content.startswith('해병복무신조'):
        file = open("해병복무신조.")
        await client.send_message(message.channel,file.read())
        file.close()

    if "총장님" in message.content:
        file = openpyxl.load_workbook("경고.xlsx")
        sheet = file.active
        for i in range(1, 38):
            if str(sheet["A" + str(i)].value) == str(message.author.id):
                sheet["B" + str(i)].value = int(sheet["B" + str(i)].value) + 1
                break
            if str(sheet["A" + str(i)].value) == "~":
                sheet["A" + str(i)].value = str(message.author.id)
                sheet["B" + str(i)].value = 1
                break
        file.save("경고.xlsx")
        await client.send_message(message.channel, "님...? 님이라고 했어..?")

    if "조덕빤다" in message.content:
        file = openpyxl.load_workbook("경고.xlsx")
        sheet = file.active
        for i in range(1, 38):
            if str(sheet["A" + str(i)].value) == str(message.author.id):
                sheet["B" + str(i)].value = int(sheet["B" + str(i)].value) + 1
                break
            if str(sheet["A" + str(i)].value) == "~":
                sheet["A" + str(i)].value = str(message.author.id)
                sheet["B" + str(i)].value = 1
                break
        file.save("경고.xlsx")
        await client.send_message(message.channel, "그런거 빠는거 아닙니다.")

    if message.content.startswith('힘드네'):
        food = "고생했습니다악 뭐가힘드냨"
        foodchoice = food.split(" ")
        foodnumber = random.randint(1, len(foodchoice))
        foodresult = foodchoice[foodnumber-1]
        await client.send_message(message.channel, foodresult)

    if message.content.startswith("군번줄"):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="성명", value=message.author.name, inline=True)
        embed.add_field(name="별명", value=message.author.display_name, inline=True)
        embed.add_field(name="입대일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=True)
        embed.add_field(name="군번", value=message.author.id, inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith("투표"):
        vote = message.content[3:].split("/")
        await client.send_message(message.channel, "🎖투표 - " +  vote[0])
        for i in range(1, len(vote)):
            choose = await client.send_message(message.channel, "```" + vote[i] + "```")
            await client.add_reaction(choose, '👍')




access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
