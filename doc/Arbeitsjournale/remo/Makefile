EPUBPARAMS=--toc -N -s -t epub
PDFPARAMS=--toc -N -s -t latex --pdf-engine=xelatex -V documentclass=scrartcl -V papersize=a4 -V lang=de -V urlcolor=blue -V linkcolor=blue
FONTS=-V mainfont='DejaVu Serif' -V sansfont='DejaVu Sans' -V monofont='DejaVu Sans Mono'
DATE=-V date="`date +'%Y-%m-%d'`"

all: arbeitsjournal_starthack.pdf

arbeitsjournal_starthack.pdf: *.md
	pandoc $(PDFPARAMS) $(FONTS) $(DATE) *.md -o arbeitsjournal_starthack.pdf

clean:
	rm -f arbeitsjournal_starthack.pdf