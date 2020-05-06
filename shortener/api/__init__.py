from .handlers.short import ShortenerView
from .handlers.redirect import RedirectLinkView

HANDLERS = (ShortenerView, RedirectLinkView)
