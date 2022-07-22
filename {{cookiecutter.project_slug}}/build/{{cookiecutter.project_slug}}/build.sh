#!/bin/sh
set -e

mkdir -p "${PREFIX}/bin"
mkdir -p "${PREFIX}/config"
mkdir -p "${PREFIX}/workflow"
mkdir -p "${PREFIX}/test"

cp -r bin/* "${PREFIX}/bin/"
cp -r config/* "${PREFIX}/config/"
cp -r workflow/* "${PREFIX}/workflow/"
cp -r test/* "${PREFIX}/test/"
cp LICENSE README.md VERSION "${PREFIX}/"

{{cookiecutter.project_slug}} -h
