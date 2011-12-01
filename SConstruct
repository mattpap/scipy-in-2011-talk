import os
env = Environment(ENV=os.environ)
pdf = env.PDF(target='output/slides.pdf', source='slides.tex')
Depends(pdf, Split('slides.tex slides.bib'))
