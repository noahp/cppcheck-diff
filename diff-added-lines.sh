#!/usr/bin/env bash

# Uses bash regex features, must use bash
# From https://stackoverflow.com/a/12179492

diff-added-lines() {
    local path=
    local line=
    while read -r; do
        esc=$'\033'
        if [[ $REPLY =~ ---\ (a/)?.* ]]; then
            continue
        elif [[ $REPLY =~ \+\+\+\ (b/)?([^[:blank:]$esc]+).* ]]; then
            path=${BASH_REMATCH[2]}
        elif [[ $REPLY =~ @@\ -[0-9]+(,[0-9]+)?\ \+([0-9]+)(,[0-9]+)?\ @@.* ]]; then
            line=${BASH_REMATCH[2]}
        elif [[ $REPLY =~ ^($esc\[[0-9;]+m)*([\ +-]) ]]; then
            if [[ ${BASH_REMATCH[2]} != - ]]; then
                # only echo added lines +
                echo "$path:$line:$REPLY"
                ((line++))
            fi
        fi
    done
}

diff-added-lines
