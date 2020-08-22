#!/usr/bin/env python

from k3.utils import *

Arguments = get_Arguments({'src':None})

if Arguments['src'] is not None:
	restore_Desktop(Arguments['src'])
