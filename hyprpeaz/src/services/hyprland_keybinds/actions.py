from src.services.hyprland_keybinds.common import KeyBind, main_mod, Category

key_binds = (
    KeyBind(
        (main_mod, "SHIFT", "A"),
        ("exec", "hyprpeazctl toggle_animations"),
        "Toggle all animations",
        Category.ACTIONS
    ),
    KeyBind(
        (main_mod, "SHIFT", "S"),
        ("exec", "hyprpeazctl screenshot region"),
        "Screenshot",
        Category.ACTIONS
    ),
    KeyBind(
        (main_mod, "CTRL", "S"),
        ("exec", "hyprpeazctl screenshot window"),
        "Screenshot of window",
        Category.ACTIONS
    ),
    KeyBind(
        (main_mod, "ALT", "S"),
        ("exec", "hyprpeazctl screenshot active"),
        "Screenshot of active screen",
        Category.ACTIONS
    ),
    KeyBind(
        (main_mod, "SHIFT", "F"),
        ("exec", "hyprpeazctl screenshot region freeze"),
        "Screenshot and freeze",
        Category.ACTIONS
    ),
    KeyBind(
        (main_mod, "CTRL", "F"),
        ("exec", "hyprpeazctl screenshot window freeze"),
        "Screenshot of window and freeze",
        Category.ACTIONS
    ),
    KeyBind(
        (main_mod, "ALT", "F"),
        ("exec", "hyprpeazctl screenshot active freeze"),
        "Screenshot of active screen and freeze",
        Category.ACTIONS
    ),
    KeyBind(
        (main_mod, "SHIFT", "W"),
        ("exec", "hyprpeazctl wallpaper random"),
        "Change wallpaper to random one",
        Category.ACTIONS
    ),
    KeyBind(
        (main_mod, "SHIFT", "R"),
        ("exec", "hyprpeazctl reload"),
        "Restart HyprPeaz",
        Category.ACTIONS
    ),
    KeyBind(
        (main_mod, "L"),
        ("exec", "hyprpeazctl lock"),
        "Lock screen",
        Category.ACTIONS
    )
)
