#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright 2021 Markus Rothe
# SPDX-License-Identifier: EUPL-1.2

import logging

import torch


def cuda_device_info():
    if not torch.cuda.is_available():
        logging.info("CUDA is *NOT* available")
        return

    device_count = torch.cuda.device_count()
    logging.info(
        "CUDA is available"
        f" ({device_count} {'device' if device_count == 1 else 'devices'})."
    )

    for i in range(0, device_count):
        logging.info(f"device({i}): {torch.cuda.get_device_name(i)}")


def main():
    setup_logging("playground.log")
    logging.info("Started")
    cuda_device_info()
    logging.info("Finished")


def setup_logging(filename, log_level=logging.DEBUG):
    # set up logging to file and stdout
    log_formatter = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S%z"
    )
    root_logger = logging.getLogger()

    file_handler = logging.FileHandler(filename)
    file_handler.setFormatter(log_formatter)
    root_logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    root_logger.addHandler(console_handler)

    # needs to be set to DEBUG in order to see INFO and DEBUG messages
    root_logger.setLevel(log_level)


if __name__ == "__main__":
    main()
