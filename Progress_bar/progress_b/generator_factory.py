from .progbar import progBar
from .progpercent import progPercent

def generator_factory(mother_class):
    def generator_progress(iteritem,iterations=None,*args,**kw):
        if iterations is None:
            iterations=len(iteritem)
        mbar=mother_class(iterations,*args,**kw)
        for item in iteritem:
            yield item
            mbar.update()
    return generator_progress

prog_percent=generator_factory(progPercent)
prog_bar=generator_factory(progBar)