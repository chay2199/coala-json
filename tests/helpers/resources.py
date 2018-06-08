from pathlib import Path

base_relative_url = Path.cwd().joinpath(
    'tests', 'resources', 'diagnostic')


def url(val, as_obj=False):
    names = val.split('|')
    path = base_relative_url.joinpath(*names)

    return path if as_obj else str(path)


sample_diagnostics = url('diagnostics.json')
