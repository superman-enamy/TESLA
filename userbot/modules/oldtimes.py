from telethon import events
from userbot.events import register
from userbot import CMD_HELP

normiefont = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
oldeng = ['𝔞', '𝔟', '𝔠', '𝔡', '𝔢', '𝔣', '𝔤', '𝔥', '𝔦', '𝔧', '𝔨', '𝔩', '𝔪', '𝔫', '𝔬', '𝔭', '𝔮', '𝔯', '𝔰', '𝔱', '𝔲', '𝔳', '𝔴', '𝔵', '𝔶', '𝔷']



@register(outgoing=True, pattern="^.oldeng(?: |$)(.*)")
async def oldy(event):

    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text   
    if not args:
        await event.edit("`What, I am Supposed To Work with text only`")
        return
    string = '  '.join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
           oldycharacter = oldyfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, oldycharacter)
    await event.edit(string)
CMD_HELP.update({
"oldengfont":
"old eng font \
\nUse:- .oldeng (text)"
})
