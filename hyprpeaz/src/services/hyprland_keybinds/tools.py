from src.services.hyprland_keybinds.common import KeyBind, main_mod, Category

key_binds = (
    KeyBind(
        (main_mod, "Z"),
        ("exec", "hyprpeazctl toggle_window players"),
        "Players",
        Category.TOOLS
    ),
    KeyBind(
        (main_mod, "period"),
        ("exec", "hyprpeazctl open_window emojis"),
        "Emoji picker",
        Category.TOOLS
    ),
    KeyBind(
        (main_mod, "CTRL", "C"),
        ("exec", "hyprpeazctl toggle_window cliphist"),
    ),
    KeyBind(
        (main_mod, "V"),
        ("exec", "hyprpeazctl toggle_window cliphist"),
        "Clipboard history",
        Category.TOOLS
    ),
    KeyBind(
        (main_mod, "SLASH"),
        ("exec", "hyprpeazctl toggle_window keybindings"),
        "List of keybindings",
        Category.TOOLS
    ),
    KeyBind(
        (main_mod, "CTRL", "W"),
        ("exec", "hyprpeazctl settings wallpaper"),
        "Open wallpaper settings",
        Category.TOOLS
    ),
    KeyBind(
        (main_mod, "SPACE"),
        ("exec", "hyprpeazctl toggle_window apps_menu"),
        "App Launcher",
        Category.TOOLS
    ),
    KeyBind(
        (main_mod, "W"),
        ("exec", "hyprpeazctl toggle_window sidebar"),
        "Sidebar",
        Category.TOOLS
    ),
    KeyBind(
        (main_mod, "A"),
        ("exec", "hyprpeazctl toggle_window clients"),
        "Opened windows",
        Category.TOOLS
    ),
    KeyBind(
        (main_mod, "D"),
        ("exec", "hyprpeazctl settings"),
        "Open settings",
        Category.TOOLS
    )
)
