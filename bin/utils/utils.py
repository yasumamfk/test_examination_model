#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json


def read_config():
    with open('config.json') as f:
        return json.loads(f.read())
