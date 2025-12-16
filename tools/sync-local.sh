#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

ASSETS_DST="${HOME}/.local/share/hyprpeaz"
LIB_DST="${HOME}/.local/lib/hyprpeaz"
BIN_DST="${HOME}/.local/bin"
SESSION_DST="${HOME}/.local/share/wayland-sessions"

echo "[HyprPeaz] Building C helpers…"
(
  cd "${REPO_ROOT}/build"
  ./build.sh
)

echo "[HyprPeaz] Syncing assets and code to ${ASSETS_DST} and ${LIB_DST}…"
rm -rf "${ASSETS_DST}" "${LIB_DST}"
mkdir -p "${ASSETS_DST}" "${LIB_DST}" "${BIN_DST}" "${SESSION_DST}"
cp -a "${REPO_ROOT}/hyprpeaz-assets" "${ASSETS_DST}/"
cp -a "${REPO_ROOT}/hyprpeaz" "${LIB_DST}/"

# Stamp a version string (commit + UTC timestamp) for UI display
VERSION_HASH="$(cd "${REPO_ROOT}" && git rev-parse --short HEAD 2>/dev/null || echo "nogit")"
VERSION_TS="$(date -u +%Y%m%d-%H%M%S)"
echo "local-${VERSION_TS}-${VERSION_HASH}" > "${LIB_DST}/hyprpeaz/version.txt"

echo "[HyprPeaz] Installing binaries to ${BIN_DST}…"
install -m755 "${REPO_ROOT}/build/hyprpeaz-start" "${BIN_DST}/hyprpeaz-start"
install -m755 "${REPO_ROOT}/build/hyprpeazctl" "${BIN_DST}/hyprpeazctl"
install -m755 "${REPO_ROOT}/build/hyprpeaz-crash-dialog" "${BIN_DST}/hyprpeaz-crash-dialog"

echo "[HyprPeaz] Installing session files to ${SESSION_DST}…"
install -m644 "${REPO_ROOT}/assets/hyprpeaz.desktop" "${SESSION_DST}/hyprpeaz.desktop"
if [ -f "${REPO_ROOT}/assets/hyprpeaz-fallback.desktop" ]; then
  install -m644 "${REPO_ROOT}/assets/hyprpeaz-fallback.desktop" "${SESSION_DST}/hyprpeaz-fallback.desktop"
fi

cat <<'INFO'
[HyprPeaz] Done.
Ensure these are set (add to your shell rc for permanence):
  export HYPRPEAZ_ASSETS="$HOME/.local/share/hyprpeaz/hyprpeaz-assets"
  export HYPRPEAZ_LIB="$HOME/.local/lib/hyprpeaz/hyprpeaz"
  export PATH="$HOME/.local/bin:$PATH"
INFO
