PDFPARAMS=--toc -N -s -t latex --pdf-engine=xelatex -V documentclass=scrreprt -V papersize=a4 -V lang=de -V urlcolor=blue -V linkcolor=blue -V geometry:margin=2.54cm
FONTS=-V mainfont='DejaVu Serif' -V sansfont='DejaVu Sans' -V monofont='DejaVu Sans Mono'
DATE=-V date="`date +'%Y-%m-%d'`"

all: clean pdf

pdf: *.md
	pandoc $(PDFPARAMS) $(FONTS) $(DATE) *.md -o starthack_team_asimov_doc.pdf

clean:
	rm -f starthack_team_asimov_doc.pdf