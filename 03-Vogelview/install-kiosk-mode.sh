#!/usr/bin/env bash

if [ -z "$1" ]; then
    echo "Error: No argument provided.
Usage: ./install-kiosk-mode.sh <url>"
    exit 1
fi

url="$1"

KIOSK_MODE_CONF_HEADER="## Kiosk Mode"
KIOSK_MODE_XINITRC='/etc/xdg/openbox/autostart'
KIOSK_MODE_BASHRC="${HOME_PATH}/.bashrc"
KIOSK_MODE_CHROMIUM_CUSTOM_DISABLE_UPDATE_CHECK='/etc/chromium-browser/customizations/01-disable-update-check'
KIOSK_MODE_CHROMIUM_FLAG_UPDATE_INTERVAL='--check-for-update-interval=31536000'

_kiosk_mode_install_os_dependencies() {
  echo "Install Kiosk Mode dependencies"
  # Resource:
  # https://blog.r0b.io/post/minimal-rpi-kiosk/
  sudo apt-get -qq -y install --no-install-recommends \
    xserver-xorg \
    x11-xserver-utils \
    xinit \
    openbox \
    chromium-browser
}

_kiosk_mode_set_autostart() {
  echo "Configure Kiosk Mode"
  local url="$1"
  local _DISPLAY='$DISPLAY'
  local _XDG_VTNR='$XDG_VTNR'

  tee -a "${KIOSK_MODE_BASHRC}" <<-EOF

${KIOSK_MODE_CONF_HEADER}
[[ -z $_DISPLAY && $_XDG_VTNR -eq 1 ]] && startx -- -nocursor

EOF

  sudo tee -a "${KIOSK_MODE_XINITRC}" <<-EOF

${KIOSK_MODE_CONF_HEADER}
# Disable any form of screen saver / screen blanking / power management
xset s off
xset s noblank
xset -dpms

# Start Chromium in kiosk mode
sed -i 's/"exited_cleanly":false/"exited_cleanly":true/' ~/.config/chromium/'Local State'
sed -i 's/"exited_cleanly":false/"exited_cleanly":true/; s/"exit_type":"[^"]\+"/"exit_type":"Normal"/' ~/.config/chromium/Default/Preferences
chromium-browser ${url} \
  --disable-infobars \
  --disable-pinch \
  --disable-translate \
  --kiosk \
  --noerrdialogs \
  --no-first-run

EOF
}

_kiosk_mode_update_settings() {
  # Resource: https://github.com/Thyraz/Sonos-Kids-Controller/blob/d1f061f4662c54ae9b8dc8b545f9c3ba39f670eb/README.md#kiosk-mode-installation
  sudo mkdir -p $(dirname "${KIOSK_MODE_CHROMIUM_CUSTOM_DISABLE_UPDATE_CHECK}")
  sudo rm -f "${KIOSK_MODE_CHROMIUM_CUSTOM_DISABLE_UPDATE_CHECK}"
  sudo tee -a "${KIOSK_MODE_CHROMIUM_CUSTOM_DISABLE_UPDATE_CHECK}" <<-EOF
${KIOSK_MODE_CONF_HEADER}
CHROMIUM_FLAGS=\"\$\{CHROMIUM_FLAGS\} --check-for-update-interval=31536000\"
EOF
}


_kiosk_mode_install_os_dependencies
_kiosk_mode_set_autostart "$url"
_kiosk_mode_update_settings
