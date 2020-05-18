#-*-coding: UTF-8-*-
import discord


class Help:
    def create_help_embed(self):
        embed = discord.Embed(title="Discord 음악봇입니다",description="Rythm 이 몇번씩 터져서 화가나서 만든 봇입니다.", color=0xf7cac9)
        embed.add_field(name = '-재생 [제목] or [링크]', value = '음악을 재생합니다. 만약 재생중이면 예약이 자동으로 됩니다',inline = False)
        embed.add_field(name='-큐', value='현재 재생되고 있는 노래와 예약된 곡들이 저장된 큐를 출력합니다', inline=False)
        embed.add_field(name='-스킵', value='현재 재생되고 있는 노래를 스킵할 수 있으며 음성방 에 과반수가 동의해야 가능 합니다. 관리자는 바로 스킵할 수 있습니다.', inline=False)
        return embed