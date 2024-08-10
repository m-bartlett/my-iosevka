#!/usr/bin/env bash
# sudo rm -v /usr/share/fonts/iosevka/*.ttf && sudo mv -v ~/Desktop/Iosevka/dist/Iosevka/TTF/* /usr/share/fonts/iosevka/ && font-cache
# yay -Sy --needed ttfautohint npm

set -o errexit

PLANS=(
   Iosevka
   IosevkaCondensed
   IosevkaExpanded
)

[ -d iosevka ] || git clone --depth 1 https://github.com/be5invis/Iosevka.git 'iosevka'
cd ./iosevka
npm i
cp ../private-build-plans.toml .

build_plans="${@:-${PLANS[@]}}"
echo "Building: $build_plans"

for plan in $build_plans; do
    npm run build -- ttf::$plan
done