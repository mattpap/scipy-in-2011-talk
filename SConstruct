import os
env = Environment(ENV=os.environ)

name = 'slides'

pdf_file = name + '.pdf'
tex_file = name + '.tex'
bib_file = name + '.bib'

target = os.path.join('output', pdf_file)

pdf = env.PDF(target=target, source=tex_file)
Depends(pdf, [tex_file, bib_file])

view = env.AlwaysBuild(env.Alias("view", [], "evince %s &" % target))
Depends(view, [target])
