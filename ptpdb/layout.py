from __future__ import unicode_literals, absolute_import

from prompt_toolkit.layout.controls import TokenListControl
from ptpython.utils import current_python_buffer

from pygments.token import Token


class PdbLeftMargin(TokenListControl):
    """
    Pdb prompt.

    Show "(pdb)" when we have a pdb command or '>>>' when the user types a
    Python command.
    """
    def __init__(self, settings, pdb_commands,
                 ipython=False, prompt_manager=None):
        def get_tokens(cli):
            _, buffer = current_python_buffer(cli, settings)

            if buffer:
                command = buffer.document.text.lstrip()
                if command:
                    command = command.split()[0]

                if any(c.startswith(command) for c in pdb_commands):
                    return [(Token.Prompt, '(pdb) ')]
                elif ipython:
                    text = prompt_manager.render('in', color=False, just=False)
                    return [(Token.Layout.Prompt, text)]
                else:
                    return [(Token.Prompt, '  >>> ')]
            else:
                return []

        super(PdbLeftMargin, self).__init__(get_tokens)
