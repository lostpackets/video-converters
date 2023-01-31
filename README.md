# video-converters
This includes scripts that allow: convert all videos to .hevc, combine all videos (This repo will be more refined soon)

Some of the following pip packages are required:

pip install moviepy

pip install setuptools

# If HEVC is unplayable

If .HEVC is unplayable, try the cmds below for the respective distro being used (cmds will dl libx265)

# Ubuntu/Debian:

sudo apt-get update

sudo apt-get install libx265-dev


# Fedora:

sudo dnf install x265


# Arch:

sudo pacman -S x265
