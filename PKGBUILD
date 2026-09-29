# Maintainer: Lievin Christopher <lievin.christopher@gmail.com>
pkgname=wl-4rch
pkgver=0.6
pkgrel=1
pkgdesc="Autoconfig new archlinux installation"
arch=('x86_64')
license=('MIT')
install=wl-4rch.install
source=(https://github.com/lievin-christopher/wl-4rch/archive/refs/heads/main.zip)
sha512sums=('SKIP')
backup=(
        "${HOME:1}/.zshrc"
        "${HOME:1}/.dialogrc"
        "etc/default/lxc-net"
        "etc/lxc/default.conf"
        "etc/dnsmasq.conf"
        "etc/dialogrc"
        "etc/sudoers.d/iftop"
        "usr/local/share/fonts/UBraille.ttf"
        "etc/grub.d/41_bepo"
        "${HOME:1}/.config/4rch-bar/config.example.toml"
        "${HOME:1}/.config/alacritty/alacritty.toml"
        "${HOME:1}/.config/bemenu/powermenu/logout"
        "${HOME:1}/.config/bemenu/powermenu/poweroff"
        "${HOME:1}/.config/bemenu/powermenu/reboot"
        "${HOME:1}/.config/bemenu/powermenu/suspend"
        "${HOME:1}/.config/bemenu/powermenu/unresponding poweroff"
        "${HOME:1}/.config/bemenu/powermenu/unresponding reboot"
        "${HOME:1}/.config/dunst/dunstrc"
        "${HOME:1}/.config/fontconfig/fonts.conf"
        "${HOME:1}/.config/hypr/hyprlock.conf"
        "${HOME:1}/.config/lite-xl/colors/onedark.lua"
        "${HOME:1}/.config/lite-xl/init.lua"
        "${HOME:1}/.config/lite-xl/lpm/settings.json"
        "${HOME:1}/.config/lite-xl/plugins/autosave.lua"
        "${HOME:1}/.config/lite-xl/plugins/bracketmatch.lua"
        "${HOME:1}/.config/lite-xl/plugins/colorpreview.lua"
        "${HOME:1}/.config/lite-xl/plugins/dragdropselected.lua"
        "${HOME:1}/.config/lite-xl/plugins/gitstatus.lua"
        "${HOME:1}/.config/lite-xl/plugins/indent_convert.lua"
        "${HOME:1}/.config/lite-xl/plugins/indentguide.lua"
        "${HOME:1}/.config/lite-xl/plugins/memoryusage.lua"
        "${HOME:1}/.config/lite-xl/plugins/minimap.lua"
        "${HOME:1}/.config/lite-xl/plugins/motiontrail.lua"
        "${HOME:1}/.config/lite-xl/plugins/opacity.lua"
        "${HOME:1}/.config/lite-xl/plugins/rainbowparen.lua"
        "${HOME:1}/.config/lite-xl/plugins/restoretabs.lua"
        "${HOME:1}/.config/lite-xl/plugins/scalestatus.lua"
        "${HOME:1}/.config/lite-xl/plugins/selectionhighlight.lua"
        "${HOME:1}/.config/lite-xl/plugins/sort.lua"
        "${HOME:1}/.config/lite-xl/plugins/titleize.lua"
        "${HOME:1}/.config/lite-xl/plugins/togglesnakecamel.lua"
        "${HOME:1}/.config/lite-xl/plugins/wordcount.lua"
        "${HOME:1}/.config/micro/bindings.json"
        "${HOME:1}/.config/micro/colorschemes/nano.micro"
        "${HOME:1}/.config/micro/settings.json"
        "${HOME:1}/.config/ranger/commands.py"
        "${HOME:1}/.config/ranger/rc.conf"
        "${HOME:1}/.config/ranger/rifle.conf"
        "${HOME:1}/.config/ranger/scope.sh"
        "${HOME:1}/.config/sway/back.jpg"
        "${HOME:1}/.config/sway/config"
        "${HOME:1}/.config/sway/lock_day.png"
        "${HOME:1}/.config/sway/lock_night.png"
        "${HOME:1}/.config/sway/scripts/lock.sh"
        "${HOME:1}/.config/sway/scripts/sway-sensible-terminal"
        "${HOME:1}/.local/bin/crunchbang-mini_color"
        "${HOME:1}/.local/bin/pacman_color"
        "${HOME:1}/.local/bin/panes_color"
        "${HOME:1}/.local/bin/pukeskull_color"
        "${HOME:1}/.local/bin/space-invaders_color"
        "${HOME:1}/.local/share/unrpyc/decompiler/__init__.py"
        "${HOME:1}/.local/share/unrpyc/decompiler/astdump.py"
        "${HOME:1}/.local/share/unrpyc/decompiler/atldecompiler.py"
        "${HOME:1}/.local/share/unrpyc/decompiler/magic.py"
        "${HOME:1}/.local/share/unrpyc/decompiler/renpycompat.py"
        "${HOME:1}/.local/share/unrpyc/decompiler/sl2decompiler.py"
        "${HOME:1}/.local/share/unrpyc/decompiler/testcasedecompiler.py"
        "${HOME:1}/.local/share/unrpyc/decompiler/translate.py"
        "${HOME:1}/.local/share/unrpyc/decompiler/util.py"
        "${HOME:1}/.local/share/unrpyc/deobfuscate.py"
        "${HOME:1}/.local/share/unrpyc/unrpyc.py"
        "${HOME:1}/.ncmpcpp/config"
       )
# Same files are also shipped in /etc/skel for future users
for _f in "${backup[@]}"; do
  [[ $_f == "${HOME:1}/"* ]] && backup+=("etc/skel/${_f#"${HOME:1}/"}")
done
unset _f

# Base
depends=('grub' 'python' 'exfat-utils' 'ntfs-3g')
# Network
depends+=('nmap' 'gnu-netcat' 'openssh' 'dnsmasq' 'wpa_supplicant' 'openssl')
# CLI
depends+=('bash-completion' 'zsh' 'zsh-syntax-highlighting' 'git' 'htop' 'iftop' 'micro'  'ranger' 'rsync' 'screen' 'lm_sensors')
depends+=('oh-my-zsh-git') #AUR
# UI
## Wayland
depends+=('swayimg' 'sway' 'swaybg' 'wlsunset' 'hyprlock' 'brightnessctl' 'bemenu-wayland')
depends+=('wl-clipboard-rs') #AUR
## Universal
depends+=('screenfetch' 'pipewire' 'pipewire-audio' 'pipewire-pulse' 'wireplumber' 'python-requests' 'dialog' 'dunst')
# Fonts
depends+=('ttf-hack-nerd' 'noto-fonts' 'noto-fonts-cjk' 'noto-fonts-emoji')
# Virtualisation
depends+=('qemu' 'lxc' 'arch-install-scripts')
# GUI Apps
depends+=('p7zip' 'ranger'  'rxvt-unicode-terminfo' 'alacritty')
# Multimedia
depends+=('mpv' 'w3m' 'mpd' 'ffmpeg' 'ncmpcpp' 'mpc')
# Android
depends+=('android-file-transfer' 'android-udev' 'android-tools')
# Optional packages
## Base
optdepends=('linux-hardened' 'linux-hardened-headers' 'linux-hardened-docs')
## Network
optdepends+=('openvpn' 'wireguard-tools')
## GUI Apps
optdepends+=('firefox-developer-edition' 'lite-xl')
## CLI
optdepends+=('bat' 'gtop' 'ldm')
## GUI
optdepends+=('filezilla')
### Office
optdepends+=('wps-office')
### Multimedia
optdepends+=('krita' 'vlc')
## Old Urxvt Variant
optdepends+=('rxvt-unicode-patched-with-scrolling' 'urxvt-perls' 'urxvt-resize-font-git')

package() {
  local _src="$srcdir/wl-4rch-main"

  # User config: current user + /etc/skel for future users
  install -d -m755 "$pkgdir$HOME" "$pkgdir/etc/skel"
  local _dest
  for _dest in "$pkgdir$HOME" "$pkgdir/etc/skel"; do
    install -d -m700 "$_dest/.config" "$_dest/.local"
    cp -a "$_src/.config/." "$_dest/.config/"
    cp -a "$_src/.local/." "$_dest/.local/"
    chmod 700 "$_dest/.local" "$_dest/.local/share"
    cp -a "$_src/.ncmpcpp" "$_dest/"
    install -m644 "$_src/.zshrc" -t "$_dest/"
    install -d "$_dest/Music"
    dialog --create-rc "$_dest/.dialogrc"
  done
  chown -R "$(id -u):$(id -g)" "$pkgdir$HOME"

  # mpd (final /etc/mpd.conf is deployed by the .install hook)
  install -d "$pkgdir/opt/mpd/playlists" "$pkgdir/opt/mpd/lyrics"
  touch "$pkgdir/opt/mpd/mpd.log" "$pkgdir/opt/mpd/mpd.db"
  install -d "$pkgdir/usr/share/wl-4rch"
  {
    echo "music_directory \"$HOME/Music\""
    cat "$_src/mpd.conf"
  } > "$pkgdir/usr/share/wl-4rch/mpd.conf"

  # System config
  install -Dm755 "$_src/4rch-bar" -t "$pkgdir/usr/bin/"
  install -Dm644 "$_src/dnsmasq.conf" -t "$pkgdir/etc/"
  install -Dm644 "$_src/default.conf" -t "$pkgdir/etc/lxc/"
  install -Dm644 "$_src/lxc-net" -t "$pkgdir/etc/default/"
  install -d -m750 "$pkgdir/etc/sudoers.d"
  install -Dm440 "$_src/iftop" "$pkgdir/etc/sudoers.d/iftop"
  dialog --create-rc "$pkgdir/etc/dialogrc"
  install -Dm644 "$_src/UBraille.ttf" -t "$pkgdir/usr/local/share/fonts/"

  # grub (bepo keymap + default config applied by the .install hook)
  install -Dm644 "$_src/bepo.gkb" "$pkgdir/boot/grub/bepo.gkb"
  install -Dm644 "$_src/grub" "$pkgdir/usr/share/wl-4rch/grub.default"
  install -Dm755 "$_src/41_bepo" "$pkgdir/etc/grub.d/41_bepo"
}
