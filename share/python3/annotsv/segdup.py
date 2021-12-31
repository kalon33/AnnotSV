from __future__ import annotations

from annotsv.context import Context


def check_segdup_file(app: Context):
    downloaded_file = app.config.segdup_dir / "SegDup.bed"
    formatted_files = list(app.config.segdup_dir.glob("*_SegDup.sorted.bed"))
    label = "SegDup"

    if app.segdup_ann is False:
        app.log.debug(f"No {label} data in output columns, ignoring")
    elif not downloaded_file.exists() and not formatted_files:
        app.log.debug(f"No {label} annotation")
        app.segdup_ann = False
    elif len(formatted_files) > 1:
        app.keep_last_file(label, formatted_files)
    elif not formatted_files:
        raise NotImplementedError()
    else:
        app.log.debug(f"No new {label} annotation to format")


def segdup_annotation(app: Context, breakpoint_chrom: str, breakpoint_pos: int):
    ...