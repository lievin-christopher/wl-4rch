# Maintainer: Lievin Christopher <lievin.christopher@gmail.com>
pkgname=wl-4rch
pkgver=0.6
pkgrel=1
pkgdesc="Autoconfig new archlinux installation"
arch=('x86_64')
license=('MIT')
source=(https://github.com/lievin-christopher/wl-4rch/archive/refs/heads/main.zip)
sha512sums=('SKIP')
backup=(
        "${HOME:1}/.zshrc"
        "${HOME:1}/.dialogrc"
        "${HOME:1}/.taskrc"
        "etc/default/lxc-net"
        "etc/lxc/default.conf"
        "etc/dnsmasq.conf"
        "etc/dialogrc"
        "etc/sudoers.d/iftop"
        "usr/local/share/fonts/UBraille.ttf"
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
  ls $srcdir/wl-4rch-main
  mkdir -p $pkgdir$HOME/
  mkdir -p $pkgdir/etc/{lxc,default}
  chmod 700 $pkgdir$HOME/
  # Install config files and directories
  rsync -av $srcdir/wl-4rch-main/.config $pkgdir$HOME/
  chmod 700 $pkgdir$HOME/.config
  rsync -av $srcdir/wl-4rch-main/.local $pkgdir$HOME/
  chmod 700 $pkgdir$HOME/.local
  ## mpd + ncmpcpp
  mkdir -p $pkgdir/opt/mpd/playlists
  touch $pkgdir/opt/mpd/mpd.log $pkgdir/opt/mpd/mpd.db
  mkdir -p $pkgdir/opt/mpd/lyrics
  mkdir -p $pkgdir$HOME/Music
  rsync -av $srcdir/wl-4rch-main/.ncmpcpp $pkgdir$HOME/
  install -m644 "$srcdir/wl-4rch-main/.zshrc" -t "$pkgdir$HOME/"
  ## Daily script
  mkdir -p "$pkgdir/usr/bin"
  install -m755 "$srcdir/wl-4rch-main/4rch-bar" -t "$pkgdir/usr/bin/"
  chown -R $USER:users $pkgdir$HOME
  install -m644 "$srcdir/wl-4rch-main/dnsmasq.conf" -t "$pkgdir/etc/"
  install -m644 "$srcdir/wl-4rch-main/default.conf" -t "$pkgdir/etc/lxc/"
  install -m644 "$srcdir/wl-4rch-main/lxc-net" -t "$pkgdir/etc/default/"
  install -Dm440 "$srcdir/wl-4rch-main/iftop" "$pkgdir/etc/sudoers.d/iftop"
  dialog --create-rc $pkgdir$HOME/.dialogrc
  dialog --create-rc $pkgdir/etc/dialogrc
  mkdir -p "$pkgdir/usr/local/share/fonts/"
  install -m644 "$srcdir/wl-4rch-main/UBraille.ttf" -t "$pkgdir/usr/local/share/fonts/"
}

post_install() {
	echo -en "music_directory " > $pkgdir/etc/mpd.conf
	echo "\"$HOME/Music\"" >>  $pkgdir/etc/mpd.conf
	cat $srcdir/wl-4rch-main/mpd.conf >>  $pkgdir/etc/mpd.conf
    sed --in-place=.pacsave 's/arch.pool.ntp.org/fr.pool.ntp.org iburst/' $pkgdir/etc/ntp.conf 
	chown mpd /etc/mpd.conf
	chown -R mpd /opt/mpd
	install -m644 "$srcdir/wl-4rch-main/bepo.gkb" "/boot/grub/bepo.gkb"
	install -m644 "$srcdir/wl-4rch-main/grub" "/etc/default/grub"
	echo "insmod keylayouts" >> /etc/grub.d/40_custom
	echo "keymap /boot/grub/bepo.gkb" >> /etc/grub.d/40_custom
	grub-mkconfig -o /boot/grub/grub.cfg
	systemctl enable mpd.service
	systemctl enable mpd.socket
	systemctl enable lxc-net.service
	systemctl enable ntpd.service
}
