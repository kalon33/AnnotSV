from __future__ import annotations

from annotsv.context import Context


def check_gap_file(app: Context):
    downloaded_file = app.config.gap_dir / "Gap.bed"
    formatted_files = list(app.config.gap_dir.glob("*_Gap.sorted.bed"))
    label = "gap"

    if app.gap_ann is False:
        app.log.debug(f"No {label} data in output columns, ignoring")
    elif not downloaded_file.exists() and not formatted_files:
        app.log.debug(f"No {label} annotation")
        app.gap_ann = False
    elif len(formatted_files) > 1:
        app.keep_last_file(label, formatted_files)
    elif not formatted_files:
        raise NotImplementedError()
    else:
        app.log.debug(f"No new {label} annotation to format")


def gap_annotation(app: Context, breakpoint_chrom: str, breakpoint_pos: int):
    ...