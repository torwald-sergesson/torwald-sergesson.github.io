#!/usr/bin/env python

'''
tag_generator.py
Copyright 2017 Long Qian
Contact: lqian8@jhu.edu
This script creates tags for your Jekyll blog hosted by Github page.
No plugins required.
'''

import glob
import os
from collections import Counter 

post_dir = '_posts/'
tag_dir = 'tag/'
tags_file = 'tags.md'

filenames = glob.glob(post_dir + '**/*.md', recursive=True)

total_tags = list() 
for filename in filenames:
    print('Processing %s', filename)
    with open(filename, 'r', encoding='utf8') as f:
        crawl = False
        for line in f:
            if crawl:
                if not line.startswith('tags:'):
                    continue
                current_tags = set(line.replace('tags:', '').strip().split())
                total_tags.extend(current_tags) 
                break
            if line.strip() == '---':
                if not crawl:
                    crawl = True
                else:
                    crawl = False
                    break
stat = Counter(total_tags)
print('Found tags:\n');
for tag, count in stat.most_common():
    print(f'- {tag}: {count}')
old_tags = glob.glob(tag_dir + '*.md')
for tag in old_tags:
    os.remove(tag)
    
if not os.path.exists(tag_dir):
    os.makedirs(tag_dir)

for tag, count in stat.most_common():
    tag_filename = tag_dir + tag + '.md'
    with open(tag_filename, 'w') as f:
        write_str = f'---\nlayout: tagpage\ntitle: "Tag: {tag}"\ntag: {tag}\ntcount: {count}\nrobots: noindex\n---\n'
        f.write(write_str)
print(f"Tags generated, count {len(total_tags)}\n")

