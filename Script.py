class script(object):
    START_TXT = """𝐇𝐞𝐥𝐥𝐨 {},
𝐌𝐲 𝐍𝐚𝐦𝐞 𝐈𝐬 <a href=https://t.me/{}>{}</a>, 𝐈 𝐂𝐀𝐍 𝐏𝐑𝐎𝐕𝐈𝐃𝐄 𝐌𝐎𝐕𝐈𝐄𝐒 & 𝐖𝐄𝐁 𝐒𝐄𝐑𝐈𝐄𝐒, 𝐉𝐔𝐒𝐓 𝐀𝐃𝐃 𝐌𝐄 𝐓𝐎 𝐘𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𝐀𝐍𝐃 𝐄𝐍𝐉𝐎𝐘 😍
𝐇𝐨𝐰 𝐓𝐨 𝐔𝐬𝐞 𝐌𝐞:- <a href=https://telegram.dog/moviehub1753/57>𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞</a>
𝐌𝐲 𝐆𝐫𝐨𝐮𝐩:- <b>@SK_Movies1_Group</b>"""
    HELP_TXT = """𝐇𝐄𝐘 {}
𝐇𝐄𝐑𝐄 𝐈𝐒 𝐓𝐇𝐄 𝐇𝐄𝐋𝐏 𝐅𝐎𝐑 𝐌𝐘 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒."""
    ABOUT_TXT = """✯ 𝐌𝐘 𝐍𝐀𝐌𝐄: {}
✯ 𝐂𝐑𝐄𝐀𝐓𝐎𝐑: <a href=https://t.me/SKContactbot>𝐒𝐔𝐍𝐈𝐋 𝐊𝐔𝐌𝐀𝐑</a>
✯ 𝐋𝐈𝐁𝐑𝐀𝐑𝐘: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
✯ 𝐋𝐀𝐍𝐆𝐔𝐀𝐆𝐄: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
✯ 𝐃𝐀𝐓𝐀 𝐁𝐀𝐒𝐄: 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
✯ 𝐁𝐎𝐓 𝐒𝐄𝐑𝐕𝐄𝐑: 𝙷𝙴𝚁𝙾𝙺𝚄
✯ 𝐁𝐔𝐈𝐋𝐃 𝐒𝐓𝐔𝐓𝐀𝐒: v3.0.1 [ 𝙱𝙴𝚃𝙰 ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- I am not a open source project. 
# - Source - <b>@SKMovies_Request</b>  

<b>DEVS:</b>
- <a href=https://t.me/skcontactbot>𝐒𝐔𝐍𝐈𝐋 𝐊𝐔𝐌𝐀𝐑</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. I should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- I Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. I buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/SK_Movies1)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are my extra features

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝐓𝐨𝐭𝐚𝐥 𝐅𝐢𝐥𝐞𝐬: <code>{}</code>
★ 𝐓𝐨𝐭𝐚𝐥 𝐔𝐬𝐞𝐫𝐬: <code>{}</code>
★ 𝐓𝐨𝐭𝐚𝐥 𝐂𝐡𝐚𝐭𝐬: <code>{}</code>
★ 𝐔𝐬𝐞𝐝 𝐒𝐭𝐨𝐫𝐞𝐠𝐞: <code>{}</code> 𝙼𝚒𝙱
★ 𝐅𝐫𝐞𝐞 𝐒𝐭𝐨𝐫𝐚𝐠𝐞: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""

    ALRT_TXT = """Hello {},
