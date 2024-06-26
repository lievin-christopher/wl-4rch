# Maintainer: Lievin Christopher <lievin.christopher@gmail.com>
pkgname=wl-4rch
pkgver=0.2
pkgrel=0
pkgdesc="Autoconfig new archlinux installation"
arch=('x86_64')
license=('MIT')
source=(https://github.com/lievin-christopher/wl-4rch/archive/master.zip)
sha512sums=('SKIP')
NoUpgrade=$HOME/.zshrc
backup=(
        "${HOME:1}/.config"
        "${HOME:1}/.ncmpcpp/config"
        "${HOME:1}/.dialogrc"
        "${HOME:1}/.taskrc"
        "etc/default/lxc-net"
        "etc/lxc/default.conf"
        "etc/dnsmasq.conf"
        "etc/dialogrc"
       )

# Base
depends=('linux-hardened' 'linux-hardened-headers' 'linux-hardened-docs' 'grub' 'python' 'exfat-utils' 'ntfs-3g')
# Network
depends+=('nmap' 'gnu-netcat' 'openssh' 'dnsmasq' 'wpa_supplicant' 'openssl' 'ntp')
# CLI
depends+=('bash-completion' 'zsh' 'zsh-syntax-highlighting' 'task' 'git' 'htop' 'iftop' 'micro'  'ranger' 'rsync' 'screen' 'lm_sensors')
depends+=('oh-my-zsh-git') #AUR
# UI
## Wayland
depends+=('yambar-wayland' 'swayimg' 'sway' 'swaybg' 'wlsunset' 'hyprlock' 'brightnessctl' 'bemenu-wayland')
depends+=('grimshot' 'yambar-wayland' 'wl-clipboard-rs') #AUR
## Universal
depends+=('screenfetch' 'pipewire' 'pipewire-audio' 'pipewire-pulse' 'wireplumber' 'python-requests' 'dialog' 'dunst')
# Fonts
depends+=('ttf-hack-nerd' 'noto-fonts' 'noto-fonts-cjk' 'noto-fonts-emoji')
# Virtualisation
depends+=('qemu' 'lxc' 'arch-install-scripts')
# GUI Apps
depends+=('vlc' 'p7zip' 'ranger'  'rxvt-unicode-terminfo' 'alacritty' 'firefox-developer-edition')
# Multimedia
depends+=('w3m' 'mpd' 'ffmpeg' 'ncmpcpp' 'mpc')
# Android
depends+=('android-file-transfer' 'android-udev' 'android-tools')
# Optional packages
## Network
optdepends=('openvpn' 'wireguard-tools')
## CLI
optdepends+=('bat' 'gtop' 'ldm')
## GUI
optdepends+=('filezilla')
### Office
optdepends+=('wps-office')
### Images
optdepends+=('krita')
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
  ## Daily script
  install -m640 "$srcdir/wl-4rch-main/.taskrc" -t "$pkgdir$HOME/"
  chown -R $USER:users $pkgdir$HOME
  install -m644 "$srcdir/wl-4rch-main/dnsmasq.conf" -t "$pkgdir/etc/"
  install -m644 "$srcdir/wl-4rch-main/default.conf" -t "$pkgdir/etc/lxc/"
  install -m644 "$srcdir/wl-4rch-main/lxc-net" -t "$pkgdir/etc/default/"
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
	install -m600 "$srcdir/wl-4rch-main/iftop" "/etc/sudoers.d/iftop"
	systemctl enable mpd.service
	systemctl enable mpd.socket
	systemctl enable lxc-net.service
	systemctl enable ntpd.service
}
