from src.services.hyprland_keybinds.common import KeyBind

key_binds = (
    KeyBind(
        ("", "XF86AudioPlay"),
        ("exec", "hyprpeazctl player play-pause")
    ),
    KeyBind(
        ("", "XF86AudioPause"),
        ("exec", "hyprpeazctl player pause")
    ),
    KeyBind(
        ("", "XF86AudioNext"),
        ("exec", "hyprpeazctl player next")
    ),
    KeyBind(
        ("", "XF86AudioPrev"),
        ("exec", "hyprpeazctl player previous")
    ),
    KeyBind(
        ("", "XF86Lock"),
        ("exec", "hyprpeazctl lock")
    ),
    KeyBind(
        ("", "XF86Tools"),
        ("exec", "hyprpeazctl settings")
    ),
    KeyBind(
        ("", "XF86Calculator"),
        ("exec", "hyprpeazctl qalculate-gtk")
    )
)
