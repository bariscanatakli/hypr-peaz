# HyprPeaz recent changes

## Local workflow
- `tools/sync-local.sh` now rebuilds, syncs to `~/.local`, and stamps `hyprpeaz/version.txt` with `local-<timestamp>-<git-hash>` so the UI shows a fresh version after each sync.
- Default configs point to local paths (`~/.local/share/hyprpeaz/hyprpeaz-assets`, `~/.local/lib/hyprpeaz/hyprpeaz`). Export `HYPRPEAZ_ASSETS`/`HYPRPEAZ_LIB`/`PATH` in your shell rc.
- `hyprpeazctl reload` only works when a HyprPeaz session is running; otherwise it cannot reach the socket.
- If you see missing wallpaper/DBus XML errors, rerun `./tools/sync-local.sh` (and `chown` `~/.local/share|lib|cache/hyprpeaz` to your user if needed) to restore assets under `~/.local/share/hyprpeaz`.

## Keyboard layout indicator
- The bar always shows the current layout; clicking it cycles configured layouts via `hyprctl switchxkblayout`.
- Add multiple layouts in **Settings → Keyboard** (e.g., `us,tr`) and keep a change-layout keybind for keyboard-driven toggling.

## Audio panel context menus
- Speakers: right-click to mute/unmute and set default output.
- Streams (apps): right-click to mute/unmute or “Move to” another output; actions log to `/tmp/hyprpeaz_audio.log` for debugging `pactl` moves.
- Popovers are created per item, preventing earlier crashes from missing menus.

## Version visibility
- The version label in the UI reads `hyprpeaz/version.txt`; local sync writes `local-...` so you can confirm the running build after each sync.
