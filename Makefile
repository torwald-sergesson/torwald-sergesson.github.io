.PHONY: tags
tags:
	python3 tools/tag_generator.py

.PHONY: serve
serve:
	bundle exec jekyll serve -l
