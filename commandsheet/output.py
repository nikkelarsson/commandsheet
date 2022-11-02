"""Code for displaying the command sheet -catalog."""

from textwrap import dedent
from textwrap import wrap


def header():
    """
    ████████████████████████████████████████████████████████████████████████████
    █─▄▄▄─█─▄▄─█▄─▀█▀─▄█▄─▀█▀─▄██▀▄─██▄─▀█▄─▄█▄─▄▄▀█─▄▄▄▄█─█─█▄─▄▄─█▄─▄▄─█─▄─▄─█
    █─███▀█─██─██─█▄█─███─█▄█─███─▀─███─█▄▀─███─██─█▄▄▄▄─█─▄─██─▄█▀██─▄█▀███─███
    ▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▀▀▄▄▄▄▄▀▄▀▄▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀
    """
    print(dedent(header.__doc__))


def format_section_heading(heading, index):
    if index is not None:
        return f'{index}. {heading}'
    return heading


# Tries to achieve the following:
#
#    <section command>............... <section's way too long description
#                                      string here, so it is split like
#                                      this, like the argparse does with
#                                      the help messages> :)
#
# Instead of:
#
#    <section command>............... <section's way too long description
#    string here, which is not split like the example above, and looks kinda
#    ugly and not readable, especially when more commands starts to pile up> :(
#
def format_section_content(cmd, desc, indent, fillchar, max_width):
    parts = wrap(desc, width=max_width)
    indented = []

    # Construct the description
    for index, sentence in enumerate(parts):
        if index == 0:
            indented.append(sentence)
        else:
            indented.append(' ' + (' ' * indent) + sentence)
    wrapped = '\n'.join(indented)
    description = wrapped

    result = f'{cmd:{fillchar}<{indent}} {description}'
    return result


def display_commandsheet(
    commandsheet,
    *,
    fillchar,
    section_numbers,
    max_width=40,
    indent=50
):
    index_start=1
    for idx, section in enumerate(commandsheet, start=index_start):
        # Format section heading
        section_heading = format_section_heading(
            section.name, index=idx if section_numbers else None,
        )

        # Print section heading
        print(section_heading)

        # Print section contents
        for cmd, desc in section.contents:
            line = format_section_content(
                cmd,
                desc,
                indent=indent,
                fillchar=fillchar,
                max_width=max_width
            )
            print(line)
        print()
