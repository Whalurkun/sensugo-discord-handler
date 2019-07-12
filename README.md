# sensugo-discord-handler
Get status updates from SensuGo directly in Discord!

## Setup <sup>(`B`ackend `A`gent)</sup>
0. `B` Clone the repository
```bash
git clone https://github.com/runarsf/sensugo-discord-handler.git
```
1. `B` Add it to path (in this example `/usr/local/bin`)
```bash
ln -s $(pwd)/sensugo-discord-handler.py /usr/local/bin/sensugo-discord-handler
```
2. Create a Discord Webhook
  * Open Discord (Desktop / Web, not currently available on mobile app) and navigate to the channel you want the status messages to be posted in
  * Click `Edit Channel` > `Webhooks` > `Create Webhook`
  * Name the webhook something recognizable, the name will only matter when managing it, as the name visible in chat will be provided by the script.
  * Same goes for the icon, the script will provide a custom one.
  * Take note of the `WEBHOOK URL`, you will need it later (you can view it at any time).
3. `B` Modify `handler.json` file to match your setup.
  * `spec` > `command`: Full path or script registered in path.
  * `spec` > `filters`: Conditions for which events to trigger the handler.
  * `spec` > `env_vars`[`WEBHOOK_URL`]: The URL you got when creating the webhook.
  * `spec` > `env_vars`[`USERNAME`]: The display name of the bot-user that posts the status messages. 
  * `spec` > `env_vars`[`ICON_URL`]: The icon of the bot-user that posts the status messages.
  * `spec` > `env_vars`[`USE_EMBED`]: Set to `true` to enable embedded messages, if set to anything else the script will generate a plain text table.
4. `B` Create the Handler from the file.
```bash
sensuctl create --file handler.json
# You should now have a new handler in your SensuGo WebUI
```
5. `B` Create/Update your check(s)
Add `discord` to the `handlers` array in your check, take a look at `check.json` for an example.
6. `B` (Re)create the Check from the file
```bash
sensuctl create --file check.json
```


## Running a manual test (requires the ENV var `WEBHOOK_URL`)
```bash
export WEBHOOK_URL=https://discordapp.com/api/webhooks/AAAAAA/BBBBBBBBB
cat example.json | ./sensugo-discord-handler
```
You can also remove the `spec` > `filters` array from `handler.json` and recreate the handler to get it to run every time a check assigned to it runs.


## SensuGo Handler Docs
https://docs.sensu.io/sensu-go/5.11/reference/handlers/<br>
Note: SensuGo handlers are run on the Backend, not on the Agent.


## Screenshots
![USE_EMBED=False](https://i.runarsf.dev/xMmvcP3bjw.png)
![USE_EMBED=True](https://i.runarsf.dev/9zTfL5tzkT.png)
![SensuGo Dashboard](https://i.runarsf.dev/tVArSKgBHs.png)


> **sensugo-discord-handler** © [runarsf](https://github.com/runarsf) · Author and maintainer.<br>
> Released under the [MIT](https://github.com/runarsf/sensugo-discord-handler/blob/master/LICENSE) License.
