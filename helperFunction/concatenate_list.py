def concat_list(
    input_strings: [str, ...],
    general_sep: str = ', ',
    last_sep: str = ' a ',
) -> str:
    if not input_strings:
        raise ValueError("List 'input_strings' must not be empty.")
    if len(input_strings) == 1:
        return f"{input_strings[0]}"
    concat_names = general_sep.join(input_strings[:-1]) + \
        f'{last_sep}{input_strings[-1]}'
    return f"{concat_names}"
