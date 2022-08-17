FROM fedora:latest
RUN dnf -y install git neovim python3 python3-neovim sudo && dnf clean all \
    && useradd -m -G users -s /bin/bash vscode \
    && echo vscode ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/vscode
