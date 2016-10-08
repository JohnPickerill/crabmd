import mistune
import re 
import copy
import urlparse
import posixpath  

#TODO disable embedded HTML ? 

 

__version__ = '0.0.0'
__author__ = 'John Pickerill <me@curiouscrab.com>'
__all__ = [
    'BlockGrammar', 'BlockLexer',
    'InlineGrammar', 'InlineLexer',
    'Renderer', 'Markdown',
    'markdown', 'escape',
]
    
class Markdown(mistune.Markdown):
    def __init__(self, renderer=None, inline=None, block=None, **kwargs):
        super(Markdown, self).__init__(renderer=renderer, inline=inline, block=block, **kwargs)          

class InlineGrammar(mistune.InlineGrammar):
    x = "l2"

class InlineLexer(mistune.InlineLexer):      
    default_rules = copy.copy(mistune.InlineLexer.default_rules)
    def __init__(self, renderer, rules=None, **kwargs):
        if rules is None:
            # use the inline grammar
            rules = mistune.InlineGrammar()					
        super(InlineLexer, self).__init__(renderer, rules, **kwargs) 
        
class BlockGrammar(mistune.BlockGrammar):
    x = "2"
        
    
class BlockLexer(mistune.BlockLexer):
    def __init__(self,  rules=None, **kwargs):
        if rules is None:
            # use the inline grammar
            rules = mistune.BlockGrammar()
        super(BlockLexer, self).__init__(rules, **kwargs)    
  
def markdown(text, escape=True, **kwargs):
    """Render markdown formatted text to html.

    :param text: markdown formatted text content.
    :param escape: if set to False, all html tags will not be escaped.
    :param use_xhtml: output with xhtml tags.
    :param hard_wrap: if set to True, it will use the GFM line breaks feature.
    :param parse_block_html: parse text only in block level html.
    :param parse_inline_html: parse text only in inline level html.
    """
    return Markdown(escape=escape, **kwargs)(text) 
        


        
        
