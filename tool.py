#!/usr/bin/env python3

# MIT License
#
# Copyright (c) 2022 Kenta Kabashima
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

"""Tool to create and test Docker image."""

import datetime
import os
import subprocess

import click

THIS_DIR = os.path.dirname(os.path.realpath(__file__))

GITLAB_IMAGE_URL = "registry.gitlab.com/musicscience37projects/docker/pipenv-docker"
DOCKER_HUB_IMAGE_URL = "musicscience37/pipenv"

IMAGE_TAGS = [
    "jammy",  # 22.04 LTS
    "noble",  # 24.04
    "questing",  # 25.10
    "resolute",  # 26.04 LTS
    "alpine",  # Alpine Linux
]
IMAGE_DIR_DICT = {
    "jammy": "since_jammy",
    "noble": "since_jammy",
    "questing": "since_jammy",
    "resolute": "since_jammy",
    "alpine": "alpine",
}
LATEST_IMAGE_TAG = "noble"


@click.group()
def cli():
    pass


def _run_command(command: list[str]):
    """Run a command.

    Args:
        command (list[str]): Command.
    """

    click.secho(f"> {command}", bold=True)
    subprocess.run(command, check=True, cwd=THIS_DIR)


def _create_time_stamp() -> str:
    """Create a time stamp.

    Returns:
        str: Time stamp.
    """

    return datetime.datetime.now().strftime("%Y%m%d")


def _build(image_tag: str, image_full_name: str):
    """Build Docker image.

    Args:
        image_tag (str): Tag of the image.
        image_full_name (str): Full name of the image.
    """

    _run_command(
        [
            "docker",
            "build",
            "-t",
            image_full_name,
            "--build-arg",
            f"IMAGE_TAG={image_tag}",
            IMAGE_DIR_DICT[image_tag],
        ]
    )


def _test(image_full_name: str):
    """Test Docker image.

    Args:
        image_full_name (str): Full name of the image.
    """

    _run_command(
        [
            "docker",
            "run",
            "--rm",
            "-v",
            f"{THIS_DIR}/test:/home/test",
            image_full_name,
            "/home/test/run_test.sh",
        ]
    )


def _tag_and_upload(image_full_name: str, another_image_full_name: str):
    _run_command(["docker", "tag", image_full_name, another_image_full_name])
    _run_command(["docker", "push", another_image_full_name])


def _upload(image_tag: str, image_full_name: str):
    """Upload Docker image.

    Args:
        image_tag (str): Tag of the image.
        image_full_name (str): Full name of the image.
    """

    _run_command(
        [
            "docker",
            "login",
            "-u",
            os.environ["CI_REGISTRY_USER"],
            "-p",
            os.environ["CI_REGISTRY_PASSWORD"],
            os.environ["CI_REGISTRY"],
        ]
    )
    _run_command(["docker", "push", image_full_name])
    _tag_and_upload(
        image_full_name=image_full_name,
        another_image_full_name=f"{GITLAB_IMAGE_URL}:{image_tag}-{_create_time_stamp()}",
    )
    if image_tag == LATEST_IMAGE_TAG:
        _tag_and_upload(
            image_full_name=image_full_name,
            another_image_full_name=f"{GITLAB_IMAGE_URL}:latest",
        )

    _run_command(
        [
            "docker",
            "login",
            "-u",
            os.environ["HUB_USER_NAME"],
            "-p",
            os.environ["HUB_ACCESS_TOKEN"],
        ]
    )
    _tag_and_upload(
        image_full_name=image_full_name,
        another_image_full_name=f"{DOCKER_HUB_IMAGE_URL}:{image_tag}",
    )
    if image_tag == LATEST_IMAGE_TAG:
        _tag_and_upload(
            image_full_name=image_full_name,
            another_image_full_name=f"{DOCKER_HUB_IMAGE_URL}:latest",
        )


@cli.command()
@click.argument("image_tag", type=click.Choice(IMAGE_TAGS))
def test(image_tag: str):
    """Build and test Docker image."""

    image_full_name = f"{GITLAB_IMAGE_URL}:{image_tag}-test"
    _build(image_tag=image_tag, image_full_name=image_full_name)
    _test(image_full_name=image_full_name)


@cli.command()
@click.argument("image_tag", type=click.Choice(IMAGE_TAGS))
def update(image_tag: str):
    """Build, test, and update Docker image."""

    image_full_name = f"{GITLAB_IMAGE_URL}:{image_tag}"
    _build(image_tag=image_tag, image_full_name=image_full_name)
    _test(image_full_name=image_full_name)
    _upload(image_tag=image_tag, image_full_name=image_full_name)


if __name__ == "__main__":
    cli()
