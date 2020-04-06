# coding=utf-8
from pybadges import badge


badge_logo = 'https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg'

s = badge(left_text='', right_text='Python', right_color='orange', logo=badge_logo, embed_logo=True,
          left_link='https://www.python.org/', right_link='https://github.com/djsnipa1/python-shit',
          left_title='Python', right_title='is the shit!')

# TODO: Fix this script so it works again. It's making svg's without a background color

badge2 = badge(left_text='made with', right_text='pybadges', right_title='pybadges',
               right_color='orange', right_link='https://github.com/google/pybadges')

# s is a string that contains the badge data as an svg image.
print(s[:40]) # => <svg height="20" width="191.0" xmlns="ht
print("-=" * 20)
print("badge2")
print(badge2)

with open('tmp/assets/badge1.svg', 'w', encoding='utf-8') as outfile:
    outfile.write(s)

with open('tmp/assets/badge2.svg', 'w', encoding='utf-8') as outfile:
    outfile.write(badge2)

'''   
python -m pybadges \
    --left-text="" \
    --right-text="Python" \
    --right-color=orange \
    --left-link=https://www.python.org// \
    --right-link="https://github.com/djsnipa1/" \
    --logo='https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg' \
    --embed-logo \
    --whole-title="Python-Shit" \
    --left-title="Python Logo" \
    --right-title="ss the shit!" \
    --browser

'''