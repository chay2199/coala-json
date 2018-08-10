import textwrap


def unicode_diff_dedent(diff):
    return (
        textwrap.dedent(diff).
        lstrip().
        replace('---\n+++', '--- \n+++ ').
        replace('\n+\n\n', '\n+\n \n').
        replace('\n\n', '\n \n')
    )
