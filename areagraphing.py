NAME = 'areagraphing'
HEIGHT = 100
WIDTH = HEIGHT / 10

glyphs = []
start = 0xE000
for i in range(HEIGHT+1):
    char = start + i
    glyphs.append(f'<glyph unicode="&#x{char:x};" horiz-adv-x="{WIDTH/2}" d="M0,-{HEIGHT/2} H{WIDTH} v{i} H0 z" />')
glyphs = '\n'.join(glyphs)

print(f'''
<svg xmlns="http://www.w3.org/2000/svg">
<font id="{NAME}" horiz-adv-x="{HEIGHT/2}" vert-origin-x="0" vert-origin-y="{HEIGHT/2}">
  <font-face font-family="{NAME}" font-style="normal" units-per-em="{HEIGHT}" cap-height="{HEIGHT}" x-height="{HEIGHT}" >
    <font-face-src>
      <font-face-name name="{NAME}"/>
    </font-face-src>
  </font-face>
{glyphs}
</font>
</svg>
''')
