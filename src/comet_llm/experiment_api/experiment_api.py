# -*- coding: utf-8 -*-
# *******************************************************
#   ____                     _               _
#  / ___|___  _ __ ___   ___| |_   _ __ ___ | |
# | |   / _ \| '_ ` _ \ / _ \ __| | '_ ` _ \| |
# | |__| (_) | | | | | |  __/ |_ _| | | | | | |
#  \____\___/|_| |_| |_|\___|\__(_)_| |_| |_|_|
#
#  Sign up for free at https://www.comet.com
#  Copyright (C) 2015-2023 Comet ML INC
#  This file can not be copied and/or distributed without the express
#  permission of Comet ML Inc.
# *******************************************************

from typing import IO, Any, Optional

from . import comet_api_client


class ExperimentAPI:
    def __init__(
        self,
        api_key: str,
        workspace: Optional[str],
        project_name: Optional[str],
    ):
        self._client = comet_api_client.get(api_key)
        self._initialize_experiment(workspace, project_name)

    def _initialize_experiment(
        self, workspace: Optional[str] = None, project_name: Optional[str] = None
    ) -> None:
        response = self._client.create_experiment("LLM", workspace, project_name)
        self._experiment_key = response["experimentKey"]

    def log_asset_with_io(self, name: str, file: IO) -> None:
        self._client.log_experiment_asset_with_io(
            self._experiment_key, name=name, file=file
        )

    def log_parameter(self, name: str, value: Any) -> None:
        self._client.log_experiment_parameter(
            self._experiment_key, name=name, value=value
        )