FROM python:3
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y sudo \
    && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/* \
    && useradd -m -G users -s /bin/bash vscode \
    && echo vscode ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/vscode \
    && pip install virtualenv