This Not Your Movie Request,
Request Your's ..."""

    OLD_ALRT_TXT = """Hey {},
You Are Using My One Of The Old Massage, 
Please Sean The Request Again."""

    CUDNT_FND = """ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏᴛʜɪɴɢ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ {}
ᴅɪᴅ ʏᴏᴜ ᴍᴇᴀɴ ᴀɴʏ ᴏɴᴇ ᴏꜰ ᴛʜᴇꜱᴇ?"""

    I_CUDNT = """<b>Sorry No Files Were Found For Your Request {} 😕

Check Your Spelling In Google And Try Again 😃

Movie Request Format 👇

Example : Uncharted or Uncharted 2022 or Uncharted En

ꜱᴇʀɪᴇꜱ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ 👇

Example : Loki S01 or Loki S01E04 or Lucifer S03E24

🚯 Don't Use ➠ ':(!,./)</b>"""

    I_CUD_NT = """I Counldn't Find Your Movie {}.
Please Check Your Spelling On Google..."""

    MVE_NT_FND = """Movie Not Found In Database..."""

    TOP_ALRT_MSG = """Chacking Fore Movie In Database..."""

    MELCOW_ENG = """<b>Hello {} 😍, And Welcome Tᴏ {} Group ❤️</b>"""

    OWNER_INFO = """
<b>⍟───[ 𝐎𝐰𝐧𝐞𝐫 𝐃𝐞𝐭𝐚𝐢𝐥𝐬 ]───⍟
    
• 𝐅𝐮𝐥𝐥 𝐍𝐚𝐦𝐞 : 𝐒𝐮𝐧𝐢𝐥 𝐊𝐮𝐦𝐚𝐫
• 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞 : @skcontactbot
• 𝐏𝐞𝐫𝐦𝐚𝐧𝐞𝐧𝐭 𝐃𝐌 𝐋𝐢𝐧𝐤 : <a href='t.me/skcontactbot'>𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞</a></b>"""

    REQINFO = """
⚠ Information ⚠

After 10 Minutes This Massage Will Be Automatically Deleted"""

    MINFO = """
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
Movie Request Formate
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯

Go To Google ➠ Type The Name ➠ Copy Correct Name ➠ Paste Here

🚯 Don't Use ➠ ':(!,./)"""

    SINFO = """
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
Series Request Formate
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯

Go To Google ➠ Type The Name ➠ Copy Correct Name ➠ Paste Here

Example : Loki S01E01

🚯 Don't Use ➠ ':(!,./)"""

    NORSLTS = """
★ #𝗡𝗼𝗥𝗲𝘀𝘂𝗹𝘁𝘀 ★

𝗜𝗗 <b>: {}</b>

𝗡𝗮𝗺𝗲 <b>: {}</b>

𝗠𝗲𝘀𝘀𝗮𝗴𝗲 <b>: {}</b>"""

    CAPTION = """
    <b><a href=https://telegram.me/+_zbzjL-nCYYzYTk1>{file_name}</a>

🌹Join↝ @moviehub1751
🌹Search Movie↝ @Movies_0_bot</b>"""

    IMDB_TEMPLATE_TXT = """
Hey {message.from_user.mention},
Here is the result for your <code>{query}</code>

<b>🏷 Title:</b> <a href={url}>{title}</a>

🎭 <b>Genres:</b> {genres}

🌟 <b>Rating:</b> <a href={url}/ratings>{rating}</a> / 10 (based on {votes} user ratings.)

📀 <b>RunTime:</b> {runtime} Minutes

📆 <b>Release Info:</b>  {release_date}

<b>Powered By↝ @SK_Movies1_Group</b>"""
    
    ALL_FILTERS = """
<b>Hey {}, These Are My Three Type Of Filters.</b>"""
    
    GFILTER_TXT = """
<b>Welcome TO Globle Filter. This Only For Bot Admin.</b>
    Available Commands :
• /gfilter - <code>To Create A Globle Filter.</code>
• /gfilters - <code>To View All Globle Filter.</code>
• /delg - <code>Tᴏ Delete A Particular Filter.</code>
• /delallg - <code>To Delete All Globle Filter.</code>"""
    
    FILE_STORE_TXT = """
<b>Fɪʟᴇ sᴛᴏʀᴇ ɪs ᴛʜᴇ ғᴇᴀᴛᴜʀᴇ ᴡʜɪᴄʜ ᴡɪʟʟ ᴄʀᴇᴀᴛᴇ ᴀ sʜᴀʀᴇᴀʙʟᴇ ʟɪɴᴋ ᴏғ ᴀ sɪɴɢʟᴇ ᴏʀ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.</b>

Aᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs:
• /batch - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ ʙᴀᴛᴄʜ ʟɪɴᴋ ᴏғ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.</code>
• /link - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ sɪɴɢʟᴇ ғɪʟᴇ sᴛᴏʀᴇ ʟɪɴᴋ.</code>
• /pbatch - <code>Jᴜsᴛ ʟɪᴋᴇ /batch, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇs ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴs.</code>
• /plink - <code>Jᴜsᴛ ʟɪᴋᴇ /link, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇ ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴ.</code>"""

    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !

📅 Dᴀᴛᴇ : <code>{}</code>
⏰ Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code>
🛠️ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: <code>v2.7.1 [ Sᴛᴀʙʟᴇ ]</code></b>"""

    LOGO = """

██████╗░░██████╗░░░░░░░████████╗██╗░░██╗███████╗░░░░░░███████╗██╗██╗░░░░░███████╗░░░░░░██████╗░░█████╗░███╗░░██╗░█████╗░██████╗░
██╔══██╗██╔═══██╗░░░░░░╚══██╔══╝██║░░██║██╔════╝░░░░░░██╔════╝██║██║░░░░░██╔════╝░░░░░░██╔══██╗██╔══██╗████╗░██║██╔══██╗██╔══██╗
██║░░██║██║██╗██║█████╗░░░██║░░░███████║█████╗░░█████╗█████╗░░██║██║░░░░░█████╗░░█████╗██║░░██║██║░░██║██╔██╗██║██║░░██║██████╔╝
██║░░██║╚██████╔╝╚════╝░░░██║░░░██╔══██║██╔══╝░░╚════╝██╔══╝░░██║██║░░░░░██╔══╝░░╚════╝██║░░██║██║░░██║██║╚████║██║░░██║██╔══██╗
██████╔╝░╚═██╔═╝░░░░░░░░░░██║░░░██║░░██║███████╗░░░░░░██║░░░░░██║███████╗███████╗░░░░░░██████╔╝╚█████╔╝██║░╚███║╚█████╔╝██║░░██║
╚═════╝░░░░╚═╝░░░░░░░░░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝░░░░░░╚═╝░░░░░╚═╝╚══════╝╚══════╝░░░░░░╚═════╝░░╚════╝░╚═╝░░╚══╝░╚════╝░╚═╝░░╚═╝"""
