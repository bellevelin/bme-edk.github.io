#!/usr/bin/env python3

import csv

with open('lectures.csv') as lecturesfile:
	lectures = csv.DictReader(lecturesfile)
	for lecture in lectures:
		filecontent = "\n".join((
			"---",
			"layout: post",
			"categories: lecture",
			"date: %s" % lecture['date'],
			"title: %s" % lecture['title'],
			"lecturers: %s" % lecture['lecturer'],
			"phdla: %s" % lecture['phdla'],
			"duration: %s" % lecture['duration'],
			"school: %s" % lecture['school'],
			"---",
			"",
			"Bemutató szöveg..."
		))

		filename = "%s.md" % lecture['filename']

		print(filename)
		with open(filename, "w") as output:
			print(filecontent, file=output)
