#!/usr/bin/env python3
import os
import sys
import json
import requests

# sensuctl event info entity_name check_name --format json

def getHost(parser):
    if bool(parser['check']['proxy_entity_name']):
        return parser['check']['proxy_entity_name']
    else:
        return parser['entity']['metadata']['name']

def getStatus(ret):
    if ret == 0:
        return 'OK'
    elif ret == 1:
        return 'WARNING'
    elif ret == 2:
        return 'CRITICAL'
    else:
        return 'UNKNOWN'

if __name__ == "__main__":
    WEBHOOK_URL = str(os.environ.get('WEBHOOK_URL', ''))
    AVATAR_URL = str(os.environ.get('ICON_URL', 'https://docs.sensu.io/images/sensu-logo-icon-dark@2x.png'))
    USERNAME = str(os.environ.get('USERNAME', 'SensuGo'))

    piped = json.loads(''.join(sys.stdin.readlines()))

    host = getHost(piped)
    check = piped['check']['metadata']['name']
    output = str(piped['check']['output']).replace('\n', '')
    status = getStatus(piped['check']['status'])

    # Discord doesn't have tables, this is one way to solve it, another would be to use embeds
    dashes = len(max([str(host), str(check), str(output), str(status)], key = len)) + 2 # (16+2) (2 is for spaces)
    content = ('+--------+' + '-' * dashes + '+\n'
               '| Entity | '+ host + ' ' * (dashes - len(host) - 2) + ' |\n'
               '+--------+' + '-' * dashes + '+\n'
               '| Check  | '+ check + ' ' * (dashes - len(check) - 2) + ' |\n'
               '+--------+' + '-' * dashes + '+\n'
               '| Output | '+ output + ' ' * (dashes - len(output) - 2) + ' |\n'
               '+--------+' + '-' * dashes + '+\n'
               '| Status | '+ status + ' ' * (dashes - len(status) - 2) + ' |\n'
               '+--------+' + '-' * dashes + '+')

    data = {
        "username": USERNAME,
        "avatar_url": AVATAR_URL,
        "content": str('```\n' + content + '```')
    }

    # https://discordapp.com/developers/docs/resources/channel#embed-object
    data["embeds"] = []
    embed = {}
    embed["title"] = str(host)
    embed["description"] = content
    data["embeds"].append(embed)

    poster = requests.post(WEBHOOK_URL, data=json.dumps(data), headers={"Content-Type": "application/json"})

    try:
        poster.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(int(poster.status_code))
    else:
        print("Payload delivered successfully, code {}.".format(poster.status_code))
        sys.exit(0)
