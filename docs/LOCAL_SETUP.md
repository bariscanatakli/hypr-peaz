# HyprPeaz Local Setup

This documents a fully local (no `/usr` writes) setup that keeps assets and binaries under your home directory so you can iterate safely.

## Paths

- Assets/configs: `~/.local/share/hyprpeaz/hyprpeaz-assets`
- Python code: `~/.local/lib/hyprpeaz/hyprpeaz`
- Binaries: `~/.local/bin` (`hyprpeaz-start`, `hyprpeazctl`, `hyprpeaz-crash-dialog`)
- Wayland sessions: `~/.local/share/wayland-sessions`

Environment variables (export once per shell or add to your shell rc):

```bash
export HYPRPEAZ_ASSETS="$HOME/.local/share/hyprpeaz/hyprpeaz-assets"
export HYPRPEAZ_LIB="$HOME/.local/lib/hyprpeaz/hyprpeaz"
export PATH="$HOME/.local/bin:$PATH"
```

## One-time sync from the repo

From the repo root:

```bash
./tools/sync-local.sh
```

What it does:
- Rebuilds C helpers (`build/build.sh`)
- Copies `hyprpeaz/` and `hyprpeaz-assets/` to the XDG-style paths above
- Copies rebuilt binaries to `~/.local/bin`
- Installs session files to `~/.local/share/wayland-sessions`

## Running

- From DM: select **HyprPeaz** (session file points to `~/.local/share/hyprpeaz/hyprpeaz-assets/configs/hyprland/main.conf`).
- From TTY (ensure no other Hyprland is running):
  ```bash
  export HYPRPEAZ_ASSETS="$HOME/.local/share/hyprpeaz/hyprpeaz-assets"
  export HYPRPEAZ_LIB="$HOME/.local/lib/hyprpeaz/hyprpeaz"
  export PATH="$HOME/.local/bin:$PATH"
  hyprpeaz-start
  # or hyprland --config "$HYPRPEAZ_ASSETS/configs/hyprland/main.conf"
  ```

To exit the session cleanly from inside HyprPeaz:
```bash
hyprctl dispatch exit
```

## Keeping in sync

After making repo changes:
```bash
./tools/sync-local.sh
```
to refresh local copies and binaries. Remove the local tree with:
```bash
rm -rf ~/.local/share/hyprpeaz ~/.local/lib/hyprpeaz
```
