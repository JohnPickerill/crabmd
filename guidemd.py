import mistune
import re 
import inspect
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

def output_box(self):
    return self.renderer.box(self.token['option'],self.token['text']);  

    
class Markdown(mistune.Markdown):
    def __init__(self, renderer=None, inline=None, block=None, **kwargs):
        Markdown.output_box = output_box
        if not renderer:
            renderer = Renderer(**kwargs)

        if inline and inspect.isclass(inline):
            inline = inline(renderer, **kwargs)
            
        if block and inspect.isclass(block):
            block = block(**kwargs)       
        
        #Markdown.output_drop = output_drop
        #Markdown.output_blk = output_blk
        #Markdown.output_item = output_item
        Markdown.output_box = output_box           
 
        super(Markdown, self).__init__(renderer=renderer, inline=inline, block=block, **kwargs)         

#class Markdown(mistune.Markdown):
    #def __init__(self, hn="_drop", renderer=None, inline=None, block=None, **kwargs):
 #       self.hn = hn
        #if not renderer:
        #    renderer = Renderer(**kwargs)

        #if inline and inspect.isclass(inline):
        #    inline = inline(renderer, **kwargs)
            
        #if block and inspect.isclass(block):
        #    block = block(**kwargs)

        #Markdown.output_drop = output_drop
        #Markdown.output_blk = output_blk
        #Markdown.output_item = output_item
        #Markdown.output_box = output_box
#        super(Markdown, self).__init__(renderer=renderer, inline=inline, block=block, **kwargs)   

        

class Renderer(mistune.Renderer):
    hn = "hd"
    hi = 0
    
    def __init__(self, hn="hdx" , **kwargs):
        self.hn = hn
        super(Renderer,self).__init__(**kwargs)
         
    def box (self,option,text): 
        return '<pre><jpc>' + text + '<jpc></pre>'      

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
    box  = re.compile(r'(?:^|\n){{(box(?:![a-z]+)?):[ \t]*([a-zA-Z0-9 \t]*)\n([\s\S]*?)\n(?:\1)}}[^\n]*(?:\n|$)')
        
    
class BlockLexer(mistune.BlockLexer):
    default_rules = copy.copy(mistune.BlockLexer.default_rules)
    default_rules.insert(1,'box')

    def __init__(self,  rules=None, **kwargs):
        if rules is None:
            # use the inline grammar
            rules = BlockGrammar()
        super(BlockLexer, self).__init__(rules, **kwargs) 

    def parse_box(self, m):  
        assert false
        src = m.group(0)
        option =  m.group(2) 
        textstr = m.group(3) 
        self.tokens.append({
            'type': 'box',
            'option': option,
            'text': textstr
        })          
  
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
        


        
        
