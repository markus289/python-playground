FROM fedora:latest
RUN dnf update -y \
    && dnf install sudo neovim python3-neovim \
    && dnf clean all \
    && useradd -m -G users -s /bin/bash vscode \
    && echo vscode ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/vscode
