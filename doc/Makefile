EPUBPARAMS=--toc -N -s -t epub
PDFPARAMS=--toc -N -s -t latex --pdf-engine=xelatex -V documentclass=scrartcl -V papersize=a4 -V lang=en -V urlcolor=blue -V linkcolor=blue
FONTS=-V mainfont='DejaVu Serif' -V sansfont='DejaVu Sans' -V monofont='DejaVu Sans Mono'
DATE=-V date="`date +'%Y-%m-%d'`"

all: starthack.pdf starthack.epub

starthack.pdf: *.md
	pandoc $(PDFPARAMS) $(FONTS) $(DATE) *.md -o starthack.pdf

starthack.epub: *.md
	pandoc $(EPUBPARAMS) $(DATE) *.md -o starthack.epub

clean:
	rm -f starthack.pdf
	rm -f starthack.epub