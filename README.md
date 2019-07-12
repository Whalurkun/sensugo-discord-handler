# sensugo-discord-handler

## SensuGo `Handlers` Docs
https://docs.sensu.io/sensu-go/5.11/reference/handlers/

## Running a manual test
```bash
cat example.json | ./sensugo-discord-handler
```

# setup
1. Create a Discord webhook.
2. Create a new file called `discord-handler.json` in the sensu-backend, this will be your Sensu Handler
3. Create the Sensu Handler from the file
```bash
sensuctl create --file discord-handler.json
```
