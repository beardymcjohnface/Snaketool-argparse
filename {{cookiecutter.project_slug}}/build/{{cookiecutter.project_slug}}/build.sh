#!/bin/sh
set -e

mkdir -p "${PREFIX}/bin"
mkdir -p "${PREFIX}/{{cookiecutter.project_slug}}.workflow"

cp -r bin/* "${PREFIX}/bin/"
cp -r {{cookiecutter.project_slug}}.workflow/* "${PREFIX}/{{cookiecutter.project_slug}}.workflow/"
cp {{cookiecutter.project_slug}}.LICENSE {{cookiecutter.project_slug}}.VERSION "${PREFIX}/"

{{cookiecutter.project_slug}} -h
