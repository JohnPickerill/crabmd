import guidemd as mistune


def test_box():
    ret = mistune.markdown('{{box!s:\ns\nbox!s}}', escape=True)
    print ret

 

 


