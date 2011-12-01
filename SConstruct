import os
env = Environment(ENV=os.environ)

pdf = env.PDF(target='output/slides.pdf', source='slides.tex')
Depends(pdf, ['slides.tex', 'slides.bib'])

view = env.AlwaysBuild(env.Alias("view", [], "evince output/slides.pdf &"))
Depends(view, ['output/slides.pdf'])
