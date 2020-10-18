#!/usr/bin/env python3

'''
Example custom dynamic inventory script for Ansible, in Python.
'''

import os
import sys
import argparse
import pprint

try:
    import json
except ImportError:
    import simplejson as json

class ExampleInventory(object):

    def __init__(self):
        self.inventory = {}
        self.read_cli_args()

        if self.args.verbose:
            self.inventory = self.example_inventory()
            pp = pprint.PrettyPrinter(indent=4)
            pp.pprint(self.args)
            pp.pprint(len(self.args.verbose))
        # Called with `--list`.
        if self.args.list:
            self.inventory = self.example_inventory()
        # Called with `--host [hostname]`.
        elif self.args.test:
            self.inventory = self.example_inventory()
        
        elif self.args.host:
            # Not implemented, since we return _meta info `--list`.
            self.inventory = self.empty_inventory()
        # If no groups or vars are present, return an empty inventory.
        else:
            self.inventory = self.empty_inventory()
        if self.args.verbose:
            print(json.dumps(self.inventory, indent=4))
        else:
            print(json.dumps(self.inventory))

    # Example inventory for testing.
    def example_inventory(self):
        return {
            'group': {
                'hosts': ['192.168.28.71', '192.168.28.72'],
                'vars': {
                    'ansible_ssh_user': 'vagrant',
                    'ansible_ssh_private_key_file':
                        '~/.vagrant.d/insecure_private_key',
                    'example_variable': 'value'
                }
            },
            '_meta': {
                'hostvars': {
                    '192.168.28.71': {
                        'host_specific_var': 'foo'
                    },
                    '192.168.28.72': {
                        'host_specific_var': 'bar'
                    }
                }
            }
        }

    # Empty inventory for testing.
    def empty_inventory(self):
        return {'_meta': {'hostvars': {}}}

    # Read the command line args passed to the script.
    def read_cli_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--list', action = 'store_true', default=False)
        parser.add_argument('--test', action = 'store_true', default=False)
        #parser.add_argument('-v', action = 'store_true', dest = 'verbose', default=False)
        parser.add_argument('-v', action = 'store', metavar = 'n', dest = 'verbose', nargs = '?', const = "v")
        parser.add_argument('--host', action = 'store')
        parser.add_argument('--version', action='version', version='%(prog)s 0.1', help="show the program version")
        self.args = parser.parse_args()

# Get the inventory.
ExampleInventory()