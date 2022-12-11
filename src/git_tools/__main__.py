import os

import click


@click.group()
def cli():
    pass


def check_stage(on_success, on_failed):
    """check git stage"""
    res = os.system("git diff --cached --exit-code")
    if res == 0:
        on_success()
    else:
        on_failed()


def safe_cmd(name, msg):
    os.system(f"""git commit -m "{name} {msg}" """)


def unsafe_cmd(name, msg):
    os.system("git add .")
    safe_cmd(name, msg)


@click.command(help="feat -> quick feat command")
@click.argument("--command", type=str)
@click.argument("--msg", type=str)
def run(command, msg):
    from functools import partial

    check_stage(
        on_success=partial(unsafe_cmd, command, msg),
        on_failed=partial(safe_cmd, command, msg),
    )
