import crabmd as mistune

def test_box():
    str = \
'''
{{box!s:
s
box!s}}
'''  
    html = \
'''<pre><jpc>s</jpc></pre>'''    
    ret = mistune.markdown(str, escape=True)
    if ret != html:
        raise ValueError("\ngot:\n{0} \nexpected:\n{1}".format(ret,html))



def test_table():
    str = \
'''
john | was | here
---- | --- | ----
A    | b   | c 
'''  
    html = \
'''<table class="table table-striped table-bordered">
<thead><tr>
<th>john</th>
<th>was</th>
<th>here</th>
</tr>
</thead>
<tbody>
<tr>
<td>A</td>
<td>b</td>
<td>c </td>
</tr>
</tbody>
</table>
'''    
    ret = mistune.markdown(str, escape=True)
    if ret != html:
        raise ValueError("\ngot:\n{0} \nexpected:\n{1}".format(ret,html))

def test_blk():
    styles = {
          "legal_italic":{
          "span":"i",
          "block":"legal_italic",
          "class":"g_legal_italic",
          "purpose":"Italics required to match prescribed formatting in legislation, documents or forms"},  

          "legal_bold":{
          "span":"b",
          "block":"legal_bold",
          "class":"g_legal_bold",
          "purpose":"Bold required to match prescribed formatting in legislation, documents or forms"}
        }
        

    str = \
'''
{{blk!l:    
default
blk!l}}
{{blk!legal_italic:    
John
blk!legal_italic}}
'''  
    html = \
'''<div class="g_default"><p>default</p>
</div><div class="g_legal_italic"><p>John</p>
</div>'''    
    ret = mistune.markdown(str, styles = styles,  escape=True)
    if ret != html:
        raise ValueError("\ngot:\n{0} \nexpected:\n{1}".format(ret,html))
        
        
        
        
       
test_box() 
test_table()
test_blk() 
