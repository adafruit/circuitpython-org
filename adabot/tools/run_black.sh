# SPDX-FileCopyrightText: 2023 Alec Delaney
#
# SPDX-License-Identifier: MIT

rm -rf .gitlibs
mkdir .gitlibs
cd .libraries
for repo in *; do
    cd ../.gitlibs
    git clone https://github.com/adafruit/$repo.git
    cd $repo
    pre-commit run --all-files
    git add -A
    git commit -m "Run pre-commit"
    git push
    cd ..
done
