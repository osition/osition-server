# -*- coding=utf-8 -*-
r"""

"""
import typing as t
from functools import cache
import configlib
from ._logging import configure_logging
from ._process_config import configure_process


@cache
def get_config() -> t.Tuple['configlib.ConfigInterface', str]:
    try:
        fp = configlib.find(
            ".jarklin.ext",
            ".jarklin/config.ext",
            places=[
                configlib.places.cwd(),
            ]
        )
    except configlib.ConfigNotFoundError:
        raise FileNotFoundError("no jarklin config file found in current directory") from None
    else:
        config = configlib.load(fp=fp)
        config.merge(configlib.from_environ(prefix="JARKLIN"))
        configlib.config.update(config)
        configure_logging(config=config)
        configure_process(config=config)
        return config, str(fp.absolute())
