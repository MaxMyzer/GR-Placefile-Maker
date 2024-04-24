#!/usr/bin/python
import sys
import argparse
import pandas as pd

parser = argparse.ArgumentParser(
    prog='GR2 Analyst 3 PlaceFile Generator',
    description='Generate a PlaceFile of points for GR2 Analyst 3 from a CSV file.',
    )
parser.add_argument('-f', '--file', help='CSV file to read', required=True)
parser.add_argument('-o', '--output', help='PlaceFile to write', required=True)
parser.add_argument('-lat', '--latitude', help='Latitude column name', required=True)
parser.add_argument('-lon', '--longitude', help='Longitude column name', required=True)
parser.add_argument('-i', '--icon', help='Icon URL', required=True)
parser.add_argument('-n', '--name', help='Name column name', required=False)
parser.add_argument('-ln', '--labelname', help='label for name', required=False, default='Name')
parser.add_argument('-ld', '--labeldesc', help='label for description', required=False, default='Description')
parser.add_argument('-t', '--title', help='Title of the placefile', required=False)
parser.add_argument('-d', '--description', help='Description column name', required=False)
parser.add_argument('-iw', '--iconwidth', help='Icon width', required=False, default=32)
parser.add_argument('-ih', '--iconheight', help='Icon height', required=False, default=32)
parser.add_argument('-ix', '--iconx', help='Icon x offset', required=False, default=16)
parser.add_argument('-iy', '--icony', help='Icon y offset', required=False, default=16)
parser.add_argument('-ia', '--iconangle', help='icon angle column', default=None)


args = parser.parse_args()

df = pd.read_csv(args.file)
with open(args.output, 'w') as f:
    filenum=1
    f.write('Title: {}\n'.format(args.title))
    f.write('Refresh: 60\n') # probably dont need to refresh
    f.write(f'IconFile: {filenum}, {args.iconwidth}, {args.iconheight}, {args.iconx}, {args.icony}, {args.icon}') # may need to parameterize the sizes
    hovers = [0,0]
    if(args.name):
        hovers[0] = 1
    if(args.description):
        hovers[1] = 1
    for index, row in df.iterrows(): # for each row
        hoverText = ""
        if(hovers[0] == 1 and hovers[1] == 1):
            hoverText += f', {args.labelname}: {row[args.name]}\\n{args.labeldesc}: {row[args.description]}\n'
        elif(hovers[0] == 1):
            hoverText += f', {row[args.name]}\n'
        elif(hovers[1] == 1):
            hoverText += f', {row[args.description]}\n'
        ia = row[args.iconangle] if args.iconangle else 0
        f.write(f'Icon: {row[args.latitude]},{row[args.longitude]},{ia},{filenum}{hoverText}\n')