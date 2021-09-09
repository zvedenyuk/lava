# Lava Lamp
This is my "lava lamp". I use my old iPad as a picture frame so that it shows beautiful "10 hours" videos.

Actually, this is just a webpage with fullscreen YouYube video. You can change videos remotely via Telegram bot.

## How it works

Open `index.php` in your web browser. It plays a YouTube video and also checks `videoId.txt` every 10 seconds via Ajax in background. To change video all you have to do is put new YouTube video ID in `videoId.txt`.

> N.B. You can get video ID of any video from its URL:
> For a video with URL https://www.youtube.com/watch?v=wnhvanMdx4s the video ID is ```wnhvanMdx4s```

## Telegram bot
Telegram bot uses WSGI so make sure your web server supports this interface (i.e. `mod_wsgi` is activated in Apache).
### Config 
1. Create your new Telegram bot via `@botfather` and insert bot token in file `telebot.wsgi` on this line:
```
TOKEN = '1234567890:XXXxxxXXXxxxXXXxxxXXXxxxXXXxxxXXXx' # PLACE YOUR TELEGRAM BOT TOKEN HERE!
```
2. Set webhook to your server via `setWebhook` command in Telegram. You can do it in Terminal:
```
$ curl -X POST -d '{"url":"https://YOU_WEBSERVER_URL/telebot.wsgi"}' -H "Content-Type: application/json" "https://api.telegram.org/botYOUR_BOT_TOKEN/setWebhook"
```
### Bot commands
Just send your bot any YouTube video URL and it will start playing on your "lava lamp".

Also,  supports some commands:
`/current` — Sends you current Lava video ID
`/list` — List these commands (you can change this message in `telebot.wsgi`)

Furthermore, you can just send bot a video ID with `/` in this format: `/wnhvanMdx4s`

## BONUS: Here are some beautiful long videos
```
/wnhvanMdx4s - Our planet from space
/aZ_rw6FDOAM - Lava lamp animation
/L_LUpnjgPso - Fireplace
/Pbzn79TSRO0 — Drone aerial views of Iceland
```









