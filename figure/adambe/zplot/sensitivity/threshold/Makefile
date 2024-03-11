all:
	#!/bin/bash; \
	for file in $$(ls *.py | grep -v "zplot.py"); do \
		python "$$file" eps; \
	done; \
	for file in *.eps; do \
		ps2pdf "$$file"; \
	done; \
	for file in *.pdf; do \
		pdfcrop "$$file" "$$file"; \
	done
	rm -rf *.eps
fig:
	mv -f *.pdf ../../../
clean: 
	rm -rf *.eps *.pdf