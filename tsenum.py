#!/usr/bin/python
# -*- coding: UTF-8 -*-
# vim: noet tabstop=4 shiftwidth=4
#
# Timestamp enumerator 
# Copyright (C) 2016 Alexander Böhm <alxndr.boehm@gmail.com>
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


import sys, argparse
from datetime import datetime, timedelta

def enumerate_times(cur_time, offset, count, step, patern):
	cur = cur_time
	r = []

	l_count = (count < 0)*count
	h_count = (count >= 0)*count

	if step == None or type(step) != str:
		return []

	elif step.lower() == "day":
		for i in range(l_count, h_count):
			t = cur+timedelta(days=(i+offset))
			r += [t.strftime(patern)]

	elif step.lower() == "week":
		for i in range(l_count, h_count):
			t = cur+timedelta(weeks=(i+offset))
			r += [t.strftime(patern)]

	elif step.lower() == "hour":
		for i in range(l_count, h_count):
			t = cur+timedelta(hours=(i+offset))
			r += [t.strftime(patern)]

	elif step.lower() == "minute":
		for i in range(l_count, h_count):
			t = cur+timedelta(minutes=(i+offset))
			r += [t.strftime(patern)]
	else:
		return []

	return r

if __name__ == "__main__":
	parser = argparse.ArgumentParser(
		description="Enumerate timestamps from now with offset in different units.",
	)

	parser.add_argument(
		'--utc', '-u',
		help="Current time is in UTC",
		dest="utc",
		action="store_true",
		default=False,
	)

	parser.add_argument(
		'--offset', '-o',
		help="Offset to enumerate from",
		dest="offset",
		type=int,
		required=True,
	)

	parser.add_argument(
		'--count', '-c',
		help="Count to enumerate",
		dest="count",
		type=int,
		required=True,
	)

	parser.add_argument(
		'--step', '-s',
		help="Step width",
		dest="step",
		choices=["day", "week", "hour", "minute"],
		type=str,
		required=True,
	)

	parser.add_argument(
		'--pattern', '-p',
		help="Date pattern to use (see Python's strftime in datetime)",
		dest="pattern",
		type=str,
		required=True,
	)

	args = parser.parse_args()

	if args.utc:
		now = datetime.utcnow()
	else:
		now = datetime.now()

	for i in enumerate_times(now, args.offset, args.count, args.step, args.pattern):
		print i
	
	sys.exit(0)
