# HyprPeaz

> This project is not affiliated with or sponsored by Google.

![GitHub commit activity](https://img.shields.io/github/commit-activity/m/bariscanatakli/hypr-peaz?style=for-the-badge&labelColor=%23424242&color=%23B2FF59)
![GitHub repo size](https://img.shields.io/github/repo-size/bariscanatakli/hypr-peaz?style=for-the-badge&labelColor=%23424242&color=%2384FFFF)
![GitHub Repo stars](https://img.shields.io/github/stars/bariscanatakli/hypr-peaz?style=for-the-badge&labelColor=%23424242&color=%23B9F6CA)
![GitHub contributors](https://img.shields.io/github/contributors/bariscanatakli/hypr-peaz?style=for-the-badge&labelColor=%23424242&color=%23FFAB40)
![GitHub License](https://img.shields.io/github/license/bariscanatakli/hypr-peaz?style=for-the-badge&labelColor=%23424242&color=%23FF9E80)

HyprPeaz (formerly hyprland-material-you v2 / HyprYou). It aims to provide a modern, feature-rich, and visually appealing desktop configuration. Here are some key features:

- **Material You Colors**: The project generates colors for your apps based on you wallpapers or settings.
- **Fluid Animations**: Expect natural and fluid animations throughout the desktop experience.
- **Design**: The design wherever possible is made by [Material 3 design](https://m3.material.io/)
- **Settings**: Almost all settings are possible to configure in settings! You don't need to change hyprland.conf unless you need something specific.
- **Clean home folder**: I made everything so won't have any unnecessary files in home. And from settings you can enable configs for terminals or anything else.

> [!TIP]
> When you run HyprPeaz as DE session (from SDDM, Greetd, etc.) it doesn't use `~/.config/hypr/hyprland.conf`  
> For any custom variables/configs look for `~/.config/hyprpeaz/hyprland.conf`  
> I made that so you can have different dotfiles on one system  
> If you don't have Display Manager you can use `hyprland --config /usr/share/hyprpeaz/configs/hyprland/main.conf`

> [!NOTE]
> If you want to talk or to check devlogs go to our Discord server  
> <https://discord.gg/nCK3sh8mNU>

## Packages info

- `hyprpeaz` - The main package, should be installed before anything else
- `hyprpeaz-utils` - Replacement of `hyprland-qtutils`, uses gtk4 for hyprland dialogs instead of qt
- `hyprpeaz-greeter` - Configs for greetd, so it's replacement of SDDM or anything like that. With Material 3 theme.

## How to install (Arch)

> [!TIP]
> If you have an error like "cannot resolve dependency" you should install packages that are named there with `yay` or any other AUR helpers.  
> For very new people to ArchLinux, check this: <https://itsfoss.com/install-yay-arch-linux/>  
> Also if AUR is down (it happens sometimes) you can check for Chaotic AUR: <https://aur.chaotic.cx/>  
> And if you have errors like `Config error in file /....` just try using `hyprctl reload`

<details>
    <summary>Manual installation</summary>

- Clone repository: `git clone --depth=1 https://github.com/bariscanatakli/hypr-peaz.git`
- Install all dependencies from depends.txt
- Build Cython code by using `build.sh` in `hyprpeaz/`
- Then copy `hyprpeaz` to `/usr/lib/hyprpeaz` and copy `hyprpeaz-assets` to `/usr/share/hyprpeaz`
- Then use `build.sh` in `build`
- Move `hyprpeazctl`, `hyprpeaz-start`, `hyprpeaz-crash-dialog` to `/usr/bin`
- Copy `assets/hyprpeaz.desktop` to `/usr/share/wayland-sessions/`
- And run it as `HyprPeaz` from your display manager (Not `Hyprland`!!)
- Optional:
  - You can build `hyprpeaz-utils` or `hyprpeaz-greeter` if you want  
    > By using `makepkg -si` in `greeter` for `hyprpeaz-greeter` or in `hyprpeaz-utils`

</details>
<details>
    <summary>Automatic installation</summary>

- **Pre-built (AUR):**
  > The easiest way
  - Use `yay`, `paru` or any other AUR helper to install it.
  - To see what packages are available just run `yay -Ss hyprpeaz`

- **Pre-built:**
  - Install needed packages from [releases](https://github.com/bariscanatakli/hypr-peaz/releases)
  - Use `sudo pacman -U <file name>` change `<file name>` to name of the package you downloaded and make sure you're in Downloads folder
    > Yea some people were trying to use `pacman -U` in home folder so I had to say that

- **Build manually:**
  - `hyprpeaz` - Use `makepkg -si`
  - `hyprpeaz-greeter` - Use `makepkg -si` in `greeter/`
  - `hyprpeaz-utils` - Use `makepkg -si` in `hyprpeaz-utils/`

</details>

## License and attribution

- License: GPLv3 (see `LICENSE`). This fork is maintained by bariscanatakli and is based on the upstream hyprland-material-you project.
- If you redistribute binaries or modified versions, you must also provide the complete corresponding source code under the same GPLv3 terms.
- Keep copyright and license notices intact and clearly mark your modifications (git history or release notes are fine).
- There is no warranty; use at your own risk (see the warranty disclaimer in `LICENSE`).
- For consumer devices, ensure users can install modified versions (anti-tivoization requirement in GPLv3).

## Thanks to

- All people from my discord server
- All Sponsors (I love y'all!)
- [Astal](https://github.com/Aylur/astal): For Bluetooth and WirePlumber services
- [Gtk4LayerShell](https://github.com/wmww/gtk4-layer-shell): For LayerShell
- [Hyprland](https://github.com/hyprwm/Hyprland): For the best TWM I've ever seen
- [Shxmz](https://github.com/shxmz): submitted it to AUR
- Maybe that's it

## Cool numbers (maybe)
[![Stargazers over time](https://starchart.cc/bariscanatakli/hypr-peaz.svg?variant=adaptive)](https://starchart.cc/bariscanatakli/hypr-peaz)

## Local setup
- For a fully local (no `/usr` writes) install, see `docs/LOCAL_SETUP.md`.
- For the latest session changes and tips, see `docs/CHANGES.md`.
