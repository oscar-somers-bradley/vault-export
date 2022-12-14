#!/usr/bin/env python3

import requests
import argparse
import urllib3
import re
from os import linesep, remove

from ruamel.yaml import YAML
from ruamel.yaml.scalarstring import PreservedScalarString as pss
from ruamel.yaml.representer import RoundTripRepresenter
yaml = YAML()



parser = argparse.ArgumentParser(description='This program is used to export secrets from vault that are using \n'
                                             'a version below 0.10.0, if you have a version above\n'
                                             'please use https://github.com/jonasvinther/medusa')

parser.add_argument('-t', '--token',
                    help="Vault token", required=True)

parser.add_argument('-d', '--destination',
                    help="Url to the vault server", required=True)

parser.add_argument('-l', '--list',
                    help="This will list all the secrets within a folder", action='store_true')

# Variables:

# disable ssl warning in output
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
args = parser.parse_args()
url = args.destination
token = args.token
custom_method = 'LIST'
payload = {'X-Vault-Token': token}
# disable cert checking for requests
unsecure = False

# Classes

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Functions

def repr_str(dumper: RoundTripRepresenter, data: str):
    if '\n' in data:
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)

def list_secrets():
    try:
        resp_list = requests.request(custom_method, url=url, headers=payload, verify=unsecure)
        resp_list.raise_for_status()
        list_json = resp_list.json()
        items = []
        for key, value in list_json.items():
            if key == 'data':
                items.append(value)
                items = items[0]['keys']
        return items
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


def read_secret(key):
    try:
        resp_get = requests.get(url=url + key, headers=payload, verify=unsecure)
        resp_get.raise_for_status()
        list_json = resp_get.json()
        items = []
        for key, value in list_json.items():
            if key == 'data':
                items.append(value)
        return items
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

def main ():
    yaml.representer.add_representer(str, repr_str)

    # Print list
    if args.list:
        print(list_secrets())
        exit(0)
    output_list_json = list_secrets()
    initial_list = []
    sub_folder_list = []
    # Loop to remove unwanted sub-folders
    for i in output_list_json:
        if i.find("/") != -1:
            sub_folder_list.append(i)
        else:
            initial_list.append(i)
    # Set temp file object
    secrets_file = 'secrets.yml'
    f = open(secrets_file, "w")

    # Main loop
    for i in initial_list:
        f.write(i + ":" + linesep)
        secrets = read_secret(i)
        yaml.dump(secrets, f)

    with open(secrets_file, 'r') as f:
        secrets_data = f.read()
    # Doesn't cover all cases, could need some work
    secrets_data = re.sub(r'^-(.*)', r' \1', secrets_data, flags=re.M)
    # For empty values medusa uses {} instead of ''
    secrets_data = secrets_data.replace('\'\'', '{}')
    # Remove the extra blank line
    secrets_data = secrets_data[:secrets_data.rfind('\n')]

    # delete temp file
    remove(secrets_file)
    print(secrets_data)
    if not sub_folder_list:
        pass
    else:
        print(bcolors.WARNING + "\n The Destination folder contains the following sub-folders: \n" + bcolors.ENDC)
        print(sub_folder_list)
        print(bcolors.WARNING + "\n Please make sure to export these separately" + bcolors.ENDC)

if __name__ == "__main__":
    main()
