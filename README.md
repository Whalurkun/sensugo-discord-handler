# sensugo-discord-handler

## SensuGo `Handlers` Docs
https://docs.sensu.io/sensu-go/5.11/reference/handlers/

# setup
1. Create a Discord webhook.
2. Create a new file called `discord-handler.json` in the sensu-backend, this will be your Sensu Handler
```json
{
  "type": "Handler",
  "api_version": "core/v2",
  "metadata": {
    "name": "discord",
    "namespace": "default"
  },
  "spec": {
    "command": "sensugo-discord-handler",
    "env_vars": [
      "WEBHOOK_URL=https://discordapp.com/api/webhooks/AAAAAA/BBBBBBBBBBB",
      "USERNAME=SensuGo",
      "ICON_URL=https://docs.sensu.io/images/sensu-logo-icon-dark@2x.png"
    ],
    "filters": [
      "is_incident",
      "not_silenced",
      "state_change_only"
    ],
    "handlers": [],
    "runtime_assets": [],
    "timeout": 0,
    "type": "pipe"
  }
}
```
3. Create the Sensu Handler from the file
```bash
sensuctl create --file discord-handler.json
```
