import discord
import time

players = []
images = []

math = []
phys = []
eart = []
other = []

client = discord.Client()

# 생성된 토큰을 입력해준다.
token = "NzYxODQxNzg0MzYzMDI0Mzk0.X3gecw.4hkVYNCvHg_wdx9tA724PvEMKJo"

# 봇이 구동되었을 때 보여지는 코드
@client.event
async def on_ready():
    print("다음으로 로그인합니다")
    print(client.user.name)
    print(client.user.id)
    print("================")

# 봇이 특정 메세지를 받고 인식하는 코드
@client.event
async def on_message(message):
    # 메세지를 보낸 사람이 봇일 경우 무시한다
    if message.author.bot:
        return None

    if str(message.author) in players:
        link = str(message.attachments)
        if link == "[]":
            text = str(message.content)
            link = str(message.attachments)
            if str(message.channel) == "문제-등록":
                if text == "수학" or text == "물리" or text == "지구과학" or text == "기타":
                    code = text + " #" + str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))
                    ques_data = int(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))
                    if text == "물리":
                        ch_id = 761454137438371891
                        phys.append(ques_data)
                    if text == "수학":
                        ch_id = 761454054995525672
                        math.append(ques_data)
                    if text == "지구과학":
                        ch_id = 761454126437236747
                        eart.append(ques_data)
                    if text == "기타":
                        ch_id = 761955205272961044
                        other.append(ques_data)

                    embed = discord.Embed(title=code, color=0x62c1cc)
                    url = str(images[players.index(str(message.author))])

                    embed.set_image(url=url)
                    blow_chat = "@발신자: " + str(message.author)
                    embed.set_footer(text=blow_chat)

                    await message.channel.send(" > 성공적으로 문제를 등록했습니다.")
                    await client.get_channel(int(ch_id)).send(embed=embed)

                    del images[players.index(str(message.author))]
                    players.remove(str(message.author))

                elif text == "/취소":
                    if str(message.author) in players:
                        del images[players.index(str(message.author))]
                        players.remove(str(message.author))

                else:
                    if link == "[]":
                        await message.channel.send("잘못된 과목명입니다. 등록을 취소하려면 '/취소'를 입력하세요.")

            elif str(message.channel) == "답변-등록":
                if text == "/취소":
                    if str(message.author) in players:
                        del images[players.index(str(message.author))]
                        players.remove(str(message.author))
                else:
                    next_pass = 1
                    if int(text) in phys:
                        ch_id = 761454137438371891
                    elif int(text) in math:
                        ch_id = 761454054995525672
                    elif int(text) in eart:
                        ch_id = 761454126437236747
                    elif int(text) in other:
                        ch_id = 761955205272961044
                    else:
                        next_pass = 0
                        await message.channel.send("해당 문제번호는 존재하지 않는 번호입니다.")

                    if next_pass == 1:
                        title = "#" + str(text) + "의 답변"
                        embed = discord.Embed(title=title, color=0x62c1cc)
                        url = str(images[players.index(str(message.author))])

                        embed.set_image(url=url)
                        blow_chat = "@답변인: " + str(message.author)
                        embed.set_footer(text=blow_chat)

                        await message.channel.send(" > 성공적으로 답변을 등록했습니다.")
                        await client.get_channel(int(ch_id)).send(embed=embed)

                        del images[players.index(str(message.author))]
                        players.remove(str(message.author))


    link =str(message.attachments)
    if link != "[]":
        if str(message.channel) == "문제-등록":
            if str(message.author) in players:
                await message.channel.send("이미 등록을 준비하고 있는 문제나 답변이 있습니다. 전 활동을 취소하려면 './취소'를 입력하세요.")
            else:
                link = link.split("url='")
                url = link[1].split("'>]")

                images.append(url[0])
                players.append(str(message.author))
                await message.channel.send("올리실 과목명을 입력해 주세요.")
                await message.channel.send(" > 현재 지원하는 과목 : 수학, 물리, 지구과학, 기타")
        if str(message.channel) == "답변-등록":
            if str(message.author) in players:
                await message.channel.send("이미 등록을 준비하고 있는 문제나 답변이 있습니다. 전 활동을 취소하려면 './취소'를 입력하세요.")
            else:
                link = link.split("url='")
                url = link[1].split("'>]")

                images.append(url[0])
                players.append(str(message.author))
                await message.channel.send("올리실 답변의 번호를 입력해 주세요.")
                await message.channel.send(" > ex) 20201003232953")
    # if message.content.startswith('!안녕'):

client.run(token)