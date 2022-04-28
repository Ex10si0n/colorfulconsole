def render(string, fg='', bg=''):
    '''
    Render a string in a given foreground and background color.
    The sample pattern is shown below:

        string = 
        +----------------------------------+
        |                                  |
        |                                  |
        +----------------------------------+

        fg = 
        rgbyrgbyrgbyrgbyrgbyrgbyrgbyrgbyrgby
        g                                  r
        b                                  g
        yrgbyrgbyrgbyrgbyrgbyrgbyrgbyrgbyrgb

        bg = 
        ++++++++++++++++++++++++++++++++++++
        +cccccccccccccccccccccccccccccccccc+
        +cccccccccccccccccccccccccccccccccc+
        ++++++++++++++++++++++++++++++++++++

    Call render(string, fg, bg) to render the string in the foreground color
    '''
    fg_colors = { 'r': 31, 'g': 32, 'y': 33, 'b': 34, 'm': 35, 'c': 36 }
    bg_colors = { '1': 40, 'r': 41, 'g': 42, 'y': 43, 'b': 44, 'm': 45, 'c': 46, '0': 47 }
    lines = string.split('\n')
    fg_lines = fg.split('\n')
    bg_lines = bg.split('\n')
    for i in range(len(lines)):
        line = lines[i]
        fg_line = fg_lines[i]
        bg_line = bg_lines[i]
        for j in range(len(line)):
            char = line[j]
            fg_char = fg_line[j]
            bg_char = bg_line[j]
            if fg_char in fg_colors:
                fg = fg_colors[fg_char]
            else:
                fg = ''
            if bg_char in bg_colors:
                bg = bg_colors[bg_char]
            else:
                bg = ''
            print('\033[{};{}m{}\033[0m'.format(fg, bg, char), end='')
        print()




if __name__ == '__main__':
    string = '''\
+----------------------------------+
|                                  |
|                                  |
+----------------------------------+
    '''

    fg = '''\
rgbyrgbyrgbyrgbyrgbyrgbyrgbyrgbyrgby
g                                  r
b                                  g
yrgbyrgbyrgbyrgbyrgbyrgbyrgbyrgbyrgb
    '''

    bg = '''\
++++++++++++++++++++++++++++++++++++
+cccccccccccccccccccccccccccccccccc+
+cccccccccccccccccccccccccccccccccc+
++++++++++++++++++++++++++++++++++++
    '''

    render(string, fg, bg)
